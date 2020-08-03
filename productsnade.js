var faker = require('faker');

//var randomproductName = faker.commerce.productName();
//var randomprice = faker.commerce.price();

console.log("================ \n Welcome to My Shop \n ================ \n");
for (i = 0; i < 5; i++) {
  console.log(faker.commerce.productName() + "-$" + faker.commerce.price());
	
}
