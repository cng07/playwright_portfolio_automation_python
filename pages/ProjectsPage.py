from playwright.sync_api import Page

class ProjectsPage:
    def __init__(self, page: Page):
        self.page = page
        self.pageProjects = page.get_by_role("link", name="Projects")

    def click_projects(self):
        self.pageProjects.click()

    def verifyProject1(self):
        project1 = self.page.get_by_role("heading", name="Portfolio Website Automation (JavaScript)")
        assert self.page.get_by_text("Comprehensive Playwright automation test suite for this portfolio website. Tests critical user flows including navigation, form submissions, and responsive design across browsers.").is_visible()
        assert self.page.locator("a[href='https://github.com/cng07/playwright_portfolio_automation_javascript']").is_visible(), "GitHub link for Project1 is not visible on the Projects page"
        assert project1.is_visible(), "Project1 is not visible on the Projects page"

    def verifyProject2(self):
        project2 = self.page.get_by_role("heading", name="Portfolio Website Automation (TypeScript)")
        assert self.page.get_by_text("Advanced Playwright automation framework using TypeScript with containerization and CI/CD support. Implements Page Object Model (POM) architecture for better scalability, type safety, and maintainability. Features Docker containerization and flexible CI/CD options with Jenkins and GitHub Actions.").is_visible()
        assert self.page.locator("a[href='https://github.com/cng07/playwright_portfolio_automation_typescript']").is_visible(), "GitHub link for Project2 is not visible on the Projects page"
        assert project2.is_visible(), "Project2 is not visible on the Projects page"
        

    def verifyProject3(self):
        project3 = self.page.get_by_role("heading", name="Portfolio Website Automation (Python)")
        assert self.page.get_by_text("UI automation for this portfolio site using Playwright and pytest. Implements a Page Object Model architecture covering Home and Projects page navigation, heading assertions, and HTML report generation.").is_visible()
        assert self.page.locator("a[href='https://github.com/cng07/playwright_portfolio_automation_python']").is_visible(), "GitHub link for Project3 is not visible on the Projects page"
        assert project3.is_visible(), "Project3 is not visible on the Projects page"

    def verifyProject4(self):
        project4 = self.page.get_by_role("heading", name="QA Practice Framework")
        assert self.page.get_by_text("Automated end-to-end test suites written in TypeScript using Playwright. Features a structured approach to testing web applications with reusable components and data-driven tests.").is_visible()
        assert self.page.locator("a[href='https://github.com/cng07/qaPractice']").is_visible(), "GitHub link for Project4 is not visible on the Projects page"
        assert project4.is_visible(), "Project4 is not visible on the Projects page"
