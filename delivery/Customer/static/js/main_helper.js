var cart_info = document.getElementById("shopping_cart");
var store_info = document.getElementById("store_info");
var dish_info = document.getElementById("dish_info");
var dishes_holder = document.getElementById("dishes_holder");
var kind_holder = document.getElementById("category_content");

var body = document.getElementById("page-top");

function cart_close() {
  cart_info.style.display = "none";
}

function store_info_onclick() {
  store_info.style.display = "block";
  body.classList.add("modal-open");
}

function cart_onclick() {

  if (cart_info.style.display === "none") {
    cart_info.style.display = "block";
  }
}

function store_info_close() {

  store_info.style.display = "none";
  body.classList.remove("modal-open");
}

function dish_info(id) {
  dish_info.style.display = "block";
  body.classList.add("modal-open");
  let dishurl = "{% url 'menu_dish' 123 %}".replace(/123/, id);
  display_dish_info(dishurl);
}

function dish_info_close() {
  dish_info.style.display = "none";
  body.classList.remove("modal-open");
}

function display_dish_info(url){
  var data = fetchJSON(url);

}

function display_dishes_by_kind(data){

  for (var i=0; i < data.length; i++){
    // category sidebar
    let kind = document.creatElement("li");
    kind.class = "nav-item active";
    kind_holder.appendChild(kind);
    let kind_link = document.createElement("a");
    kind_link.class = "nav-link";
    kind_link.href = "#kind" + i.toString();
    kind.appendChild(kind_link);
    let kind_span = document.creatElement("span");
    kind_span.innerHTML = data[i].name;
    kind_link.appendChild(kind_span);


    // group dishes in sections by kind
    let section = document.creatElement("div");
    section.class = "row";
    section.id = "kind" + i.toString();
    dishes_holder.appendChild(section);
    // header for the section
    let header_holder = document.creatElement("div");
    header_holder.style = "flex-basis:100%;";
    section.appendChild(header_holder);
    let header = document.creatElement("h1");
    header.class = "h3 mb-3 text-gray-800";
    header.innerHTML = data[i].name;
    header_holder.appendChild(header);
    // dishes for the section
    for (var j=0; j < data[i].dishes.length; j++){
      let dish = data[i].dishes[j];
      let dish_holder = document.creatElement("div");
      dish_holder.class = "col-xl-3 col-md-6 mb-4";
      section.appendChild(dish_holder);
      let inner_holder = document.creatElement("div");
      inner_holder.class = "card shadow";
      dish_holder.appendChild(inner_holder);
      let dish_link = document.creatElement("button");
      dish_link.class = "btn";
      dish_link.onclick = function() {dish_info(dish.id)};
      inner_holder.appendChild(dish_link);
      let content_holder = document.creatElement("div");
      content_holder.class = "card-body row no-gutters align-items-center";
      inner_holder.appendChild(content_holder);
      // dish image
      let image_holder = document.creatElement("div");
      image_holder.class = "col-md-10 mr-2";
      content_holder.appendChild(image_holder);
      let image = document.creatElement("img");
      image.class = "dropdown-list-image col-md-12";
      image.src = dish.picture;
      image_holder.appendChild(image);
      // dish name and price
      let text_holder = document.creatElement("div");
      text_holder.class = "col-6 mr-2";
      content_holder.appendChild(text_holder);
      let dish_header = document.creatElement("h6");
      dish_header.class = "mt-3 font-weight-bold text-primary";
      dish_header.innerHTML = dish.name;
      text_holder.appendChild(dish_header);
      let dish_price = document.creatElement("div");
      dish_price.class = "h5 mb-2 mt-2 font-weight-bold text-gray-800";
      dish_price.innerHTML = "$" + dish.price.toString();
      text_holder.appendChild(dish_price);
    }
  }

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
/*
https://stackoverflow.com/questions/56449599/how-to-get-input-from-dynamically-created-checkboxes-and-radio-buttons-in-javasc
function radiobutton(d) {
  var output = "";

  for (var i = 0; i < d.length; i++) {
    output += '<input type="radio" value="' + d[i] + '" name="box2">' + d[i] +  '<br><br>';

  }
  return output;
}

function check() {
  var elements = document.getElementsByTagName("input");
  for (var a = 0; a < elements.length; a++) {
        if (elements[a].checked) {
          console.log(elements[a].value + " is checked");
        }
  }
}
*/
