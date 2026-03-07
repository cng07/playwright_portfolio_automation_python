import re

from playwright.sync_api import Page, expect

from pages.Helper import Helper


class ProjectsPage:
    BASE_URL = "https://carlosng07.vercel.app"

    def __init__(self, page: Page):
        self.page = page
        self.h = Helper(page)

        self.skip_to_content_link = page.get_by_role("link", name="Skip to content")
        self.main_content = page.locator("#main-content")

        self.nav_projects_link = page.get_by_role("link", name="Projects", exact=True)

        self.projects_heading = page.get_by_role("heading", name="Projects", level=1)
        self.text_highlights = page.get_by_text("Highlights")
        self.text_technologies = page.get_by_text("Technologies")
        self.project_titles = page.locator("h3")
        self.project_status_active = page.get_by_text("Active", exact=True)
        self.repository_links = page.get_by_role("link", name="Repository")

        self.project_javascript_title = page.get_by_role(
            "heading", name="Portfolio Website Automation (JavaScript)", level=3
        )
        self.project_javascript_card = page.locator("div.glass").filter(has=self.project_javascript_title)
        self.project_typescript_title = page.get_by_role(
            "heading", name="Portfolio Website Automation (TypeScript)", level=3
        )
        self.project_typescript_card = page.locator("div.glass").filter(has=self.project_typescript_title)
        self.project_python_title = page.get_by_role("heading", name="Portfolio Website Automation (Python)", level=3)
        self.project_python_card = page.locator("div.glass").filter(has=self.project_python_title)
        self.project_qa_practice_title = page.get_by_role("heading", name="QA Practice Framework", level=3)
        self.project_qa_practice_card = page.locator("div.glass").filter(has=self.project_qa_practice_title)

        self.more_projects_coming_heading = page.get_by_role("heading", name="More Projects Coming", level=2)
        self.more_projects_coming_text = page.get_by_text("Check back soon for updates!", exact=True)

        self.privacy_policy_link = page.get_by_role("link", name="Privacy Policy")
        self.terms_and_conditions_link = page.get_by_role("link", name="Terms & Conditions")

    def go_to_projects_page(self) -> None:
        self.nav_projects_link.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(r".*/projects$"))
        expect(self.page).to_have_title("Carlos Ng | Projects")

    def go_to_projects_page_direct(self) -> None:
        self.page.goto(f"{self.BASE_URL}/projects")
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(r".*/projects$"))
        expect(self.page).to_have_title("Carlos Ng | Projects")

    def verify_accessibility_elements(self) -> None:
        expect(self.skip_to_content_link).to_have_attribute("href", "#main-content")
        expect(self.main_content).to_be_visible()

    def verify_projects_page_header(self) -> None:
        expect(self.projects_heading).to_be_visible()
        expect(self.project_titles).to_have_count(4)
        expect(self.project_status_active).to_have_count(4)
        expect(self.text_highlights).to_have_count(4)
        expect(self.text_technologies).to_have_count(4)

    def verify_project1(self) -> None:
        expect(self.project_javascript_title).to_be_visible()
        expect(
            self.project_javascript_card.get_by_text(
                "Comprehensive Playwright automation test suite for this portfolio website.", exact=False
            )
        ).to_be_visible()
        expect(self.text_highlights.nth(0)).to_be_visible()
        expect(self.project_javascript_card.get_by_text("Cross-browser testing (Chrome, Firefox, Safari, Edge)")).to_be_visible()
        expect(self.project_javascript_card.get_by_text("Link integrity checks")).to_be_visible()
        expect(self.project_javascript_card.get_by_text("CI/CD integration with GitHub Actions")).to_be_visible()
        expect(self.text_technologies.nth(0)).to_be_visible()
        expect(self.project_javascript_card.get_by_text("JavaScript", exact=True)).to_be_visible()
        expect(self.project_javascript_card.get_by_text("GitHub Actions", exact=True)).to_be_visible()

    def verify_project2(self) -> None:
        expect(self.project_typescript_title).to_be_visible()
        expect(
            self.project_typescript_card.get_by_text(
                "Advanced Playwright automation framework using TypeScript with containerization and CI/CD support.",
                exact=False,
            )
        ).to_be_visible()
        expect(self.text_highlights.nth(1)).to_be_visible()
        expect(self.project_typescript_card.get_by_text("Strongly typed test architecture with TypeScript")).to_be_visible()
        expect(self.project_typescript_card.get_by_text("Page Object Model (POM) implementation")).to_be_visible()
        expect(
            self.project_typescript_card.get_by_text("Docker containerization for consistent test environments")
        ).to_be_visible()
        expect(
            self.project_typescript_card.get_by_text("Multi-platform CI/CD support (Jenkins & GitHub Actions)")
        ).to_be_visible()
        expect(self.text_technologies.nth(1)).to_be_visible()
        expect(self.project_typescript_card.get_by_text("TypeScript", exact=True)).to_be_visible()
        expect(self.project_typescript_card.get_by_text("Jenkins", exact=True)).to_be_visible()
        expect(self.project_typescript_card.get_by_text("Docker", exact=True)).to_be_visible()

    def verify_project3(self) -> None:
        expect(self.project_python_title).to_be_visible()
        expect(
            self.project_python_card.get_by_text(
                "UI automation for this portfolio site using Playwright and pytest.", exact=False
            )
        ).to_be_visible()
        expect(self.text_highlights.nth(2)).to_be_visible()
        expect(self.project_python_card.get_by_text("Page Object Model (POM) for Home & Projects pages")).to_be_visible()
        expect(self.project_python_card.get_by_text("pytest + playwright integration")).to_be_visible()
        expect(self.project_python_card.get_by_text("HTML report generation via pytest-html")).to_be_visible()
        expect(self.text_technologies.nth(2)).to_be_visible()
        expect(self.project_python_card.get_by_text("Python", exact=True)).to_be_visible()
        expect(self.project_python_card.get_by_text("pytest", exact=True)).to_be_visible()

    def verify_project4(self) -> None:
        expect(self.project_qa_practice_title).to_be_visible()
        expect(
            self.project_qa_practice_card.get_by_text(
                "Automated end-to-end test suites written in TypeScript using Playwright.", exact=False
            )
        ).to_be_visible()
        expect(self.text_highlights.nth(3)).to_be_visible()
        expect(self.project_qa_practice_card.get_by_text("Data-driven testing via CSV integration")).to_be_visible()
        expect(self.project_qa_practice_card.get_by_text("Page Object Model (POM) architecture")).to_be_visible()
        expect(self.project_qa_practice_card.get_by_text("Automated form validation & edge case handling")).to_be_visible()
        expect(self.text_technologies.nth(3)).to_be_visible()

    def verify_repository_links(self) -> None:
        expect(self.repository_links).to_have_count(4)

        repository_hrefs = [self.repository_links.nth(i).get_attribute("href") for i in range(self.repository_links.count())]
        assert repository_hrefs == [
            "https://github.com/cng07/playwright_portfolio_automation_javascript",
            "https://github.com/cng07/playwright_portfolio_automation_typescript",
            "https://github.com/cng07/playwright_portfolio_automation_python",
            "https://github.com/cng07/qaPractice",
        ]

    def verify_repository_links_api_responses(self) -> None:
        repository_hrefs = [
            self.repository_links.nth(i).get_attribute("href")
            for i in range(self.repository_links.count())
            if self.repository_links.nth(i).get_attribute("href")
        ]
        self.h.verify_urls_api_responses(repository_hrefs, timeout=30000, url_type="repository URL")

    def verify_more_projects_coming_section(self) -> None:
        expect(self.more_projects_coming_heading).to_be_visible()
        expect(self.more_projects_coming_text).to_be_visible()

    def verify_footer_section(self) -> None:
        expect(self.privacy_policy_link).to_be_visible()
        expect(self.terms_and_conditions_link).to_be_visible()
        expect(self.privacy_policy_link).to_have_attribute("href", "/privacy")
        expect(self.terms_and_conditions_link).to_have_attribute("href", "/terms")

    def verify_internal_links_api_responses(self) -> None:
        self.h.verify_internal_paths_api_responses(["/projects", "/privacy", "/terms"])

    def verify_all_projects_page_elements(self) -> None:
        self.verify_accessibility_elements()
        self.verify_projects_page_header()
        self.verify_project1()
        self.verify_project2()
        self.verify_project3()
        self.verify_project4()
        self.verify_repository_links()
        self.verify_more_projects_coming_section()
        self.verify_footer_section()

    def verify_all_projects_api_checks(self) -> None:
        self.verify_repository_links_api_responses()
        self.verify_internal_links_api_responses()
