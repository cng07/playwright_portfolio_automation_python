import re

from playwright.sync_api import Page, expect

from pages.Helper import Helper


class AboutPage:
    BASE_URL = "https://carlosng07.vercel.app"

    def __init__(self, page: Page):
        self.page = page
        self.h = Helper(page)

        self.skip_to_content_link = page.get_by_role("link", name="Skip to content")
        self.main_content = page.locator("#main-content")

        self.nav_about_link = page.get_by_role("link", name="About")

        self.about_heading = page.get_by_role("heading", name="About Me", level=1)
        self.intro_heading = page.get_by_role("heading", name="I'm Carlos Ng", level=2)
        self.qa_philosophy_heading = page.get_by_role("heading", name="QA Philosophy", level=3)
        self.name_heading = page.get_by_role("heading", name="Carlos Angelo E. Ng", level=3)
        self.about_intro_paragraph = page.get_by_text(
            "A Test Automation Engineer with 7+ years of experience in software testing", exact=False
        )
        self.main_tool_text = page.get_by_text("Main tool I use these days: Playwright - TypeScript", exact=False)
        self.role_text = page.get_by_text("Senior Quality Assurance Automation Engineer", exact=False)

        self.profile_image = page.get_by_alt_text("Carlos Angelo E. Ng - Professional")
        self.original_image = page.get_by_alt_text("Carlos Angelo E. Ng - Original")

        self.fast_execution_title = page.get_by_text("Fast Execution", exact=True)
        self.fast_execution_description = page.get_by_text(
            "Reduced execution time from 19 hours to 4 hours for 300+ test cases.", exact=True
        )
        self.maintained_code_title = page.get_by_text("Maintained Code", exact=True)
        self.maintained_code_description = page.get_by_text("Stable, clean, and reliable test suites.", exact=True)
        self.qa_philosophy_description = page.get_by_text(
            "My goal in QA is simple: reduce risk, increase confidence, and keep releases smooth.", exact=True
        )

        self.github_link = page.get_by_role("link", name="@cng07")
        self.linkedin_link = page.get_by_role("link", name="@carlosng07")
        self.email_link = page.get_by_role("link", name="carlosng07@gmail.com")

        self.privacy_policy_link = page.get_by_role("link", name="Privacy Policy")
        self.terms_and_conditions_link = page.get_by_role("link", name="Terms & Conditions")

    def go_to_about_page(self) -> None:
        self.nav_about_link.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(r".*/about$"))
        expect(self.page).to_have_title("Carlos Ng | About")

    def go_to_about_page_direct(self) -> None:
        self.page.goto(f"{self.BASE_URL}/about")
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(r".*/about$"))
        expect(self.page).to_have_title("Carlos Ng | About")

    def verify_accessibility_elements(self) -> None:
        expect(self.skip_to_content_link).to_have_attribute("href", "#main-content")
        expect(self.main_content).to_be_visible()

    def verify_about_page_header(self) -> None:
        expect(self.about_heading).to_be_visible()
        expect(self.intro_heading).to_be_visible()

    def verify_about_profile_section(self) -> None:
        expect(self.about_intro_paragraph).to_be_visible()
        expect(self.main_tool_text).to_be_visible()
        expect(self.name_heading).to_be_visible()
        expect(self.role_text).to_be_visible()
        expect(self.profile_image).to_be_visible()
        expect(self.original_image).to_be_visible()

    def verify_highlights_and_philosophy(self) -> None:
        expect(self.fast_execution_title).to_be_visible()
        expect(self.fast_execution_description).to_be_visible()
        expect(self.maintained_code_title).to_be_visible()
        expect(self.maintained_code_description).to_be_visible()
        expect(self.qa_philosophy_heading).to_be_visible()
        expect(self.qa_philosophy_description).to_be_visible()

    def verify_contact_links(self) -> None:
        expect(self.github_link).to_be_visible()
        expect(self.linkedin_link).to_be_visible()
        expect(self.email_link).to_be_visible()

        expect(self.github_link).to_have_attribute("href", "https://github.com/cng07")
        expect(self.linkedin_link).to_have_attribute("href", "https://www.linkedin.com/in/carlosng07")
        expect(self.email_link).to_have_attribute("href", "mailto:carlosng07@gmail.com")

    def verify_footer_section(self) -> None:
        expect(self.privacy_policy_link).to_be_visible()
        expect(self.terms_and_conditions_link).to_be_visible()
        expect(self.privacy_policy_link).to_have_attribute("href", "/privacy")
        expect(self.terms_and_conditions_link).to_have_attribute("href", "/terms")

    def verify_internal_links_api_responses(self) -> None:
        self.h.verify_internal_paths_api_responses(["/about", "/privacy", "/terms"])

    def verify_all_about_page_elements(self) -> None:
        self.verify_accessibility_elements()
        self.verify_about_page_header()
        self.verify_about_profile_section()
        self.verify_highlights_and_philosophy()
        self.verify_contact_links()
        self.verify_footer_section()
