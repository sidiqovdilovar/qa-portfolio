# QA Portfolio — Sidiqov Dilovar

![Manual testing](https://img.shields.io/badge/focus-manual%20%26%20API%20testing-blue)
![Playwright](https://img.shields.io/badge/Playwright-10%20UI%20tests%20passing-2EAD33)
![Postman](https://img.shields.io/badge/API%20assertions-23%2F24%20green-FF6C37)
![Defects](https://img.shields.io/badge/defects%20found-4%20verified-red)

**QA Engineer · Manual & API testing · Automation in Python (Playwright, pytest)**
Moscow, Russia · Ready to relocate to **Dubai, UAE** · Open to remote

📧 sidiqovdilovar@gmail.com · 📱 Telegram: [@ProximaCentaurius](https://t.me/ProximaCentaurius)

---

## 👋 About

QA engineer focused on manual and API testing of web applications. This repository is my public QA
portfolio: test documentation, **live-reproduced bug reports**, an API test collection and a UI
automation suite — everything a tester produces on a real project.

Every artifact here was produced and verified by me. All defects in this repository were reproduced
on the live application, and each one has a screenshot and a raw verification log — so any report can
be re-checked by anyone. What makes this portfolio different from a typical junior one is not the
number of files, but that every claim here is **independently verifiable**.

**Key facts:**
- Student of Information Systems and Programming at College of Modern Technologies named after Hero of the Soviet Union M.F. Panov (Moscow), final year
- Preparing for ISTQB Certified Tester Foundation Level (CTFL)
- Languages: Russian (fluent), Tajik (native), English (technical documentation; improving speaking)

---

## 🐞 Verified defects found (4 confirmed)

All reproduced on **2026-10-11** with Chromium (Playwright), screenshots committed:

| ID | Defect | Severity | Evidence |
|---|---|---|---|
| BUG-01 | All 6 products show the same 404 placeholder instead of their own photos | High | [screenshot](screenshots/bug-01_product-images-missing.png) |
| BUG-02 | Sorting options have no effect — all 4 sort modes return the default order | Medium | [screenshot](screenshots/bug-02_sorting-not-working.png) |
| BUG-03 | Checkout: "Last Name" field does not accept input — blocks the purchase | Critical | [screenshot](screenshots/bug-03_checkout-lastname-field.png) |
| BUG-04 | "Add to cart" works for only 3 of 6 products | High | [screenshot](screenshots/bug-04_add-to-cart-buttons.png) |

Full reports with reproduction steps: [`04_bug_reports.md`](04_bug_reports.md) ·
Raw logs: [`screenshots/VERIFICATION_RESULTS.txt`](screenshots/VERIFICATION_RESULTS.txt)

**Retest discipline:** 3 suspected issues did **not** reproduce on retest and were closed honestly
instead of being kept as "bug reports" — see the retest table in the same file. Anyone can file bugs;
knowing which ones to close is the professional part.

---

## 🧪 Projects

### 1. Manual testing of a web application — saucedemo.com

| Artifact | Description |
|---|---|
| [Test plan](01_test-plan.md) | Scope, approach, risks, entry/exit criteria |
| [Checklist (66 items)](02_checklist_webapp.md) | Auth, catalog & search, cart, checkout, profile, UI, cross-browser |
| [Test cases (25)](03_test-cases.md) | 12 detailed + 13 brief cases with steps and expected results |
| [Bug reports (4 verified + retests)](04_bug_reports.md) | Live-reproduced defects with severity, priority and screenshots |
| [Screenshots](screenshots/) | Evidence for every defect, plus clean reference captures |

### 2. REST API testing — JSONPlaceholder

- [Postman collection](postman/qa_portfolio_collection.json) — 9 requests, **24 assertions**
- [Findings](05_api_findings.md) — **23/24 passed**; 1 documented failure (missing server-side
  validation) kept visible on purpose
- [Raw run log](05_api_run_results.txt)

### 3. UI automation — Playwright + pytest (Python)

- [Automation suite](automation/) — **10 UI tests, all passing** (4.9 s on Chromium):
  login (positive, locked account, wrong credentials, empty fields), cart operations,
  end-to-end checkout, checkout validation, cancel flow
- Run: `pip install -r automation/requirements.txt` → `playwright install chromium` → `pytest automation -v`
- The same scripts power the defect verification: `python3 verify_defects.py`

### 4. SQL for QA

- [SQL practice (12 tasks)](06_sql_practice.md) — data-validation queries on a sample e-commerce
  schema: SELECT, JOIN, GROUP BY, subqueries

---

## 🛠 Skills demonstrated in this repository

| Area | Skills |
|---|---|
| Testing | Functional, regression, smoke, UI, API, cross-browser, exploratory |
| Test design | Equivalence partitioning, boundary values, pairwise, state transition |
| Documentation | Test plan, checklist, test cases, bug reports, test summary |
| Defect work | Reproduction, evidence capture, severity vs priority, verification & closing |
| Tools | Jira, Postman, Chrome DevTools, Git/GitHub, Playwright |
| Tech | Python (working level), pytest, SQL, HTML/CSS |
| Process | SDLC/STLC, Agile/Scrum, defect lifecycle |

---

## 📬 Contact

Open to **QA Engineer / QA Tester** roles — remote, or onsite with relocation to the UAE.
Telegram: [@ProximaCentaurius](https://t.me/ProximaCentaurius) · Email: sidiqovdilovar@gmail.com
