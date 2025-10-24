from config.config_reader import product2_name, product1_name


def test_view_products_page(products_page):
    assert products_page.is_displayed()


def test_products_list(products_page):
    count = products_page.product_list_is_displayed()
    assert count > 0 , "No products are listed"

    products = products_page.get_product_names()
    for item in products:
        print(f"Product : {item}\n")


def test_sort_products_descending(products_page):
    products_page.sort_name_z_to_a()
    products = products_page.get_product_names()
    print("The sorted product list")
    for item in products:
        print(f"Product : {item}\n")
    assert products == sorted(products, reverse=True), "Products are not sorted in descending order"

def test_add_to_cart(products_page, cart_page):
    products_page.add_to_cart_list_page(product1_name())
    assert "1" in cart_page.items_in_cart_badge()

def test_click_on_product2(products_page, product_details_page):
    products_page.click_on_product(product2_name())
    assert product2_name() in product_details_page.name_check()

def test_add_to_cart_from_details(products_page, product_details_page):
    products_page.click_on_product(product2_name())
    product_details_page.add_to_cart_details_page()
    assert "Remove" in product_details_page.remove_button_present()
