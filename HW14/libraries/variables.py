### Main page before login ###
LOGIN_BUTTON = "id:login2"
LOGIN_POPUP = "id:logInModalLabel"
USERNAME_INPUT_FIELD = "id:loginusername"
PASSWORD_INPUT_FIELD = "id:loginpassword"
LOGIN_BUTTON_IN_LOGIN_POPUP = "css:div[id='logInModal'] button[class='btn btn-primary']"

### Main page after login ###
LOGOUT_BUTTON = "id:logout2"
WELCOME_MESSAGE_TEST = "id:nameofuser"
MONITORS_BUTTON = "//a[text()='Monitors']"
CART_BUTTON = "id:cartur"

### Monitors content ###
ALL_MONITORS = "//div[@id='tbodyid']//div[@class='col-lg-4 col-md-6 mb-4']"
PRODUCT_PRICE = "//h5"
PRODUCT_NAME = "//a[@class='hrefch']"

### Product page ###
PRODUCT_CONTENT = "//div[@class='product-content product-wrap clearfix product-deatil']"
PRODUCT_NAME_ON_PRODUCT_PAGE = "css:h2[class='name']"
PRODUCT_PRICE_ON_PRODUCT_PAGE = "css:h3[class='price-container']"
ADD_TO_CARD_BUTTON = "xpath://a[text()='Add to cart']"

### Cart page ###
PLACE_ORDER_BUTTON = "xpath://button[@type='button' and text()='Place Order']"
TABLE_WITH_PRODUCTS = "id:tbodyid"
PRODUCT_NAME_IN_CART = "xpath://tbody[@id='tbodyid']//td[2]"
PRODUCT_PRICE_IN_CART = "xpath://tbody[@id='tbodyid']//td[3]"