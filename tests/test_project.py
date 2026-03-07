from pages.HomePage import HomePage
from pages.ProjectsPage import ProjectsPage


def test_verify_projects_page_via_navigation(page):
    projects_page = ProjectsPage(page)
    home_page = HomePage(page)

    home_page.go_to_home_page()
    projects_page.go_to_projects_page()
    projects_page.verify_accessibility_elements()
    projects_page.verify_projects_page_header()
    projects_page.verify_project1()
    projects_page.verify_project2()
    projects_page.verify_project3()
    projects_page.verify_project4()
    projects_page.verify_repository_links()
    projects_page.verify_more_projects_coming_section()
    projects_page.verify_footer_section()


def test_verify_projects_page_ui_via_direct_url(page):
    projects_page = ProjectsPage(page)

    projects_page.go_to_projects_page_direct()
    projects_page.verify_all_projects_page_elements()


def test_verify_projects_page_api_links(page):
    projects_page = ProjectsPage(page)

    projects_page.go_to_projects_page_direct()
    projects_page.verify_repository_links()
    projects_page.verify_all_projects_api_checks()
