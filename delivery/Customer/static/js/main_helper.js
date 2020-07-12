function cart_close() {
  var cart_info = document.getElementById("shopping_cart");

  cart_info.style.display = "none";
}

function store_info_onclick() {
  var store_info = document.getElementById("store_info");
    store_info.style.display = "block";
  var body = document.getElementById("page-top");
  body.classList.add("modal-open");
}

function cart_onclick() {
  var cart_info = document.getElementById("shopping_cart");

  if (cart_info.style.display === "none") {
    cart_info.style.display = "block";
  }
}

function store_info_close() {
  var store_info = document.getElementById("store_info");

  store_info.style.display = "none";
  var body = document.getElementById("page-top");
  body.classList.remove("modal-open");
}

function dish_info() {
  var dish_info = document.getElementById("dish_info");
    dish_info.style.display = "block";
  var body = document.getElementById("page-top");
  body.classList.add("modal-open");
}

function dish_info_close() {
  var dish_info = document.getElementById("dish_info");

  dish_info.style.display = "none";
  var body = document.getElementById("page-top");
  body.classList.remove("modal-open");
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
