from pages.HomePage import HomePage

def test_home(page):
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # page = browser.new_page()
    page.goto("https://carlosng07.vercel.app/")
    print(page.title())
    projects_button = page.get_by_role("link", name="Projects", exact=True)
    projects_button.click()
    print("Projects:", page.url)

def test_home_page_object(page):
    home_page = HomePage(page)
    home_page.navigate()
    print(page.title())
    home_page.click_projects()
    print("Projects:", page.url)

def test_home_api(page):
    response = page.request.get("https://carlosng07.vercel.app/")

    assert response.status == 200, f"Expected status code 200, but got {response.status}"
    print("API response status code:", response.status)
    content_type = response.headers.get("content-type", "")
    print("API response content-type:", content_type)
    assert "text/html" in content_type or "application/json" in content_type, (
        f"Unexpected content-type: {content_type}"
    )
    if "application/json" in content_type:
        json_data = response.json()
        print(json_data)
    else:
        html = response.text()
        print(html[:200])
