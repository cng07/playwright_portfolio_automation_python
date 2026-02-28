from playwright.sync_api import Page

class ProjectsPage:
    def __init__(self, page: Page):
        self.page = page
        self.pageProjects = page.get_by_role("link", name="Projects")


    def navigate(self):
        self.page.goto("https://carlosng07.vercel.app/")

    def click_projects(self):
        self.pageProjects.click()

    def verifyProject1(self):
        project1 = self.page.get_by_role("heading", name="Portfolio Website Automation (JavaScript)")
        assert project1.is_visible(), "Project1 is not visible on the Projects page"

    def verifyProject2(self):
        project2 = self.page.get_by_role("heading", name="Portfolio Website Automation (TypeScript)")
        assert project2.is_visible(), "Project2 is not visible on the Projects page"

    def verifyProject3(self):
        project3 = self.page.get_by_role("heading", name="QA Practice Framework")
        assert project3.is_visible(), "Project3 is not visible on the Projects page"