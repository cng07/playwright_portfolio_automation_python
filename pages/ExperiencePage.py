import re

from playwright.sync_api import Page, expect

from pages.Helper import Helper


class ExperiencePage:
    BASE_URL = "https://carlosng07.vercel.app"

    def __init__(self, page: Page):
        self.page = page
        self.h = Helper(page)

        self.skip_to_content_link = page.get_by_role("link", name="Skip to content")
        self.main_content = page.locator("#main-content")

        self.nav_experience_link = page.get_by_role("link", name="Experience")

        self.experience_heading = page.get_by_role("heading", name="Work Experience", level=1)
        self.experience_cards = page.locator("div.glass")

        self.datacom_heading = page.get_by_role("heading", name="Datacom", level=3)
        self.planit_heading = page.get_by_role("heading", name="Planit", level=3)
        self.dxc_heading = page.get_by_role("heading", name="DXC Technology", level=3)
        self.davi_heading = page.get_by_role("heading", name="Data Analytics Ventures, Inc.", level=3)
        self.accenture_heading_1 = page.get_by_role("heading", name="Accenture", level=3).nth(0)
        self.accenture_heading_2 = page.get_by_role("heading", name="Accenture", level=3).nth(1)

        self.current_role_text = page.get_by_text("Senior Quality Assurance Automation Engineer", exact=False)
        self.current_date_range_text = page.get_by_text("April 2025", exact=False)
        self.taguig_location_text = page.get_by_text("Taguig City, Philippines", exact=True).nth(0)
        self.pasig_location_text = page.get_by_text("Pasig City, Philippines", exact=True)
        self.mandaluyong_location_text = page.get_by_text("Mandaluyong City, Philippines", exact=True).nth(0)

        self.datacom_link = page.get_by_role("link", name="Datacom", exact=True)
        self.planit_link = page.get_by_role("link", name="Planit", exact=True)
        self.dxc_link = page.get_by_role("link", name="DXC Technology", exact=True)
        self.davi_link = page.get_by_role("link", name="Data Analytics Ventures, Inc.", exact=True)
        self.accenture_link_1 = page.get_by_role("link", name="Accenture", exact=True).nth(0)
        self.accenture_link_2 = page.get_by_role("link", name="Accenture", exact=True).nth(1)

        self.privacy_policy_link = page.get_by_role("link", name="Privacy Policy")
        self.terms_and_conditions_link = page.get_by_role("link", name="Terms & Conditions")

    def go_to_experience_page(self) -> None:
        self.nav_experience_link.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(r".*/experience$"))
        expect(self.page).to_have_title("Carlos Ng | Experience")

    def go_to_experience_page_direct(self) -> None:
        self.page.goto(f"{self.BASE_URL}/experience")
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(r".*/experience$"))
        expect(self.page).to_have_title("Carlos Ng | Experience")

    def verify_accessibility_elements(self) -> None:
        expect(self.skip_to_content_link).to_have_attribute("href", "#main-content")
        expect(self.main_content).to_be_visible()

    def verify_experience_page_header(self) -> None:
        expect(self.experience_heading).to_be_visible()
        cards_count = self.experience_cards.count()
        assert cards_count >= 6, f"Expected at least 6 experience cards, found {cards_count}"

    def verify_experience_entries(self) -> None:
        expect(self.datacom_heading).to_be_visible()
        expect(self.planit_heading).to_be_visible()
        expect(self.dxc_heading).to_be_visible()
        expect(self.davi_heading).to_be_visible()
        expect(self.accenture_heading_1).to_be_visible()
        expect(self.accenture_heading_2).to_be_visible()

        expect(self.current_role_text).to_be_visible()
        expect(self.current_date_range_text).to_be_visible()
        expect(self.taguig_location_text).to_be_visible()
        expect(self.pasig_location_text).to_be_visible()
        expect(self.mandaluyong_location_text).to_be_visible()

    def verify_company_links(self) -> None:
        expect(self.datacom_link).to_be_visible()
        expect(self.planit_link).to_be_visible()
        expect(self.dxc_link).to_be_visible()
        expect(self.davi_link).to_be_visible()
        expect(self.accenture_link_1).to_be_visible()
        expect(self.accenture_link_2).to_be_visible()

        expect(self.datacom_link).to_have_attribute("href", "https://datacom.com/nz/en")
        expect(self.planit_link).to_have_attribute("href", "https://www.planit.com/")
        expect(self.dxc_link).to_have_attribute("href", "https://dxc.com/")
        expect(self.davi_link).to_have_attribute("href", "https://www.davi.com.ph/")
        expect(self.accenture_link_1).to_have_attribute("href", "https://www.accenture.com/ph-en")
        expect(self.accenture_link_2).to_have_attribute("href", "https://www.accenture.com/ph-en")

    def verify_footer_section(self) -> None:
        expect(self.privacy_policy_link).to_be_visible()
        expect(self.terms_and_conditions_link).to_be_visible()
        expect(self.privacy_policy_link).to_have_attribute("href", "/privacy")
        expect(self.terms_and_conditions_link).to_have_attribute("href", "/terms")

    def verify_internal_links_api_responses(self) -> None:
        self.h.verify_internal_paths_api_responses(["/experience", "/privacy", "/terms"])

    def verify_external_company_links_api_responses(self) -> None:
        external_urls = [
            "https://datacom.com/nz/en",
            "https://www.planit.com/",
            "https://dxc.com/",
            "https://www.davi.com.ph/",
            "https://www.accenture.com/ph-en",
        ]
        self.h.verify_urls_api_responses(
            external_urls, timeout=30000, url_type="external URL", max_status_code=499, disallow_404=True
        )

    def verify_all_experience_page_elements(self) -> None:
        self.verify_accessibility_elements()
        self.verify_experience_page_header()
        self.verify_experience_entries()
        self.verify_company_links()
        self.verify_footer_section()

    def verify_all_experience_api_checks(self) -> None:
        self.verify_internal_links_api_responses()
        self.verify_external_company_links_api_responses()
