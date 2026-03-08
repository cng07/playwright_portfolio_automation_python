import re

from playwright.sync_api import Page, expect

from pages.Helper import Helper


class ContactPage:
    BASE_URL = "https://carlosng07.vercel.app"

    def __init__(self, page: Page):
        self.page = page
        self.h = Helper(page)

        self.skip_to_content_link = page.get_by_role("link", name="Skip to content")
        self.main_content = page.locator("#main-content")

        self.nav_contact_link = page.get_by_role("link", name="Contact")

        self.contact_heading = page.get_by_role("heading", name="Get in Touch", level=1)
        self.contact_subtitle = page.get_by_text(
            "Let's connect to exchange ideas and discuss topics related to software engineering and innovation.",
            exact=True,
        )
        self.email_heading = page.get_by_role("heading", name="Email", level=3)
        self.linkedin_heading = page.get_by_role("heading", name="LinkedIn", level=3)
        self.github_heading = page.get_by_role("heading", name="GitHub", level=3)
        self.ieee_heading = page.get_by_role("heading", name="IEEE Xplore", level=3)
        self.atsqa_heading = page.get_by_role("heading", name="AT*SQA Profile", level=3)

        self.email_link = self.main_content.locator('a[href="mailto:carlosng07@gmail.com"]').first
        self.linkedin_link = self.main_content.locator('a[href="https://www.linkedin.com/in/carlosng07"]').first
        self.github_link = self.main_content.locator('a[href="https://github.com/cng07"]').first
        self.ieee_link = self.main_content.locator('a[href="https://ieeexplore.ieee.org/author/37086553247"]').first
        self.atsqa_link = self.main_content.locator(
            'a[href="https://atsqa.org/certified-testers/profile/6676da6cab1b424aa4070395ff71f490"]'
        ).first
        self.linkedin_cta_text = page.get_by_text("Connect on LinkedIn", exact=True)
        self.github_cta_text = page.get_by_text("Follow on GitHub", exact=True)
        self.publications_cta_text = page.get_by_text("View Publications", exact=True)
        self.atsqa_cta_text = page.get_by_text("View Certified Tester Profile", exact=True)

        self.privacy_policy_link = page.get_by_role("link", name="Privacy Policy")
        self.terms_and_conditions_link = page.get_by_role("link", name="Terms & Conditions")

    def go_to_contact_page(self) -> None:
        self.nav_contact_link.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(r".*/contact$"))
        expect(self.page).to_have_title("Carlos Ng | Contact")

    def go_to_contact_page_direct(self) -> None:
        self.page.goto(f"{self.BASE_URL}/contact")
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(r".*/contact$"))
        expect(self.page).to_have_title("Carlos Ng | Contact")

    def verify_accessibility_elements(self) -> None:
        expect(self.skip_to_content_link).to_have_attribute("href", "#main-content")
        expect(self.main_content).to_be_visible()

    def verify_contact_page_header(self) -> None:
        expect(self.contact_heading).to_be_visible()
        expect(self.contact_subtitle).to_be_visible()

    def verify_contact_methods_section(self) -> None:
        expect(self.email_heading).to_be_visible()
        expect(self.linkedin_heading).to_be_visible()
        expect(self.github_heading).to_be_visible()
        expect(self.ieee_heading).to_be_visible()
        expect(self.atsqa_heading).to_be_visible()

        expect(self.email_link).to_be_visible()
        expect(self.linkedin_link).to_be_visible()
        expect(self.github_link).to_be_visible()
        expect(self.ieee_link).to_be_visible()
        expect(self.atsqa_link).to_be_visible()

        expect(self.email_link).to_have_attribute("href", "mailto:carlosng07@gmail.com")
        expect(self.linkedin_link).to_have_attribute("href", "https://www.linkedin.com/in/carlosng07")
        expect(self.github_link).to_have_attribute("href", "https://github.com/cng07")
        expect(self.ieee_link).to_have_attribute("href", "https://ieeexplore.ieee.org/author/37086553247")
        expect(self.atsqa_link).to_have_attribute(
            "href", "https://atsqa.org/certified-testers/profile/6676da6cab1b424aa4070395ff71f490"
        )

        expect(self.linkedin_cta_text).to_be_visible()
        expect(self.github_cta_text).to_be_visible()
        expect(self.publications_cta_text).to_be_visible()
        expect(self.atsqa_cta_text).to_be_visible()

    def verify_footer_section(self) -> None:
        expect(self.privacy_policy_link).to_be_visible()
        expect(self.terms_and_conditions_link).to_be_visible()
        expect(self.privacy_policy_link).to_have_attribute("href", "/privacy")
        expect(self.terms_and_conditions_link).to_have_attribute("href", "/terms")

    def verify_internal_links_api_responses(self) -> None:
        self.h.verify_internal_paths_api_responses(["/contact", "/privacy", "/terms"])

    def verify_external_contact_links_api_responses(self) -> None:
        external_urls = [
            "https://www.linkedin.com/in/carlosng07",
            "https://github.com/cng07",
            "https://ieeexplore.ieee.org/author/37086553247",
            "https://atsqa.org/certified-testers/profile/6676da6cab1b424aa4070395ff71f490",
        ]
        self.h.verify_urls_api_responses(external_urls, timeout=30000, url_type="external URL")

    def verify_all_contact_page_elements(self) -> None:
        self.verify_accessibility_elements()
        self.verify_contact_page_header()
        self.verify_contact_methods_section()
        self.verify_footer_section()

    def verify_all_contact_api_checks(self) -> None:
        self.verify_internal_links_api_responses()
        self.verify_external_contact_links_api_responses()
