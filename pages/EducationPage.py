import re

from playwright.sync_api import Page, expect

from pages.Helper import Helper


class EducationPage:
    BASE_URL = "https://carlosng07.vercel.app"

    def __init__(self, page: Page):
        self.page = page
        self.h = Helper(page)

        self.skip_to_content_link = page.get_by_role("link", name="Skip to content")
        self.main_content = page.locator("#main-content")

        self.nav_more_button = page.get_by_role("button", name="More")
        self.nav_education_menu_item = page.get_by_role("menuitem", name="Education")

        self.education_heading = page.get_by_role("heading", name="Education", level=1)
        self.section_cards = page.locator("div.glass")

        self.asia_pacific_college_heading = page.get_by_role("heading", name="Asia Pacific College", level=2)
        self.degree_text = page.get_by_text("BS Electronics Engineering", exact=True)
        self.tertiary_date_text = page.get_by_text("June 2013", exact=False)
        self.tertiary_location_text = page.get_by_text(
            "#3 Humabon Place, Magallanes, Makati City, Philippines", exact=True
        )
        self.honors_heading = page.get_by_text("Honors & Achievements", exact=True)
        self.scholarship_heading = page.get_by_text("SCHOLARSHIP", exact=False)
        self.scholarship_org_text = page.get_by_text("SM Foundation, Inc.", exact=True)

        self.leadership_heading = page.get_by_role("heading", name="Leadership & Involvement", level=2)
        self.apc_sees_text = page.get_by_text("APC Society of Electronics Engineering Students", exact=True)
        self.iecep_text = page.get_by_text(
            "Institute of Electronics Engineers of the Philippines (IECEP-Manila Student Chapter)", exact=True
        )
        self.scholars_text = page.get_by_text("APC SM Foundation Inc. Scholars", exact=True)
        self.math_society_text = page.get_by_text("APC Mathematics Society", exact=True)

        self.secondary_education_heading = page.get_by_role("heading", name="Secondary Education", level=2)
        self.makati_science_heading = page.get_by_role("heading", name="Makati Science High School", level=2)
        self.secondary_date_text = page.get_by_text("June 2009", exact=False)
        self.secondary_location_text = page.get_by_text("9 Kalayaan Ave, Makati City, Philippines", exact=True)

        self.publications_heading = page.get_by_role("heading", name="Publications", level=2)
        self.publication_title = page.get_by_role(
            "heading",
            name="A Development of a Low-Cost 12-Lead Electrocardiogram Monitoring Device Using Android-Based Smartphone",
            level=3,
        )
        self.doi_text = page.get_by_text("DOI: 10.1109/GCCE.2018.8574836", exact=True)
        self.proceedings_link = page.locator('a[href="https://ieeexplore.ieee.org/xpl/conhome/8555972/proceeding"]')
        self.ieee_xplore_link = page.locator('a[href="https://ieeexplore.ieee.org/document/8574836"]')

        self.privacy_policy_link = page.get_by_role("link", name="Privacy Policy")
        self.terms_and_conditions_link = page.get_by_role("link", name="Terms & Conditions")

    def go_to_education_page(self) -> None:
        expect(self.nav_more_button).to_be_visible()
        self.nav_more_button.click()
        expect(self.nav_education_menu_item).to_be_visible()
        self.nav_education_menu_item.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(r".*/education$"))
        expect(self.page).to_have_title("Carlos Ng | Education")

    def go_to_education_page_direct(self) -> None:
        self.page.goto(f"{self.BASE_URL}/education")
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(r".*/education$"))
        expect(self.page).to_have_title("Carlos Ng | Education")

    def verify_accessibility_elements(self) -> None:
        expect(self.skip_to_content_link).to_have_attribute("href", "#main-content")
        expect(self.main_content).to_be_visible()

    def verify_education_page_header(self) -> None:
        expect(self.education_heading).to_be_visible()
        section_card_count = self.section_cards.count()
        assert section_card_count >= 4, f"Expected at least 4 education section cards, found {section_card_count}"

    def verify_tertiary_section(self) -> None:
        expect(self.asia_pacific_college_heading).to_be_visible()
        expect(self.degree_text).to_be_visible()
        expect(self.tertiary_date_text).to_be_visible()
        expect(self.tertiary_location_text).to_be_visible()
        expect(self.honors_heading).to_be_visible()
        expect(self.scholarship_heading).to_be_visible()
        expect(self.scholarship_org_text).to_be_visible()

    def verify_leadership_and_involvement_section(self) -> None:
        expect(self.leadership_heading).to_be_visible()
        expect(self.apc_sees_text).to_be_visible()
        expect(self.iecep_text).to_be_visible()
        expect(self.scholars_text).to_be_visible()
        expect(self.math_society_text).to_be_visible()

    def verify_secondary_section(self) -> None:
        expect(self.secondary_education_heading).to_be_visible()
        expect(self.makati_science_heading).to_be_visible()
        expect(self.secondary_date_text).to_be_visible()
        expect(self.secondary_location_text).to_be_visible()

    def verify_publications_section(self) -> None:
        expect(self.publications_heading).to_be_visible()
        expect(self.publication_title).to_be_visible()
        expect(self.doi_text).to_be_visible()
        expect(self.proceedings_link).to_be_visible()
        expect(self.ieee_xplore_link).to_be_visible()
        expect(self.proceedings_link).to_have_attribute(
            "href", "https://ieeexplore.ieee.org/xpl/conhome/8555972/proceeding"
        )
        expect(self.ieee_xplore_link).to_have_attribute("href", "https://ieeexplore.ieee.org/document/8574836")

    def verify_footer_section(self) -> None:
        expect(self.privacy_policy_link).to_be_visible()
        expect(self.terms_and_conditions_link).to_be_visible()
        expect(self.privacy_policy_link).to_have_attribute("href", "/privacy")
        expect(self.terms_and_conditions_link).to_have_attribute("href", "/terms")

    def verify_internal_links_api_responses(self) -> None:
        self.h.verify_internal_paths_api_responses(["/education", "/privacy", "/terms"])

    def verify_publication_links_api_responses(self) -> None:
        publication_urls = [
            "https://ieeexplore.ieee.org/xpl/conhome/8555972/proceeding",
            "https://ieeexplore.ieee.org/document/8574836",
        ]
        self.h.verify_urls_api_responses(publication_urls, timeout=30000, url_type="publication URL")

    def verify_all_education_page_elements(self) -> None:
        self.verify_accessibility_elements()
        self.verify_education_page_header()
        self.verify_tertiary_section()
        self.verify_leadership_and_involvement_section()
        self.verify_secondary_section()
        self.verify_publications_section()
        self.verify_footer_section()

    def verify_all_education_api_checks(self) -> None:
        self.verify_internal_links_api_responses()
        self.verify_publication_links_api_responses()
