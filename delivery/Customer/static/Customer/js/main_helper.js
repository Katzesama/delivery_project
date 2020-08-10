var cart_info = document.getElementById("shopping_cart");
var store_info = document.getElementById("store_info");
var dish_info = document.getElementById("dish_info");
var dishes_holder = document.getElementById("dishes_holder");
var kind_holder = document.getElementById("category_content");

var body = document.getElementById("page-top");

/*
shopping cart sidebar popup
*/

function cart_close() {
  cart_info.style.display = "none";
}


function cart_onclick() {

  if (cart_info.style.display === "none") {
    cart_info.style.display = "block";
    display_cart();
  }
}

function display_cart(){
  let data = fetchOrders("{% url 'shopping_cart' %}");
  let cart_content = document.getElementById("shopping_cart_content");
  for (let [key, value] of data.order_detail){
    let order = document.createElement("li");
    order.class = "nav-item active justify-content-between";
    order.setAttribute('data-id' , key.toString());
    cart_content.appendChild(order);
    // ['name']['price']['options']['quantity']
    let line1 = document.createElement("div");
    order.appendChild(line1);
    let quantity = document.createElement("span");
    quantity.class = "mr-2";
    quantity.innerHTML = "x" + value['quantity'];
    line1.appendChild(quantity);
    let name = document.createElement("span");
    name.class = "mr-5";
    name.innerHTML = value["name"];
    line1.appendChild(name);
    let line2 = document.createElement("div");
    order.appendChild(line2);
    let price = document.createElement("span");
    price.innerHTML = "$" + value["price"];
    line2.appendChild(price);
    let remove_button = document.createElement("a");
    remove_button.class = "ml-5";
    remove_button.href = "#";
    line2.appendChild(remove_button);
    remove_button.addEventListener('click', function(e){
            e.preventDefault();
            let remove_info = key;
            removeOrders("{% url 'shopping_cart' %}", JSON.stringify(remove_info)).then(function(){
              order.remove();
            });
    }, false);
    let icon = document.createElement("i");
    icon.class = "fa fa-minus";
    remove_button.appendChild(icon);
  }

  // checkout
  let checkout_button = document.getElementById("checkout");
  checkout_button.addEventListener('click', function(e){
          checkoutOrders("{% url 'shopping_cart' %}");
  }, false);
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
      return [];
    }
  });
}

function removeOrders(url, remove_data) {
  var request = new Request(url, {
              method: 'POST',
              headers: {
                   'Content-Type': 'application/json'
              },
              data: remove_data,
              });
  return fetch(request).then((response) => {
    if (response.status === 200) { // OK
      return response.json(); // return a Promise
    } else {
      alert("Something went wrong: " + response.status);
    }
  });
}

function checkoutOrders(url) {
  var request = new Request(url, {
              method: 'PUT',
              headers: {
                   'Content-Type': 'application/json'
              },
              });
  return fetch(request).then((response) => {
    if (response.status === 200) { // OK
      location.href = '/order/' + response.json(); // redirect
    } else {
      alert("Something went wrong: " + response.status);
    }
  });
}
/*
store information window popup
*/

function store_info_onclick() {
  store_info.style.display = "block";
  body.classList.add("modal-open");
  display_store_info();
}


function store_info_close() {

  store_info.style.display = "none";
  body.classList.remove("modal-open");
}

function display_store_info(){
  let data = fetchJSON('/store/');
  let contact_holder = document.getElementById("store_contact_info");
  let wechat_num = document.createElement("span");
  wechat_num.innerHTML = "微信号：" + data.wechat;
  contact_holder.appendChild(wechat_num);
  let phone = document.createElement("span");
  phone.innerHTML = "电话：" + data.phone;
  contact_holder.appendChild(phone);
  let wechat_code = document.createElement("img");
  wechat_code.class = "img-fluid px-3 px-sm-4 mt-3 mb-4";
  wechat_code.style = "width: 25rem;";
  wechat_code.src = data.wechatcode;
  contact_holder.appendChild(wechat_code);
  let open_hour_holder = document.getElementById("store_open_info");
  // add the openning hours later
}


/*
dish information window popup
*/

function get_dish_info(id) {
  dish_info.style.display = "block";
  body.classList.add("modal-open");
  let dishurl = "./dishes/" + id + "/";
  fetchJSON(dishurl).then(display_dish_info);
}

function dish_info_close() {
  dish_info.style.display = "none";
  body.classList.remove("modal-open");
}

