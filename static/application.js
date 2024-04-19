//! varible declaration
var search_product_uuid = document.getElementById("search_product_uuid");
var search_product_by_name = document.getElementById("search_product_by_name");
const crf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
const resultsBox = document.getElementById("results-box");
const product__table = document.getElementById("product__table");
const delete_product_btn = document.getElementById("delete_product_btn");
const submit_product = document.getElementById("submit__product");
const clear__cart = document.getElementById("clear__cart");
const add_sales_link = document.getElementById("add_sales_link");
const current_total_price = document.getElementById("current_total_price");
const amount_received = document.getElementById("amount_received");
const close_my_popup = document.getElementById("close_my_popup");
// const product_popup_purchase = document.getElementById(
//   "product_popup_purchase"
// );

// Set up variables to track the start and end of the barcode input
let barcodeStart = false;
let barcodeData = "";

// close_my_popup.addEventListener("click", function (event) {
//   event.preventDefault();

//   product_popup_purchase.style.display = "none";
// });

// Listen for keyboard input events on the whole page
window.addEventListener("keydown", (event) => {
  // Check if the input event is coming from the barcode scanner
  if (event.code === "BarcodeScanner" || event.code === "Enter") {
    // Set the barcode start flag to true
    barcodeStart = true;
  }
  // Check if the barcode start flag is true and the input event is not the enter key
  else if (barcodeStart && event.code !== "Enter") {
    // Append the input event value to the barcode data

    barcodeData += event.key;
  }
});

// Listen for key up events to check if the barcode input is complete
window.addEventListener("keyup", (event) => {
  // Check if the input event is the enter key
  if (event.code === "Enter") {
    // Push the barcode data to the input field

    document.getElementById("search_product_uuid").focus();

    // Reset the barcode start flag and barcode data variables
    barcodeStart = false;
    barcodeData = "";
  }
});

window.onload = function () {
  document.getElementById("search_product_uuid").focus();
};
add_sales_link.addEventListener("click", function (event) {
  event.preventDefault();
  console.log("likde");
  window.location.href = "/add_sales?#";
});

clear__cart.addEventListener("click", function (event) {
  event.preventDefault();
  /// reload the page after clearing the cart
  localStorage.removeItem("cart");
  update_product_table();
  window.location.reload();
});

// geting to price of products in the cart
function get_total_price() {
  const cart = JSON.parse(localStorage.getItem("cart")) || {};
  let total_price = 0;
  for (const product_uuid in cart) {
    const product = cart[product_uuid];
    const discount = product.discount;
    if (discount > 0) {
      total_price += product.total_price;
    } else {
      total_price += product.total_price;
    }
  }

  // convert to total price to string and comma separated
  total_price = total_price.toLocaleString();
  // set to the  current total price with a new value

  current_total_price.innerHTML = total_price;
  return total_price;
}
amount_received.addEventListener("keyup", function (event) {
  const input = event.target;
  event.preventDefault();
  // Remove non-numeric characters
  let value = input.value.replace(/\D/g, "");

  // Convert to number and format with commas
  value = Number(value).toLocaleString();

  // Update the input value
  input.value = value;
});
amount_received.addEventListener("blur", function (event) {
  event.preventDefault();
  const amount_received = document.getElementById("amount_received").value;
  // remove the comma from the amount received
  const amount_received_without_comma = amount_received.replace(/,/g, "");
  // convert the amount received to number
  const amount_received_number = Number(amount_received_without_comma);
  const total_price = get_total_price();
  //remove the comma from the total price
  const total_price_without_comma = total_price.replace(/,/g, "");
  // convert the total price to number
  const total_price_number = Number(total_price_without_comma);
  const change = amount_received_number - total_price_number;
  const change_with_comma = change.toLocaleString();
  document.getElementById("current_change").innerHTML = change_with_comma;
});

