from config.config_reader import valid_creds, invalid_creds

def test_invalid_login(login_page):
    login_page.login(invalid_creds())
    assert "do not match any user" in login_page.get_error_message()

def test_valid_login(login_page):
    login_page.login(valid_creds())
    assert login_page.get_page_title() == "Products", "Products page is not displayed"




