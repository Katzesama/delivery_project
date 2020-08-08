var holder = document.getElementById("holder");
var footer = document.getElementById("footer");

function show_order(data) {
  //clear the older content from last request
  while(holder.hasChildNodes()){
    holder.removeChild(holder.firstChild);
  }

  while(footer.hasChildNodes()){
    footer.removeChild(footer.firstChild);
  }

  // loop through and create a section for each order sent by at the current page
  for (var i = 0; i < data.orders.length; i++) {
    // most outter container of the order section
    let container = document.createElement("div");
    container.setAttribute("class", "col-md-8 mr-3 mb-4");
    holder.appendChild(container);

    let order = document.createElement("div");
    order.setAttribute("class", "card shadow mb-4");
    container.appendChild(order);

    // add header to the order section
    let header_ct = document.createElement("div");
    header_ct.setAttribute("class", "card-header py-3");
    order.appendChild(header_ct);
    let header = document.createElement("h6");
    header.setAttribute("class", "m-0 font-weight-bold text-primary");
    header.innerHTML = "订单号：" + data.orders[i].order_num;
    header_ct.appendChild(header);

    // add the body part to the order section
    let body = document.createElement("div");
    body.setAttribute("class", "card-body row no-gutters align-items-center");
    order.appendChild(body);
    // display the information of the order
    let order_info = document.createElement("div");
    order_info.setAttribute("class", "mr-2");
    body.appendChild(order_info);
    // deliver address of the order
    let deliver_addr = document.createElement("div");
    deliver_addr.setAttribute("class", "h6 mb-1 font-weight-bold text-gray-800");
    deliver_addr.innerHTML = "" + data.orders[i].deliver_address;
    order_info.appendChild(deliver_addr);
    // phone number and the email address of the custormer
    let customer_phone = document.createElement("div");
    customer_phone.setAttribute("class", "h6 font-weight-bold text-gray-800 mb-1");
    customer_phone.innerHTML = "顾客号码：" + data.orders[i].customer_phone;
    order_info.appendChild(customer_phone);
    let customer_email = document.createElement("div");
    customer_email.setAttribute("class", "h6 font-weight-bold text-gray-800 mb-1");
    customer_email.innerHTML = "顾客邮箱：" + data.orders[i].customer_email;
    order_info.appendChild(customer_email);
    // total price and the detail of the order
    // hide the detail and show when button clicks
    let order_detail = document.createElement("div");
    customer_email.setAttribute("class", "h6 font-weight-bold text-gray-800 mb-1");
    order_info.appendChild(order_detail);
    let total_price = document.createElement("p");
    total_price.setAttribute("class", "h6 text-gray-800 mt-3");
    total_price.innerHTML = "总价：" + data.orders[i].total_price;
    order_detail.appendChild(total_price);
    let more_detail = document.createElement("div");
    more_detail.setAttribute("class", "h7 font-weight-light text-gray-800");
    more_detail.style = "display:none;";
    more_detail.id = "more_detail";
    order_detail.appendChild(more_detail);
    let detail_header = document.createElement("p");
    detail_header.setAttribute("class", "h6 text-gray-800");
    detail_header.innerHTML = "详情："
    more_detail.appendChild(detail_header);
    console.log(data.orders[i].detail);
    console.log(typeof data.orders[i].detail);
    // get and paste a list of dish name, quantity, price (eg. ["rice", "2", "5.00"])
    let dish_list = JSON.parse('[["煲仔饭",  "x1",  "$15.00", "啤酒,kekeekekekkekeekkekekekeke"], ["煲仔饭",  "1",  "15.00", "啤酒"]]');
    for(let j = 0, count = dish_list.length; j < count; j++) {
        let dish = dish_list[j];
        let dish_holder = document.createElement("p");
        more_detail.appendChild(dish_holder);
        for(let k = 0, count = dish.length; k < count; k++){
          let dish_info = document.createElement("span");
          dish_info.setAttribute("class", "mr-3");
          dish_info.innerHTML = dish[k];
          dish_holder.appendChild(dish_info);
        }
    }
    // show more detail button
    let show_more = document.createElement("button");
    show_more.setAttribute("class", "btn btn-light text-grey-600");
    show_more.innerHTML = "详情";
    show_more.onclick=function(){
      if (more_detail.style.display === "none") {
        this.innerHTML = "收起";
        more_detail.style.display = "inline";
      } else {
        this.innerHTML = "详情";
        more_detail.style.display = "none";
      }
    }
    order_detail.appendChild(show_more);

    body.appendChild(document.createElement("br"));
    // select the status of the order
    let order_status = document.createElement("select");
    order_status.setAttribute("class", "mr-2 mt-2");
    body.appendChild(order_status);
    let processing = document.createElement("option");
    processing.value = "处理中";
    processing.innerHTML = "处理中";
    let delivering = document.createElement("option");
    delivering.value = "送餐中";
    delivering.innerHTML = "送餐中";
    let done = document.createElement("option");
    done.value = "完成";
    done.innerHTML = "完成";
    let refunding = document.createElement("option");
    refunding.value = "退款中";
    refunding.innerHTML = "退款中";
    let refunded = document.createElement("option");
    refunded.value = "已退款";
    refunded.innerHTML = "已退款";
    switch(data.orders[i].status){
      case "处理中":
        processing.selected = true;
        break;
      case "送餐中":
        delivering.selected = true;
        break;
      case "完成":
        done.selected = true;
        break;
      case "退款中":
        refunding.selected = true;
        break;
      case "已退款":
        refunded.selected = true;
    }
    order_status.appendChild(processing);
    order_status.appendChild(delivering);
    order_status.appendChild(done);
    order_status.appendChild(refunding);
    order_status.appendChild(refunded);


    let order_footer = document.createElement("div");
    order_footer.setAttribute("class", "card-footer");
    order.appendChild(order_footer);
    // buttons to manipulate the dish info
    var save_button = document.createElement("button");
    save_button.innerHTML = '储存';
    save_button.setAttribute("class", "mr-2 mt-2 btn btn-primary");
    let order_id = data.orders[i].id;
    let order_url = "../" + order_id + "/";
    save_button.onclick=function(){
      // https://stackoverflow.com/questions/17832194/get-javascript-variables-value-in-django-url-template-tag
      let order_data = new FormData();
      order_data.append('status', order_status.options[order_status.selectedIndex].value);

      updateOrder(order_url, order_data);
    };
    order_footer.appendChild(save_button);

  }

  // footer part
  // get previous page
  if (data.previous != null)
  {
    let preButton = document.createElement("button");
    preButton.setAttribute("class", "btn btn-light text-grey-600");
    preButton.style = "width=auto;display:inline-block;";
    preButton.innerHTML = '前一页';
    preButton.onclick=function(){
      get_data_display(data.previous);
    };
    footer.appendChild(preButton);
  }

  // https://stackoverflow.com/questions/30864011/display-only-some-of-the-page-numbers-by-django-pagination
  // page number buttons
  for (let i = 1; i <= data.count; i++) {
    let page_button = document.createElement("button");
    page_button.setAttribute("class", "btn btn-light text-grey-600");
    page_button.style = "width=auto;display:inline-block;";
    page_button.innerHTML = i.toString();
    if (i == data.current){
      page_button.disabled = "true";
      footer.appendChild(page_button);
    }
    else if (i > data.current - 3 || i < data.current + 3) {
      page_button.onclick = function(){
        get_data_display('./api/?page=' + i.toString());
      };
      footer.appendChild(page_button);
    }
  }

  // get next page
  if (data.next != null)
  {
    let nextButton = document.createElement("button");
    nextButton.setAttribute("class", "btn btn-light text-grey-600");
    nextButton.style = "width=auto;display:inline-block;";
    nextButton.innerHTML = '后一页';
    nextButton.onclick=function(){
      get_data_display(data.next);
    };
    footer.appendChild(nextButton);
  }
}

function updateOrder(url, order_data) {
var request = new XMLHttpRequest();
request.onreadystatechange = function () {
    if (request.readyState==4) {
        try {
            if (request.status==200) {
              document.location.reload(true);
              }
            else{
              alert("网页出了问题: " + this.responseXML);
            }
        }
        catch(e) {
            alert("传送出了问题: " + e.name);
        }
    }
};
request.open("POST", url);
request.setRequestHeader("X-CSRFToken", csrftoken);
request.send(order_data);
}


// https://uofa-cmput404.github.io/cmput404-slides/08-AJAX.html#/9
// https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch
function fetchJSON(url) {
  var request = new Request(url, {
              method: 'GET',
              headers: {
                   'Content-Type': 'application/json'
              },
              });
  return fetch(request).then((response) => {
    if (response.status === 200) { // OK
      return response.json(); // return a Promise
    } else {
      alert("Something went wrong: " + response.status);
    }
  });
}


function get_data_display(url) {
    fetchJSON(url).then(show_order);
}
