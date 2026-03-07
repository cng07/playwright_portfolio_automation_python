from pages.HomePage import HomePage
from pages.ResumePage import ResumePage


def test_verify_resume_page_ui_via_navigation(page):
    home_page = HomePage(page)
    resume_page = ResumePage(page)

    home_page.go_to_home_page()
    resume_page.go_to_resume_page()
    resume_page.verify_all_resume_page_elements()


def test_verify_resume_pdf_download(page):
    resume_page = ResumePage(page)

    resume_page.go_to_resume_page_direct()
    resume_page.verify_download_pdf_button()
    resume_page.download_pdf_and_verify()


def test_verify_resume_page_api_links(page):
    resume_page = ResumePage(page)

    resume_page.go_to_resume_page_direct()
    resume_page.verify_all_resume_api_checks()
