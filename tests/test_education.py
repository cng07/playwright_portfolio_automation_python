from pages.EducationPage import EducationPage
from pages.HomePage import HomePage


def test_verify_education_page_ui_via_navigation(page):
    home_page = HomePage(page)
    education_page = EducationPage(page)

    home_page.go_to_home_page()
    education_page.go_to_education_page()
    education_page.verify_all_education_page_elements()


def test_verify_education_page_ui_via_direct_url(page):
    education_page = EducationPage(page)

    education_page.go_to_education_page_direct()
    education_page.verify_all_education_page_elements()


def test_verify_education_page_api_links(page):
    education_page = EducationPage(page)

    education_page.go_to_education_page_direct()
    education_page.verify_all_education_api_checks()
