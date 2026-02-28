from playwright.sync_api import Page

class CertificationsPage:
    def __init__(self, page: Page):
        self.page = page
        self.pageCertifications = page.get_by_role("link", name="Certifications")


    def click_certifications(self):
        self.pageCertifications.click()

    def verifyCertification1(self):
        assert self.page.get_by_text("ISTQB Certified Tester Foundation Level (CTFL)").is_visible()
        assert self.page.get_by_text("24-CTFL-01347-USA").is_visible()
        # assert self.page.get_by_alt_text("ISTQB Certified Tester Foundation Level (CTFL)").is_visible()
        assert self.page.locator("a[href*='1hC1IcfeBia77IPZjuVlVPJro6JD64uiV']").is_visible(), "Certification1 link is not visible on the Certifications page"

    def verifyCertification2(self):
        assert self.page.get_by_text("Certified Tester, AT*SQA DevOps Testing").is_visible()
        assert self.page.get_by_text("23-AT*DevOps-00002-USA").is_visible()
        # assert self.page.get_by_alt_text("Certified Tester, AT*SQA DevOps Testing").is_visible()
        assert self.page.locator("a[href*='1UqA8qJbYtNGSCNxxyFpiJKc8G2TtYgMy']").is_visible(), "Certification2 link is not visible on the Certifications page"
    
    def verifyCertification3(self):
        assert self.page.get_by_text("Accenture Agile Certification Program").is_visible()
        assert self.page.get_by_text("CNAG0000009961").is_visible()
        # assert self.page.get_by_alt_text("Accenture Agile Certification Program").is_visible()
        assert self.page.locator("a[href*='1wZCYGH8kWoyWfNPrV7jLUhyhJ99JWK8S']").is_visible(), "Certification3 link is not visible on the Certifications page"
    
    def verifyCertification4(self):
        assert self.page.get_by_text("Automation Anywhere Certified Advanced RPA Professional").is_visible()
        assert self.page.get_by_text("AAADVC-21147163").is_visible()
        # assert self.page.get_by_alt_text("Automation Anywhere Certified Advanced RPA Professional").is_visible()
        assert self.page.locator("a[href='https://certificates.automationanywhere.com/0b9f6c08-c724-44cc-81e0-c68c84d18225']").is_visible(), "Certification4 link is not visible on the Certifications page"
