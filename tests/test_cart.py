from config.config_reader import product2_name, product1_name


def test_click_on_cart(cart_page):
    cart_page.click_on_cart()
    assert "Your Cart" in cart_page.cart_page_title()

def test_cart_add_and_remove(products_page, cart_page):
    products_page.add_to_cart_list_page(product1_name())
    assert cart_page.items_in_cart_badge() == "1"
    products_page.add_to_cart_list_page(product2_name())
    assert cart_page.items_in_cart_badge() == "2"

    cart_page.click_on_cart()
    assert 2 == cart_page.count_items_in_cart()
    cart_page.remove_item_from_cart(product2_name())
    assert 1 == cart_page.count_items_in_cart()


