from config.config_reader import product1_name, product2_name


def test_checkout(cart_page, checkout_page, products_page):
    products_page.add_to_cart_list_page(product1_name())
    assert cart_page.items_in_cart_badge() == "1"

    products_page.add_to_cart_list_page(product2_name())
    assert cart_page.items_in_cart_badge() == "2"

    cart_page.click_on_cart()
    assert "Your Cart" in cart_page.cart_page_title()

    checkout_page.checkout()
    assert checkout_page.checkout_page_title() == "Checkout: Your Information"

    checkout_page.fill_checkout_form()
    assert "Checkout: Overview" in checkout_page.checkout_page_title()
    assert checkout_page.price_summary_displayed()

    checkout_page.click_finish()
    assert checkout_page.checkout_page_title() == "Checkout: Complete!"

def test_logout(checkout_page):
    checkout_page.click_burger_menu()
    checkout_page.logout()