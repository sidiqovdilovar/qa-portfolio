# Screenshots

Evidence for the artifacts in this portfolio. Files are named by artifact ID.

## What to put here

| File name | What it shows |
|---|---|
| `bug-01_finish-button.png` | Screenshot for BUG-01 reproduction |
| `bug-02_product-images.png` | Screenshot for BUG-02 (wrong product images) |
| `bug-03_sorting.png` | Screenshot for BUG-03 (sorting not working) |
| ... | One screenshot per bug report in `04_bug_reports.md` |
| `checklist-run.png` | Executed checklist with statuses |
| `test-cases-run.png` | Executed test cases with Passed/Failed |
| `api-collection-run.png` | Postman Collection Runner — all tests green |
| `automation-run.png` | Terminal screenshot: `pytest -v` report |
| `sql-results.png` | Query results in SQL editor |

## How to take good screenshots

1. **Full page** where the defect is visible, not a crop of one element
2. Add a **red arrow or circle** marking the problem (use any screenshot tool)
3. Include the **URL bar** — proves where the defect was found
4. Keep the browser window at a normal size, no zoom tricks

## Commit them

GitHub → Add file → Upload files → drag the images → Commit changes.
Then reference them in `04_bug_reports.md` like:
`![BUG-01](screenshots/bug-01_finish-button.png)`
