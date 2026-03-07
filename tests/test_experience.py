from pages.ExperiencePage import ExperiencePage
from pages.HomePage import HomePage


def test_verify_experience_page_ui_via_navigation(page):
    home_page = HomePage(page)
    experience_page = ExperiencePage(page)

    home_page.go_to_home_page()
    experience_page.go_to_experience_page()
    experience_page.verify_all_experience_page_elements()


def test_verify_experience_page_ui_via_direct_url(page):
    experience_page = ExperiencePage(page)

    experience_page.go_to_experience_page_direct()
    experience_page.verify_all_experience_page_elements()


def test_verify_experience_page_api_links(page):
    experience_page = ExperiencePage(page)

    experience_page.go_to_experience_page_direct()
    experience_page.verify_all_experience_api_checks()
