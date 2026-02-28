from playwright.sync_api import sync_playwright
from pages.ProjectsPage import ProjectsPage
from pages.HomePage import HomePage


def test_projects_page(page):
    projects_page = ProjectsPage(page)
    home_page = HomePage(page)

    home_page.navigate()
    print(page.title())
    projects_page.click_projects()
    print("Projects:", page.url)
    projects_page.verifyProject1()
    projects_page.verifyProject2()
    projects_page.verifyProject3()
