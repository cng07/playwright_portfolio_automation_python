import os
import re

from playwright.sync_api import Page, expect

from pages.Helper import Helper


class ResumePage:
    BASE_URL = "https://carlosng07.vercel.app"

    def __init__(self, page: Page):
        self.page = page
        self.h = Helper(page)

        self.skip_to_content_link = page.get_by_role("link", name="Skip to content")
        self.main_content = page.locator("#main-content")

        self.nav_resume_link = page.get_by_role("link", name="Resume")

        self.resume_heading = page.get_by_role("heading", name="Resume", level=1)
        self.download_pdf_button = page.get_by_role("button", name="Download PDF")
        self.resume_pdf_object = page.locator('object[type="application/pdf"]')
        self.resume_pdf_iframe = page.locator('object iframe[title="Carlos Ng Resume"]')

        self.privacy_policy_link = page.get_by_role("link", name="Privacy Policy")
        self.terms_and_conditions_link = page.get_by_role("link", name="Terms & Conditions")

    def go_to_resume_page(self) -> None:
        self.nav_resume_link.click()
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(r".*/resume$"))
        expect(self.page).to_have_title("Carlos Ng | Resume")

    def go_to_resume_page_direct(self) -> None:
        self.page.goto(f"{self.BASE_URL}/resume")
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.page).to_have_url(re.compile(r".*/resume$"))
        expect(self.page).to_have_title("Carlos Ng | Resume")

    def verify_accessibility_elements(self) -> None:
        expect(self.skip_to_content_link).to_have_attribute("href", "#main-content")
        expect(self.main_content).to_be_visible()

    def verify_resume_page_header(self) -> None:
        expect(self.resume_heading).to_be_visible()

    def verify_download_pdf_button(self) -> None:
        expect(self.download_pdf_button).to_be_visible()
        expect(self.download_pdf_button).to_be_enabled()

    def verify_resume_viewer_section(self) -> None:
        expect(self.resume_pdf_object).to_be_visible()
        expect(self.resume_pdf_object).to_have_attribute("data", "/Carlos_Ng_Resume.pdf")
        expect(self.resume_pdf_iframe).to_have_count(1)
        expect(self.resume_pdf_iframe).to_have_attribute("src", re.compile(r"docs\.google\.com/viewer"))
        expect(self.resume_pdf_iframe).to_have_attribute("src", re.compile(r"Carlos_Ng_Resume\.pdf"))

    def download_pdf_and_verify(self) -> None:
        with self.page.expect_download() as download_info:
            self.download_pdf_button.click()
        download = download_info.value

        filename = download.suggested_filename
        assert filename == "Carlos_Ng_Resume.pdf", f"Unexpected downloaded file name: {filename}"
        assert "/Carlos_Ng_Resume.pdf" in download.url, f"Unexpected download URL: {download.url}"

        api_response = self.page.request.get(download.url, timeout=30000)
        assert api_response.status == 200, f"Expected status 200 for download URL, got {api_response.status}"
        content_type = api_response.headers.get("content-type", "")
        assert "application/pdf" in content_type, f"Unexpected content type for download URL: {content_type}"

        file_path = download.path()
        assert file_path, "Download path is empty"

        file_size_kb = os.path.getsize(file_path) / 1024
        assert file_size_kb > 500, f"Unexpectedly small resume PDF: {file_size_kb:.2f}KB"
        assert file_size_kb < 1000, f"Unexpectedly large resume PDF: {file_size_kb:.2f}KB"

        os.remove(file_path)

    def verify_footer_section(self) -> None:
        expect(self.privacy_policy_link).to_be_visible()
        expect(self.terms_and_conditions_link).to_be_visible()
        expect(self.privacy_policy_link).to_have_attribute("href", "/privacy")
        expect(self.terms_and_conditions_link).to_have_attribute("href", "/terms")

    def verify_resume_pdf_api_response(self) -> None:
        response = self.page.request.get(f"{self.BASE_URL}/Carlos_Ng_Resume.pdf", timeout=30000)
        assert response.status == 200, f"Expected status 200 for resume PDF URL, got {response.status}"
        content_type = response.headers.get("content-type", "")
        assert "application/pdf" in content_type, f"Unexpected content type for resume PDF URL: {content_type}"

        content_length = int(response.headers.get("content-length", "0"))
        assert content_length > 500000, f"Unexpected content-length for resume PDF: {content_length}"

    def verify_resume_internal_links_api_responses(self) -> None:
        self.h.verify_internal_paths_api_responses(["/resume", "/privacy", "/terms"])

    def verify_all_resume_page_elements(self) -> None:
        self.verify_accessibility_elements()
        self.verify_resume_page_header()
        self.verify_download_pdf_button()
        self.verify_resume_viewer_section()
        self.verify_footer_section()

    def verify_all_resume_api_checks(self) -> None:
        self.verify_resume_pdf_api_response()
        self.verify_resume_internal_links_api_responses()