const send_search_product = async (product) => {
  $.ajax({
    type: "POST",
    url: "/product_search",
    data: {
      csrfmiddlewaretoken: crf,
      product: product,
    },
    success: (response) => {
      if (Array.isArray(response.data)) {
        resultsBox.innerHTML = "";
        response.data.forEach((product) => {
          resultsBox.innerHTML += `<a href="" class="list-group-item list-group-item-action" onclick="send_search_product_uuid_from_popup('${product.code}')">
          <div class="d-flex  mt-2 mb-2">
          
            <div class="mr-2">
                <h5 class="product-name">${product.code}</h5>

            </div>
            <div class="mr-2">
                <h5 class="product-name">${product.name}</h5>
               
            </div>
            <div class="mr-2">
                <h5 class="product-name">${product.price}</h5>
               
            </div>
            <div class="mr-2">
                <h5 class="product-name">${product.description}</h5>
               
            </div>

          </div>
          </a>`;
        });
      } else {
        if (searchInput.value.length > 0) {
          resultsBox.innerHTML = `<b>${response.data}</b>`;
        } else {
          resultsBox.innerHTML = "";
        }
      }
    },
    error: (error) => {
      console.log(error);
    },
  });
};

// ! PRODUCT SEARCH INPUT keyup event
search_product_by_name.addEventListener("keyup", function (event) {
  console.log(event.target.value);

  if (event.target.value.length > 0) {
    send_search_product(event.target.value);
  } else {
    resultsBox.innerHTML = "";
  }
});

//! update the product table
function update_product_table() {
  // Get the cart items from local storage
  const cart = JSON.parse(localStorage.getItem("cart")) || {};

  // Clear the table contents
  product__table.innerHTML = "";
  console.log("update product table");
  console.log(cart);
  // Loop through each item in the cart and add it to the table
  for (const product_uuid in cart) {
    const product = cart[product_uuid];
    // ! Show the product table
    const product_table = document.getElementById("product__table");
    //  create table header
    const product_table_header = document.createElement("thead");
    product_table_header.innerHTML = `<thead>
    <tr>
      <th scope="col">Product Name</th>
      <th scope="col">Quantity</th>
      <th scope="col">Price</th>
      <th scope="col">Total Price</th>
      <th scope="col">Discount</th>
      <th scope="col">Action</th>

    </tr>
  </thead>
  `;
    // ! create a row for the product
    const product_row = document.createElement("tr");

    // const product__table_body = document.getElementById('product__table_body')
    // console.log(product__table_body)
    // //! create a row for the product
    // var product_row = document.createElement("tr");
    // // product_row.innerHTML = ` <td>${count}</td>`;
    product_row.innerHTML += ` <td>${product.product_name}</td>`;
    product_row.innerHTML += ` <td> <input type="text" value="${product.quantity}" onblur="update_product_quantity('${product_uuid}')" id="product_quantity_input_${product_uuid}" class="form-control" placeholder="Enter the quantity" /> </td>`;
    product_row.innerHTML += ` <td> <input type="text" value="${product.sales_price}" id="product_price_input" class="form-control" placeholder="Enter the price" disabled /> </td>`;
    product_row.innerHTML += ` <td> <input type="text" value="${product.total_price}" id="product_total_price_input" class="form-control" placeholder="Enter the price" disabled /> </td>`;
    product_row.innerHTML += ` <td>  <input type="text" value="${product.discount}" onblur="update_product_price('${product_uuid}')" id='product_discount_input_${product_uuid}' class="form-control" placeholder="Enter the discount" /> </td>`;
    product_row.innerHTML += ` <td> <button class="btn btn-danger" id="delete_product_btn" onclick="delete_product('${product_uuid}')">Delete</button> </td>`;

    /// include the table header once
    if (product_table.childElementCount == 0) {
      product_table.appendChild(product_table_header);
    }
    product_table.appendChild(product_row);
  }
  submit_product.style.display = "block";
}

