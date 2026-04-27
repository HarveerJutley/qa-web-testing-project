from playwright.sync_api import sync_playwright

def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")

        page.fill("#user-name", "wrong_user")
        page.fill("#password", "wrong_pass")
        page.click("#login-button")

        assert page.locator(".error-message").is_visible()
        

        browser.close()