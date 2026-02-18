from playwright.sync_api import sync_playwright

# with sync_playwright() as playwright:


def test_home(page):
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # page = browser.new_page()
    page.goto("https://carlosng07.vercel.app/")
    print(page.title())
    # page.get_by_role("link", name="Get started").click()
    projects_button = page.get_by_role("link", name="Projects")
    projects_button.click()
    print("Projects:", page.url)
