*** Settings ***
Documentation     A test suite with a single test for removing an item from the cart.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot

*** Test Cases ***

Add One Item to Cart
	Open Inventory Page

	Add Item To Cart

	Has Items In Cart
	Element Text Should Be  class:shopping_cart_badge  1
	[Teardown]  End Session

Add Two Items to Cart
	Open Inventory Page

	Add Item To Cart
	Add Item To Cart

	Element Text Should Be  class:shopping_cart_badge  2
	[Teardown]  End Session