function display_dish_info(data){
  let submit_button = document.getElementById("dish_submit");
  let minus_dish_button = document.getElementById("dish_quan_minus");
  let plus_dish_button = document.getElementById("dish_quan_plus");
  let dish_quantity = document.getElementById("dish_quantity");
  let total_price_tag = document.getElementById("dish_total_price");
  let dish_price = data.price;
  let total_price = data.price;
  let dish_image = document.getElementById("dish_info_img");
  let options_holder = document.getElementById("dish_info_options");

  let dish_name = document.getElementById("dish_name");
  dish_name.innerHTML = data.name;

  let content_holder = document.getElementById("dish_info_content");
  if (data.picture){
    dish_image.src = data.picture;
  } else {
    dish_image.src = "../static/Manager/images/defaultimage.jpg/";
  }


  while(options_holder.hasChildNodes()){
      options_holder.removeChild(options_holder.firstChild);
  }
  for (let i=0; i < data.options.length; i++){
    let option = data.options[i];
    let option_holder = document.createElement("div");
    option_holder.setAttribute("class", "d-flex");
    options_holder.appendChild(option_holder);
    // input checkbox part
    let input_holder = document.createElement("div");
    option_holder.appendChild(input_holder);
    let input_checkbox = document.createElement("input");
    input_checkbox.type = "checkbox";
    input_checkbox.name = "option" + i.toString();
    input_checkbox.value = option.detail;
    input_holder.appendChild(input_checkbox);
    let after_part = document.createElement("div");
    after_part.setAttribute("class", "col-md-11");
    option_holder.appendChild(after_part);
    let input_label = document.createElement("label");
    input_label.setAttribute("class", "d-flex justify-content-between");
    input_label.for = "option" + i.toString();
    after_part.appendChild(input_label);
    let label_title = document.createElement("span");
    label_title.innerHTML = option.detail;
    input_label.appendChild(label_title);
    if (option.price > 0){
      let label_price_part = document.createElement("div");
      input_label.appendChild(label_price_part);
      let label_price = document.createElement("span");
      label_price.innerHTML = "$" + option.price;
      label_price_part.appendChild(label_price);
      input_checkbox.addEventListener('change', function() {
        if(this.checked) {
          dish_price = dish_price + option.price;
        } else {
          dish_price = dish_price - option.price;
        }
        total_price = parseInt(dish_quantity.value, 10) * dish_price;
        total_price_tag.innerHTML = total_price;
      }, false);
    }


  }

  dish_quantity.addEventListener('change', function(){
    total_price = parseInt(dish_quantity.value, 10) * dish_price;
    total_price_tag.innerHTML = total_price.toFixed(2);
  }, false);

  minus_dish_button.addEventListener('click', function(){
    if (parseInt(dish_quantity.value, 10) > 1){
      dish_quantity.value = parseInt(dish_quantity.value, 10) - 1;
      total_price = parseInt(dish_quantity.value, 10) * dish_price;
      total_price_tag.innerHTML = total_price.toFixed(2);
    }
  }, false);

  plus_dish_button.addEventListener('click', function(){
    dish_quantity.value = parseInt(dish_quantity.value, 10) + 1;
    total_price = parseInt(dish_quantity.value, 10) * dish_price;
    total_price_tag.innerHTML = total_price.toFixed(2);
  }, false);

  submit_button.addEventListener('click', function(e){
          e.preventDefault();
          let order_data = {};
          let options = "";
          let elements = content_holder.getElementsByTagName("input");
          for (let i = 0; i < elements.length; i++) {
                if (elements[i].checked) {
                  options = options + " " + elements[a].value;
                }
          }
          order_data['name'] = dish_name.innerHTML;
          order_data['quantity'] = dish_quantity.value.toString();
          order_data['price'] = total_price_tag.innerHTML;
          order_data['options'] = options;
          addOrder("./order/", JSON.stringify(order_data));
  }, false);

}

function addOrder(url, order_data) {
  /*
  TODO:
  check the data if JSONfied
  */
  var request = new Request(url, {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify(order_data),
              });
  return fetch(request).then((response) => {
    if (response.status === 200) { // OK
      return [];
    } else {
      alert("Something went wrong: " + response.status);
    }
  });
}


function display_dishes_by_kind(data){
  var kind_name = "";
  var section = "";

  for (let i=0; i < data.length; i++){

    if (data[i].kind.name !== kind_name){
      kind_name = data[i].kind.name;
      appendKind(kind_name);
      // group dishes in sections by kind
      section = document.createElement("div");
      section.setAttribute("class", "row");
      section.id = "kind_" + kind_name;
      dishes_holder.appendChild(section);
      // header for the section
      let header_holder = document.createElement("div");
      header_holder.style = "flex-basis:100%;";
      section.appendChild(header_holder);
      let header = document.createElement("h1");
      header.setAttribute("class", "h3 mb-3 text-gray-800");
      header.innerHTML = kind_name;
      header_holder.appendChild(header);
    }

    // dish for the section
    let dish_holder = document.createElement("div");
    dish_holder.setAttribute("class", "col-md-5 mr-4 mb-4");
    section.appendChild(dish_holder);
    let inner_holder = document.createElement("div");
    inner_holder.setAttribute("class", "card shadow");
    dish_holder.appendChild(inner_holder);
    let dish_link = document.createElement("button");
    dish_link.setAttribute("class", "btn");
    dish_link.onclick = function() {get_dish_info(data[i].id)};
    inner_holder.appendChild(dish_link);
    let content_holder = document.createElement("div");
    content_holder.setAttribute("class", "card-body no-gutters align-items-center");
    dish_link.appendChild(content_holder);
    // dish image
    let image_holder = document.createElement("div");
    content_holder.appendChild(image_holder);
    let image = document.createElement("img");
    image.setAttribute("class", "card-img");
    if (data[i].picture){
      image.src = data[i].picture;
    } else {
      image.src = '../static/Manager/images/defaultimage.jpg/';
    }
    image_holder.appendChild(image);
    // dish name and price
    let text_holder = document.createElement("div");
    content_holder.appendChild(text_holder);
    let dish_header = document.createElement("h6");
    dish_header.setAttribute("class", "mt-3 font-weight-bold text-primary");
    dish_header.innerHTML = data[i].name;
    text_holder.appendChild(dish_header);
    let dish_price = document.createElement("div");
    dish_price.setAttribute("class", "h5 mb-2 mt-2 font-weight-bold text-gray-800");
    dish_price.innerHTML = "$" + data[i].price;
    text_holder.appendChild(dish_price);
  }

}

/*
  add kind to category sidebar
*/
function appendKind(kind_name){
  let kind = document.createElement("li");
  kind.setAttribute("class", "nav-item active");
  kind_holder.appendChild(kind);
  let kind_link = document.createElement("a");
  kind_link.setAttribute("class", "nav-link");
  kind_link.href = "#kind_" + kind_name;
  kind.appendChild(kind_link);
  let kind_span = document.createElement("span");
  kind_span.innerHTML = kind_name;
  kind_link.appendChild(kind_span);
}

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
