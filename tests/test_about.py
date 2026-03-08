from pages.AboutPage import AboutPage
from pages.HomePage import HomePage


def test_verify_about_page_ui_via_navigation(page):
    home_page = HomePage(page)
    about_page = AboutPage(page)

    home_page.go_to_home_page()
    about_page.go_to_about_page()
    about_page.verify_all_about_page_elements()


def test_verify_about_page_ui_via_direct_url(page):
    about_page = AboutPage(page)

    about_page.go_to_about_page_direct()
    about_page.verify_all_about_page_elements()


def test_verify_about_page_api_links(page):
    about_page = AboutPage(page)

    about_page.go_to_about_page_direct()
    about_page.verify_internal_links_api_responses()
