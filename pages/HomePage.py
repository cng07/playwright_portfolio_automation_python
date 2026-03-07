import re

from playwright.sync_api import Page, expect

from pages.Helper import Helper


class HomePage:
    BASE_URL = "https://carlosng07.vercel.app"

    def __init__(self, page: Page):
        self.page = page
        self.h = Helper(page)

        self.skip_to_content_link = page.get_by_role("link", name="Skip to content")
        self.main_content = page.locator("#main-content")

        self.nav_logo = page.locator("a.nav-logo")
        self.nav_home_link = page.get_by_role("link", name="Home")
        self.nav_projects_link = page.get_by_role("link", name="Projects", exact=True)
        self.nav_resume_link = page.get_by_role("link", name="Resume")
        self.nav_certifications_link = page.get_by_role("menuitem", name="Certifications")
        self.nav_education_link = page.get_by_role("menuitem", name="Education")
        self.nav_about_link = page.get_by_role("link", name="About")
        self.nav_contact_link = page.get_by_role("link", name="Contact")
        self.nav_more = page.get_by_role("button", name="More")
        self.mobile_menu_button = page.locator("button.mobile-menu-btn")

        self.profile_image = page.get_by_alt_text("Carlos Angelo E. Ng")
        self.hero_name_heading = page.get_by_role("heading", name="Carlos Angelo E. Ng", level=2)
        self.hero_tagline_heading = page.get_by_role("heading", name="Automating Quality Delivering Excellence", level=1)
        self.hero_role_text = page.get_by_text("Senior Quality Assurance Automation Engineer at Datacom")
        self.hero_intro_text = page.get_by_text("Hi, I'm Carlos Ng.", exact=False)

        self.linkedin_button = page.get_by_alt_text("LinkedIn Logo")
        self.github_button = page.get_by_alt_text("GitHub Logo")
        self.ieee_button = page.get_by_alt_text("IEEE Logo")
        self.astqb_button = page.get_by_alt_text("ASTQB Logo")

        self.featured_projects_section_title = page.get_by_role("heading", name="Featured Projects", level=2)
        self.portfolio_typescript_project_title = page.get_by_role(
            "heading", name="Portfolio Website Automation (TypeScript)", level=3
        )
        self.portfolio_python_project_title = page.get_by_role(
            "heading", name="Portfolio Website Automation (Python)", level=3
        )
        self.project_repository_links = page.get_by_role("link", name="Repository")
        self.view_all_projects_link = page.get_by_role("link", name="View All Projects")

        self.skills_section_title = page.locator('h2:has-text("Technical Skills")')
        self.test_automation_card = page.locator('h3:has-text("Test Automation")')
        self.programming_languages_card = page.locator('h3:has-text("Programming Languages")')
        self.cicd_card = page.locator('h3:has-text("CI/CD")')
        self.manual_testing_card = page.locator('h3:has-text("Manual Testing")')
        self.other_tools_card = page.locator('h3:has-text("Other Tools")')
        self.ai_tools_card = page.locator('h3:has-text("AI Tools")')

        self.certifications_section_title = page.get_by_role("heading", name="Certifications", level=2)
        self.ctfl_certification_preview = page.get_by_text("ISTQB Certified Tester Foundation Level (CTFL)", exact=True)
        self.view_certificate_link = page.get_by_role("link", name="View Certificate")
        self.view_all_certifications_link = page.get_by_role("link", name="View All 4 Certifications")

        self.publication_section_title = page.get_by_role("heading", name="Publication", level=2)
        self.publication_title = page.get_by_text(
            "A Development of a Low-Cost 12-Lead Electrocardiogram Monitoring Device Using Android-based Smartphone",
            exact=True,
        )
        self.publication_date = page.get_by_text("Published in IEEE, 2018", exact=True)
        self.view_paper_link = page.get_by_role("link", name="View Paper")

        self.experience_section_title = page.locator('h2:has-text("Experience")')
        self.datacom_company_link = page.get_by_role("link", name="Datacom", exact=True)
        self.planit_company_link = page.get_by_role("link", name="Planit", exact=True)
        self.dxc_company_link = page.get_by_role("link", name="DXC Technology", exact=True)
        self.davi_company_link = page.get_by_role("link", name="Data Analytics Ventures, Inc.", exact=True)
        self.accenture_company_link_1 = page.get_by_role("link", name="Accenture", exact=True).nth(0)
        self.accenture_company_link_2 = page.get_by_role("link", name="Accenture", exact=True).nth(1)

        self.home_button = page.get_by_text("home")

    def go_to_home_page(self) -> None:
        self.page.goto(f"{self.BASE_URL}/")
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_title("Carlos Ng | Portfolio")
        expect(self.home_button).to_be_visible()
        expect(self.linkedin_button).to_be_visible()

    def verify_accessibility_elements(self) -> None:
        expect(self.skip_to_content_link).to_have_attribute("href", "#main-content")
        expect(self.main_content).to_be_visible()

    def verify_navigation_bar_section(self) -> None:
        expect(self.nav_logo).to_be_visible()
        expect(self.nav_home_link).to_be_visible()
        expect(self.nav_projects_link).to_be_visible()
        expect(self.nav_resume_link).to_be_visible()
        expect(self.nav_about_link).to_be_visible()
        expect(self.nav_contact_link).to_be_visible()
        expect(self.nav_projects_link).to_have_attribute("href", "/projects")
        expect(self.nav_resume_link).to_have_attribute("href", "/resume")
        expect(self.nav_about_link).to_have_attribute("href", "/about")
        expect(self.nav_contact_link).to_have_attribute("href", "/contact")
        expect(self.nav_more).to_be_visible()
        self.nav_more.click()
        expect(self.nav_certifications_link).to_be_visible()
        expect(self.nav_education_link).to_be_visible()
        expect(self.nav_certifications_link).to_have_attribute("href", "/certifications")
        expect(self.nav_education_link).to_have_attribute("href", "/education")

    def verify_hero_section(self) -> None:
        expect(self.profile_image).to_be_visible()
        expect(self.hero_name_heading).to_be_visible()
        expect(self.hero_tagline_heading).to_be_visible()
        expect(self.hero_role_text).to_be_visible()
        expect(self.hero_intro_text).to_be_visible()

    def verify_social_media_section(self) -> None:
        expect(self.linkedin_button).to_be_visible()
        expect(self.github_button).to_be_visible()
        expect(self.ieee_button).to_be_visible()
        expect(self.astqb_button).to_be_visible()

    def verify_featured_projects_section(self) -> None:
        expect(self.featured_projects_section_title).to_be_visible()
        expect(self.portfolio_typescript_project_title).to_be_visible()
        expect(self.portfolio_python_project_title).to_be_visible()
        expect(self.view_all_projects_link).to_be_visible()
        expect(self.view_all_projects_link).to_have_attribute("href", "/projects")

        repository_link_count = self.project_repository_links.count()
        assert repository_link_count >= 2, f"Expected at least 2 repository links, found {repository_link_count}"
        expect(self.project_repository_links.nth(0)).to_be_visible()
        expect(self.project_repository_links.nth(1)).to_be_visible()

    def verify_skills_section(self) -> None:
        expect(self.skills_section_title).to_be_visible()
        expect(self.skills_section_title).to_contain_text("Technical Skills")
        expect(self.test_automation_card).to_be_visible()
        expect(self.programming_languages_card).to_be_visible()
        expect(self.cicd_card).to_be_visible()
        expect(self.manual_testing_card).to_be_visible()
        expect(self.other_tools_card).to_be_visible()
        expect(self.ai_tools_card).to_be_visible()

    def verify_certifications_section(self) -> None:
        expect(self.certifications_section_title).to_be_visible()
        expect(self.ctfl_certification_preview).to_be_visible()
        expect(self.view_certificate_link).to_be_visible()
        expect(self.view_all_certifications_link).to_be_visible()
        expect(self.view_all_certifications_link).to_have_attribute("href", "/certifications")

    def verify_publication_section(self) -> None:
        expect(self.publication_section_title).to_be_visible()
        expect(self.publication_title).to_be_visible()
        expect(self.publication_date).to_be_visible()
        expect(self.view_paper_link).to_be_visible()
        expect(self.view_paper_link).to_have_attribute("href", re.compile(r"ieeexplore\.ieee\.org"))

    def verify_experience_section(self) -> None:
        expect(self.experience_section_title).to_be_visible()
        expect(self.experience_section_title).to_contain_text("Experience")
        expect(self.datacom_company_link).to_be_visible()
        expect(self.planit_company_link).to_be_visible()
        expect(self.dxc_company_link).to_be_visible()
        expect(self.davi_company_link).to_be_visible()
        expect(self.accenture_company_link_1).to_be_visible()
        expect(self.accenture_company_link_2).to_be_visible()

    def verify_footer_section(self) -> None:
        privacy_policy_link = self.page.get_by_role("link", name="Privacy Policy")
        terms_and_conditions_link = self.page.get_by_role("link", name="Terms & Conditions")
        expect(privacy_policy_link).to_be_visible()
        expect(terms_and_conditions_link).to_be_visible()
        expect(privacy_policy_link).to_have_attribute("href", "/privacy")
        expect(terms_and_conditions_link).to_have_attribute("href", "/terms")
