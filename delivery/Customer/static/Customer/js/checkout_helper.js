function display_content(data){
  if (data === "Overtime"){
    alert("订单超时，返回菜单页面");
    location.href = menu_url;
  }

  let address = document.getElementById("deliver_address");
  let phone = document.getElementById("customer_phone");
  let email = document.getElementById("customer_email");

  address.value = data.deliver_address;
  phone.value = data.customer_phone;
  email.value = data.customer_email;

  while(order_info.hasChildNodes()){
      order_info.removeChild(order_info.firstChild);
  }

  /*if (!data.total_price){
    checkout_price.innerHTML = "0.00";
  } else {
    checkout_price.innerHTML = data.total_price.toFixed(2);
  }*/

    for (let i =0; i <  data.items.length; i++){
      let orderitem = data.items[i];
      let detail = JSON.parse(orderitem.detail);
      let order = document.createElement("div");
      order.setAttribute("class", "justify-content-between");
      order.setAttribute('data-id' , orderitem.num);
      order_info.appendChild(order);
      // ['name']['price']['options']['quantity']
      let line1 = document.createElement("div");
      order.appendChild(line1);
      let quantity = document.createElement("span");
      quantity.setAttribute("class", "mr-2");
      quantity.innerHTML = "x" + detail['quantity'];
      line1.appendChild(quantity);
      let name = document.createElement("span");
      name.setAttribute("class", "mr-5");
      name.innerHTML = detail["name"];
      line1.appendChild(name);
      let price = document.createElement("span");
      price.innerHTML = "$" + detail["price"];
      line1.appendChild(price);
      let line2 = document.createElement("div");
      order.appendChild(line2);
      let options = document.createElement("span");
      options.setAttribute("class", "font-weight-light font-italic text-gray-500");
      options.innerHTML = detail["options"];
      line2.appendChild(options);
      let remove_button = document.createElement("a");
      remove_button.setAttribute("class", "ml-5");
      remove_button.href = "#";
      line1.appendChild(remove_button);
      remove_button.addEventListener('click', function(e){
              e.preventDefault();
              let remove_info = {'key': orderitem.num, 'price': detail['price']};
              removeOrders(shopping_cart_url, JSON.stringify(remove_info)).then(data => {
                if (data === "sucess") {
                  //checkout_price.innerHTML = (parseFloat(checkout_price.innerHTML) - parseFloat(value['price'])).toFixed(2);
                  order.remove();
                  if (!order_info.hasChildNodes()){
                    alert("购物车为空，返回菜单。");
                    location.href = menu_url;
                  }
                }
              });
      }, false);
      let icon = document.createElement("i");
      icon.setAttribute("class", "fa fa-minus");
      remove_button.appendChild(icon);
      let divider = document.createElement("hr");
      divider.style = "width:35%;margin-left:0;";
      order.appendChild(divider);
    }

}

function fetchOrders(url) {
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
      alert("网页出了问题，无法取得订单详情: " + response.status);
    }
  });
}

function removeOrders(url, remove_data) {
  var request = new Request(url, {
              method: 'DELETE',
              headers: {
                   'Content-Type': 'application/json',
                   'X-CSRFToken': csrf_token
              },
              body: remove_data,
              });
  return fetch(request).then((response) => {
    if (response.status === 204) { // OK
      return "sucess"; // return a Promise
    } else {
      alert("订单超时，返回菜单页面。");
      location.href = menu_url;
    }
  });
}
