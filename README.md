# Playwright Portfolio Automation (Python)

UI automation for a personal portfolio site using Playwright and pytest. The suite navigates the Home page, then validates Projects navigation and key headings using a Page Object Model.

**Target site**
- `https://carlosng07.vercel.app/`

**Key tooling**
- Playwright (sync API)
- pytest + pytest-playwright
- pytest-html (HTML reports)

**Project structure**
- `pages/HomePage.py` - Page Object Model for Home navigation
- `pages/ProjectsPage.py` - Page Object Model for Projects navigation and assertions
- `tests/test_home.py` - Home/Projects navigation tests (direct + POM)
- `tests/test_project.py` - Projects page assertions using the POM
- `conftest.py` - Playwright fixtures (browser/page)
- `pytest.ini` - pytest defaults and report config
- `reports/` - generated HTML reports

**Setup**
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Playwright browsers:
   ```bash
   playwright install
   ```

**Run tests**
- Default (uses `pytest.ini` addopts):
  ```bash
  pytest
  ```
- Single test:
  ```bash
  pytest tests/test_home.py -k test_home_page_object
  ```
- Projects tests:
  ```bash
  pytest tests/test_project.py
  ```

**Reports**
- HTML report is generated at `reports/report.html` (configured in `pytest.ini`).

**Current runtime configuration**
- `pytest.ini` sets:
  - `--headed --browser chromium --slowmo=200`
  - `--html=reports/report.html --self-contained-html`
- `conftest.py` launches Chromium via Playwright sync API with:
  - `headless=False`
  - `slow_mo=500`

If you want one source of truth for runtime options, consider aligning `pytest.ini` and `conftest.py` values.
