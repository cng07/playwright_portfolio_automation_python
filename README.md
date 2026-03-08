# Playwright Portfolio Automation (Python)

UI and API-link automation for `https://carlosng07.vercel.app/` using Playwright (sync API) + pytest, implemented with a Page Object Model structure mirrored from the TypeScript project.

## Coverage
- Home
- Projects
- Certifications
- About
- Contact
- Education
- Experience
- Resume (including PDF download checks)

## Project structure
- `pages/Helper.py` - shared API-link helpers
- `pages/HomePage.py`
- `pages/ProjectsPage.py`
- `pages/CertificationsPage.py`
- `pages/AboutPage.py`
- `pages/ContactPage.py`
- `pages/EducationPage.py`
- `pages/ExperiencePage.py`
- `pages/ResumePage.py`
- `tests/test_home.py`
- `tests/test_project.py`
- `tests/test_certification.py`
- `tests/test_about.py`
- `tests/test_contact.py`
- `tests/test_education.py`
- `tests/test_experience.py`
- `tests/test_resume.py`
- `conftest.py` - browser/page fixtures
- `pytest.ini` - pytest defaults and report options

## Setup
1. Create and activate a virtual environment.
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Install Playwright browsers:
```bash
playwright install
```

## Run tests
```bash
python -m pytest tests
```

## Reports
- HTML report is generated at `reports/report.html`.
