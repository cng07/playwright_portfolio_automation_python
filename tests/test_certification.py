from playwright.sync_api import sync_playwright
from pages.CertificationsPage import CertificationsPage
from pages.HomePage import HomePage


def test_certifications_page(page):
    certifications_page = CertificationsPage(page)
    home_page = HomePage(page)

    home_page.navigate()
    print(page.title())
    certifications_page.click_certifications()
    print("Certifications:", page.url)
    certifications_page.verifyCertification1()
    certifications_page.verifyCertification2()
    certifications_page.verifyCertification3()
    certifications_page.verifyCertification4()
