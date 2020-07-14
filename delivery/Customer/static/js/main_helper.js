var cart_info = document.getElementById("shopping_cart");
var store_info = document.getElementById("store_info");
var dish_info = document.getElementById("dish_info");

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

function dish_info() {
  dish_info.style.display = "block";
  body.classList.add("modal-open");
  display_dish_info(dishurl);
}

function dish_info_close() {
  dish_info.style.display = "none";
  body.classList.remove("modal-open");
}

function display_dish_info(url){
  var data = fetchJSON(url);

}

function display_dishes(url){
  var data = fetchJSON(url);
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
