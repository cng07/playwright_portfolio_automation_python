from pages.ContactPage import ContactPage
from pages.HomePage import HomePage


def test_verify_contact_page_ui_via_navigation(page):
    home_page = HomePage(page)
    contact_page = ContactPage(page)

    home_page.go_to_home_page()
    contact_page.go_to_contact_page()
    contact_page.verify_all_contact_page_elements()


def test_verify_contact_page_ui_via_direct_url(page):
    contact_page = ContactPage(page)

    contact_page.go_to_contact_page_direct()
    contact_page.verify_all_contact_page_elements()


def test_verify_contact_page_api_links(page):
    contact_page = ContactPage(page)

    contact_page.go_to_contact_page_direct()
    contact_page.verify_all_contact_api_checks()
