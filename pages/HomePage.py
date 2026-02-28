from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.pageHome = page.get_by_role("link", name="Home")
        self.pageProjects = page.get_by_role("link", name="Projects")
        self.pageResume = page.get_by_role("link", name="Resume")
        self.pageCertifications = page.get_by_role("link", name="Certifications")
        self.pageEducation = page.get_by_role("link", name="Education")
        self.pageAbout = page.get_by_role("link", name="About")
        self.pageContact = page.get_by_role("link", name="Contact")


    def navigate(self):
        self.page.goto("https://carlosng07.vercel.app/")

    def click_projects(self):
        self.pageProjects.click()