const foreign_key_input = document.getElementById("foreign_key_input");
const foreign_key_select = document.getElementById("foreign_key_select");
const crf_sales = document.getElementsByName("csrfmiddlewaretoken")[0].value;
const product_name_input = document.getElementById("product_name");
const  product_purchase_price = document.getElementById('id_purchase_price')
const product_code_input = document.getElementById("product_code");
const product_price_input = document.getElementById("product_price")
const results_box_single_sale = document.getElementById(
  "results-box-single-sale"
);
console.log(product_purchase_price);

function product_search_clicked(product) {
  e = window.event;
  e.preventDefault();
  results_box_single_sale.innerHTML = "";
  $.ajax({
    type: "GET",
    url: `/get_product_by_uuid/${product}`,
    success: (response) => {
      if (response) {
        const product_name = response.product_name;
        const sales_price = response.sales_price;
        const purchase_price = response.purchase_price
        const quantity = 1;
        const product_uuid = response.product_uuid;
        const product = {
          product_name,
          sales_price,
          quantity,
          product_uuid,
          purchase_price
        };
        console.log(product);
        product_name_input.value = product_name;
        product_code_input.value = product_uuid;
        // product_purchase_price.value = purchase_price;
        product_price_input.value = sales_price;


      }
      console.log(product_purchase_price.value)
    },
  });
}

const send_search_product_sales = async (product) => {
  const input = product;

  $.ajax({
    url: "/product_search",
    type: "POST",
    data: {
      csrfmiddlewaretoken: crf_sales,
      product: input,
    },
    success: (response) => {
      if (Array.isArray(response.data)) {
        results_box_single_sale.innerHTML = "";
        response.data.forEach((product) => {
          results_box_single_sale.innerHTML += `<a href="" class="list-group-item list-group-item-action" onclick="product_search_clicked('${product.code}')">
        <div class="d-flex  mt-2 mb-2">
        
          <div class="mr-2">
              <h5 class="product-name">${product.code}</h5>

          </div>
          <div class="mr-2">
              <h5 class="product-name">${product.name}</h5>
             
          </div>
         

        </div>
        </a>`;
        });
      }
      // response.data.forEach((product) => {
      //   //   const option = document.createElement("option");
      //   //   option.value = product.id;
      //   //   option.innerHTML = product.name;
      //   //   foreign_key_select.appendChild(option);
      //   console.log(product);
      // });
    },

    error: (error) => {
      console.log(error);
    },
  });
};
foreign_key_input.addEventListener("keyup", function (event) {
  event.preventDefault();
  console.log(event.target.value);

  if (event.target.value.length > 0) {
    send_search_product_sales(event.target.value);
  } else {
    results_box_single_sale.innerHTML = "";
  }
});
