from pages.HomePage import HomePage
from pages.CertificationsPage import CertificationsPage


def test_verify_certifications_page_via_navigation_menu(page):
    certifications_page = CertificationsPage(page)
    home_page = HomePage(page)

    home_page.go_to_home_page()
    certifications_page.go_to_certifications_page_from_home_navigation()
    certifications_page.verify_certifications_page_header()
    certifications_page.verify_ctfl_certification()
    certifications_page.verify_devops_certification()
    certifications_page.verify_accenture_agile_certification()
    certifications_page.verify_automation_anywhere_certification()
    certifications_page.verify_certification_links()


def test_verify_certifications_page_via_direct_url(page):
    certifications_page = CertificationsPage(page)

    certifications_page.go_to_certifications_page()
    certifications_page.verify_certifications_page_header()
    certifications_page.verify_ctfl_certification()
    certifications_page.verify_devops_certification()
    certifications_page.verify_accenture_agile_certification()
    certifications_page.verify_automation_anywhere_certification()
    certifications_page.verify_certification_links()