//? querying for products
const send_search_product_uuid = async (product) => {
  console.log(product);
  $.ajax({
    type: "GET",
    url: `/get_product_by_uuid/${product}`,
    success: (response) => {
      if (response) {
        const product_name = response.product_name;
        const sales_price = response.sales_price;
        const quantity = 1;
        const product_uuid = response.product_uuid;
        const product = {
          product_name,
          sales_price,
          quantity,
          product_uuid,
        };
        console.log(product);
        // If the product exists, increment its quantity in the cart
        const cart = JSON.parse(localStorage.getItem("cart")) || {};
        if (cart[response.product_uuid]) {
          cart[response.product_uuid].quantity =
            cart[response.product_uuid].quantity + 1;
          // prettier-ignore
          // This code will not be formatted by Prettier
          cart[response.product_uuid].total_price =
          (cart[response.product_uuid].quantity *  cart[response.product_uuid].sales_price) - cart[response.product_uuid].discount;
          localStorage.setItem("cart", JSON.stringify(cart));
          update_product_table();
          get_total_price();
        } else {
          cart[response.product_uuid] = {
            product_name: response.product_name,
            sales_price: response.sales_price,
            old_price: response.sales_price,
            quantity: 1,
            product_uuid: response.product_uuid,
            total_price: response.sales_price * 1,
            discount: 0,
          };
          localStorage.setItem("cart", JSON.stringify(cart));
          update_product_table();
          get_total_price();
        }
        localStorage.setItem("cart", JSON.stringify(cart));
      } else {
        // If the product doesn't exist, show an error message
        alert("Product not found");
      }
    },
    error: (error) => {
      console.log(error);
    },
  });
};

function send_search_product_uuid_from_popup(product) {
  // prevent default form submission

  e = window.event;
  e.preventDefault();

  console.log(product);
  $.ajax({
    type: "GET",
    url: `/get_product_by_uuid/${product}`,
    success: (response) => {
      if (response) {
        const product_name = response.product_name;
        const sales_price = response.sales_price;
        const quantity = 1;
        const product_uuid = response.product_uuid;
        const product = {
          product_name,
          sales_price,
          quantity,
          product_uuid,
        };
        console.log(product);
        // If the product exists, increment its quantity in the cart
        const cart = JSON.parse(localStorage.getItem("cart")) || {};
        if (cart[response.product_uuid]) {
          cart[response.product_uuid].quantity++;
          cart[response.product_uuid].total_price =
            // prettier-ignore
            // This code will not be formatted by Prettier

            (cart[response.product_uuid].quantity *  cart[response.product_uuid].sales_price) - cart[response.product_uuid].discount;
          localStorage.setItem("cart", JSON.stringify(cart));
          update_product_table();
          get_total_price();
        } else {
          cart[response.product_uuid] = {
            product_name: response.product_name,
            sales_price: response.sales_price,
            old_price: response.sales_price,
            quantity: 1,
            product_uuid: response.product_uuid,
            total_price: response.sales_price * 1,
            discount: 0,
          };
          localStorage.setItem("cart", JSON.stringify(cart));
          update_product_table();
          get_total_price();
        }
        localStorage.setItem("cart", JSON.stringify(cart));
      } else {
        // If the product doesn't exist, show an error message
        alert("Product not found");
      }
    },
    error: (error) => {
      console.log(error);
    },
  });

  const product_popup_search = document.getElementById("product_popup_search");

  // <div class="modal fade bd-example-modal-lg show" tabindex="-1" id="product_popup_search" style="display: block;" aria-modal="true" role="dialog">

  // product_popup_search.style.visibility = "hidden";

  update_product_table();
}

search_product_uuid.addEventListener("keyup", function (event) {
  event.preventDefault();
  if (event.key === "Enter") {
    console.log(event.target.value);
    send_search_product_uuid(event.target.value);
    search_product_uuid.value = "";
    update_product_table();
    get_total_price();
  }
  //! set search_product_uuid empty and focus in it
  search_product_uuid.focus;

  // if (event.target.value.length  >= 12) {
  //   //! set search_product_uuid empty and focus in it
  //   send_search_product_uuid(event.target.value);

  //   search_product_uuid.value = "";
  // }
});

