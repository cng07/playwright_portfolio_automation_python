from pages.HomePage import HomePage

def test_verify_home_page(page):
    home_page = HomePage(page)

    home_page.go_to_home_page()
    home_page.verify_accessibility_elements()
    home_page.verify_navigation_bar_section()
    home_page.verify_hero_section()
    home_page.verify_social_media_section()
    home_page.verify_featured_projects_section()
    home_page.verify_skills_section()
    home_page.verify_certifications_section()
    home_page.verify_publication_section()
    home_page.verify_experience_section()
    home_page.verify_footer_section()
