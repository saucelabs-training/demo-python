*** Settings ***
Documentation     A test suite with a single test for removing an item from the cart.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot


*** Test Cases ***

Remove One Item From Cart
	Open Inventory Page

	Add Item To Cart
	Add Item To Cart

	Remove Item From Cart

	Has Items In Cart
	Element Text Should Be  class:shopping_cart_badge  1
	[Teardown]  End Session