document.addEventListener("keydown", function (event) {
  if (event.altKey) {
    document.getElementById("searh_modal_popup").click();
  }
});

console.log("Hello World");

//? Hide the product popup
document.getElementById("close_product_popup").onclick = function () {
  document.getElementById("product_popup").style.display = "none";
  document.getElementById("product_popup").style.visibility = "hidden";
};

function delete_product(product_uuid) {
  const cart = JSON.parse(localStorage.getItem("cart")) || {};
  delete cart[product_uuid];
  localStorage.setItem("cart", JSON.stringify(cart));
  amount_received.value = "";
  current_change.innerHTML = "";
  update_product_table();
  get_total_price();
}

function update_product_price(product_uuid) {
  e = window.event;
  e.preventDefault();
  const cart = JSON.parse(localStorage.getItem("cart")) || {};
  // geting the specific product row from the cart
  const product_price_discount = document.getElementById(
    `product_discount_input_${product_uuid}`
  ).value;

  // check if it is a number
  if (isNaN(product_price_discount)) {
    alert("Please enter a valid number");
  } else {
    cart[product_uuid].discount = product_price_discount;

    // if discount is  is zero then set the sales price to the old price
    if (product_price_discount == 0) {
      cart[product_uuid].sales_price = cart[product_uuid].old_price;
      cart[product_uuid].total_price =
        cart[product_uuid].quantity * cart[product_uuid].sales_price;

      console.log(cart[product_uuid].total_price);
      // set the current total price to the new total price
      const product_total_price_input = document.getElementById(
        "product_total_price_input"
      );
      product_total_price_input.value = cart[product_uuid].total_price;
      localStorage.setItem("cart", JSON.stringify(cart));
      update_product_table();
      get_total_price();
    } else {
      // cart[product_uuid].sales_price =
      //   cart[product_uuid].sales_price - product_price_discount;
      cart[product_uuid].total_price =
        cart[product_uuid].quantity * cart[product_uuid].sales_price -
        product_price_discount;
      // set the current total price to the new total price
      const product_total_price_input = document.getElementById(
        "product_total_price_input"
      );
      product_total_price_input.value = cart[product_uuid].total_price;

      localStorage.setItem("cart", JSON.stringify(cart));
      update_product_table();
      get_total_price();
    }
  }
}

function update_product_quantity(product_uuid) {
  e = window.event;
  e.preventDefault();
  const cart = JSON.parse(localStorage.getItem("cart")) || {};
  const product_quantity = document.getElementById(
    `product_quantity_input_${product_uuid}`
  ).value;

  if (isNaN(product_quantity)) {
    alert("Please enter a valid number");
  } else {
    cart[product_uuid].quantity = product_quantity;
    cart[product_uuid].total_price =
      cart[product_uuid].quantity * cart[product_uuid].sales_price -
      cart[product_uuid].discount;
    localStorage.setItem("cart", JSON.stringify(cart));
    update_product_table();
    get_total_price();
  }
}

function submit__product() {
  e = window.event;
  e.preventDefault();

  // get all the products in the cart
  const cart = JSON.parse(localStorage.getItem("cart"));

  // if no products in the cart then alert the user
  if (cart == null) {
    alert("Please add products to the cart");
  } else {
    $.ajax({
      url: "/complete_sale",
      type: "POST",
      data: {
        csrfmiddlewaretoken: crf,
        cart: JSON.stringify(cart),
      },
      success: function (response) {
        console.log(response);
        if ((response.data = "success")) {
          alert("Sale completed successfully");
          localStorage.removeItem("cart");
          update_product_table();
          window.location.href = "/complete_sale";
        } else {
          alert(response.data);
          console.log(response.data);
        }
      },
    });
  }
}
