# QA Portfolio — Sidiqov Dilovar

![Discipline](https://img.shields.io/badge/focus-manual%20%26%20API%20testing-blue)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-UI%20tests-2EAD33?logo=playwright&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-collection-FF6C37?logo=postman&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-data%20validation-4479A1?logo=postgresql&logoColor=white)

**QA Engineer · Manual & API testing · Automation in Python (Playwright, pytest)**
Moscow, Russia · Ready to relocate to **Dubai, UAE** · Open to remote

📧 sidiqovdilovar@gmail.com · 📱 Telegram: [@ProximaCentaurius](https://t.me/ProximaCentaurius)

---

## 👋 About

QA engineer focused on manual and API testing of web applications. This repository is my public QA portfolio: test documentation, bug reports, an API test collection and a UI automation suite — everything a tester produces on a real project.

Every artifact here was produced by me. I know exactly how each checklist item, test case and bug report was created and can explain any of them in an interview — and reproduce any defect on request.

**Key facts:**
- Student of Information Systems and Programming at College of Modern Technologies named after Hero of the Soviet Union M.F. Panov (Moscow), final year
- Preparing for ISTQB Certified Tester Foundation Level (CTFL)
- Languages: Russian (fluent), Tajik (native), English (technical documentation; improving speaking)

---

## 🧪 Projects

### 1. Manual testing of a web application — saucedemo.com

| Artifact | Description |
|---|---|
| [Test plan](01_test-plan.md) | Scope, approach, risks, entry/exit criteria |
| [Checklist (66 items)](02_checklist_webapp.md) | Auth, catalog & search, cart, checkout, profile, UI, cross-browser |
| [Test cases (25)](03_test-cases.md) | 12 detailed + 13 brief cases with steps and expected results |
| [Bug reports (8)](04_bug_reports.md) | Reproduced and documented defects with severity & priority |
| [Screenshots](screenshots/) | Evidence for bug reports and test runs |

### 2. REST API testing with Postman — JSONPlaceholder API

- [Postman collection](postman/qa_portfolio_collection.json) — 9 requests with automated checks:
  status codes, response bodies, required fields, response time
- [API findings](05_api_findings.md) — results of the test run and documented issues

**How to reproduce:** import the collection into Postman → Collection Runner → Run.
The exported run report is in [05_api_findings.md](05_api_findings.md).

### 3. UI automation — Playwright + pytest (Python)

- [Automation suite](automation/) — 7 UI tests for [saucedemo.com](https://www.saucedemo.com):
  login (positive, locked account, wrong credentials), cart operations, end-to-end checkout
- Run: `pip install -r automation/requirements.txt` → `playwright install chromium` → `pytest automation -v`

### 4. SQL for QA

- [SQL practice (12 tasks)](06_sql_practice.md) — data validation queries on a sample e-commerce schema:
  SELECT, JOIN, GROUP BY, subqueries

---

## 🛠 Skills demonstrated in this repository

| Area | Skills |
|---|---|
| Testing | Functional, regression, smoke, UI, API, cross-browser, exploratory |
| Test design | Equivalence partitioning, boundary values, pairwise, state transition |
| Documentation | Test plan, checklist, test cases, bug reports, test summary |
| Tools | Jira, Postman, Chrome DevTools, Git/GitHub, [TestRail] |
| Tech | Python (working level), Playwright, pytest, SQL, HTML/CSS |
| Process | SDLC/STLC, Agile/Scrum, defect lifecycle, severity vs priority |

---

## 📄 CV

Full CV is available on request — or download it here: [add `cv/QA_Engineer_EN.pdf` to the repository]

---

## 📬 Contact

Open to **QA Engineer / QA Tester** roles, remote or with relocation to the UAE.
Telegram: [@ProximaCentaurius](https://t.me/ProximaCentaurius) · Email: sidiqovdilovar@gmail.com
