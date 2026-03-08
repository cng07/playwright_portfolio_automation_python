import re

from playwright.sync_api import Page, expect

from pages.Helper import Helper


class CertificationsPage:
    BASE_URL = "https://carlosng07.vercel.app"

    def __init__(self, page: Page):
        self.page = page
        self.h = Helper(page)

        self.nav_more = page.get_by_role("button", name="More")
        self.nav_certifications_link = page.get_by_role("menuitem", name="Certifications")

        self.certifications_heading = page.get_by_role("heading", name="Certifications", level=1)

        self.ctfl_heading = page.get_by_role("heading", name="ISTQB Certified Tester Foundation Level (CTFL)", level=2)
        self.devops_heading = page.get_by_role("heading", name="Certified Tester, AT*SQA DevOps Testing", level=2)
        self.accenture_agile_heading = page.get_by_role("heading", name="Accenture Agile Certification Program", level=2)
        self.automation_anywhere_heading = page.get_by_role(
            "heading", name="Automation Anywhere Certified Advanced RPA Professional", level=2
        )

        self.ctfl_date = page.get_by_text("April 2024", exact=True)
        self.ctfl_expiry = page.get_by_text("No Expiry", exact=True).nth(0)
        self.ctfl_issuer = page.get_by_text("ASTQB - ISTQB in the U.S.", exact=True).nth(0)
        self.ctfl_credential_id_label = page.get_by_text("Credential ID:", exact=True).nth(0)
        self.ctfl_credential_id_value = page.get_by_text("24-CTFL-01347-USA", exact=True)

        self.devops_date = page.get_by_text("January 2023").first
        self.devops_expiry = page.get_by_text("Expired", exact=True).nth(0)
        self.devops_issuer = page.get_by_text("ASTQB - ISTQB in the U.S.", exact=True).nth(1)
        self.devops_credential_id_label = page.get_by_text("Credential ID:", exact=True).nth(1)
        self.devops_credential_id_value = page.get_by_text("23-AT*DevOps-00002-USA", exact=True)

        self.accenture_subheading = page.get_by_text("Agile Professional Certified", exact=True)
        self.accenture_date = page.get_by_text("June 2020", exact=True)
        self.accenture_expiry = page.get_by_text("No Expiry", exact=True).nth(1)
        self.accenture_issuer = page.get_by_text("Accenture", exact=True)
        self.accenture_certificate_number_label = page.get_by_text("Certificate Number:", exact=True).nth(0)
        self.accenture_certificate_number_value = page.get_by_text("CNAG0000009961", exact=True)

        self.automation_anywhere_subheading = page.get_by_text(
            "Robotic Process Automation Professional (V11.0)", exact=True
        )
        self.automation_anywhere_date = page.get_by_text("July 2020").first
        self.automation_anywhere_expiry = page.get_by_text("Expired", exact=True).nth(1)
        self.automation_anywhere_issuer = page.get_by_text("Automation Anywhere", exact=True)
        self.automation_anywhere_certificate_number_label = page.get_by_text("Certificate Number:", exact=True).nth(1)
        self.automation_anywhere_certificate_number_value = page.get_by_text("AAADVC-21147163", exact=True)

        self.official_profile_link = page.get_by_role(
            "link", name="Official U.S. List of Certified & Credentialed Software Testers"
        )
        self.view_certificate_links = page.locator('a:has-text("View Certificate")')

    def go_to_certifications_page(self) -> None:
        self.page.goto(f"{self.BASE_URL}/certifications")
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_title("Carlos Ng | Certifications")

    def go_to_certifications_page_from_home_navigation(self) -> None:
        expect(self.nav_more).to_be_visible()
        self.nav_more.click()
        expect(self.nav_certifications_link).to_be_visible()
        self.nav_certifications_link.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(r".*/certifications$"))
        expect(self.page).to_have_title("Carlos Ng | Certifications")

    def verify_certifications_page_header(self) -> None:
        expect(self.certifications_heading).to_be_visible()

    def verify_ctfl_certification(self) -> None:
        expect(self.ctfl_heading).to_be_visible()
        expect(self.ctfl_date).to_be_visible()
        expect(self.ctfl_expiry).to_be_visible()
        expect(self.ctfl_issuer).to_be_visible()
        expect(self.ctfl_credential_id_label).to_be_visible()
        expect(self.ctfl_credential_id_value).to_be_visible()

    def verify_devops_certification(self) -> None:
        expect(self.devops_heading).to_be_visible()
        expect(self.devops_date).to_be_visible()
        expect(self.devops_expiry).to_be_visible()
        expect(self.devops_issuer).to_be_visible()
        expect(self.devops_credential_id_label).to_be_visible()
        expect(self.devops_credential_id_value).to_be_visible()

    def verify_accenture_agile_certification(self) -> None:
        expect(self.accenture_agile_heading).to_be_visible()
        expect(self.accenture_subheading).to_be_visible()
        expect(self.accenture_date).to_be_visible()
        expect(self.accenture_expiry).to_be_visible()
        expect(self.accenture_issuer).to_be_visible()
        expect(self.accenture_certificate_number_label).to_be_visible()
        expect(self.accenture_certificate_number_value).to_be_visible()

    def verify_automation_anywhere_certification(self) -> None:
        expect(self.automation_anywhere_heading).to_be_visible()
        expect(self.automation_anywhere_subheading).to_be_visible()
        expect(self.automation_anywhere_date).to_be_visible()
        expect(self.automation_anywhere_expiry).to_be_visible()
        expect(self.automation_anywhere_issuer).to_be_visible()
        expect(self.automation_anywhere_certificate_number_label).to_be_visible()
        expect(self.automation_anywhere_certificate_number_value).to_be_visible()

    def verify_certification_links(self) -> None:
        expect(self.official_profile_link).to_be_visible()
        expect(self.view_certificate_links).to_have_count(4)

    def verify_all_certifications_page_elements(self) -> None:
        self.verify_certifications_page_header()
        self.verify_ctfl_certification()
        self.verify_devops_certification()
        self.verify_accenture_agile_certification()
        self.verify_automation_anywhere_certification()
        self.verify_certification_links()
