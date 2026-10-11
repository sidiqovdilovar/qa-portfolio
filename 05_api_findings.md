# API Testing Findings — JSONPlaceholder

**Tool:** Postman (Collection Runner)
**Target:** https://jsonplaceholder.typicode.com
**Collection:** `postman/qa_portfolio_collection.json` (9 requests, 30+ assertions)
**Run date:** [date] · **Postman version:** [ver]

---

## What was tested

| # | Request | Method | Checks |
|---|---|---|---|
| 1 | /posts | GET | 200, returns 100 posts, required fields (`id`, `title`, `userId`), response time < 800 ms |
| 2 | /posts/1 | GET | 200, schema of a single post, `id = 1` |
| 3 | /posts?userId=1 | GET | 200, all returned posts belong to user 1, count = 10 |
| 4 | /posts/1/comments | GET | 200, comments have `email` field in valid format |
| 5 | /users/1 | GET | 200, nested object `address` and `company` present |
| 6 | /posts | POST | 201, server returns the created object with new `id = 101`, echo of sent `title` |
| 7 | /posts/1 | PUT | 200, changed field returned, other fields unchanged |
| 8 | /posts/1 | PATCH | 200, single field updated, rest intact |
| 9 | /posts/1 | DELETE | 200, response body empty or `{}` |

## Test run result

- **Requests executed:** 9
- **Assertions passed:** [30] / 30
- **Failed:** [0]
- **Screenshot of the run:** `screenshots/api-collection-run.png`

## Observations / findings

1. **Success status codes are correct** for all CRUD operations (200/201) — documented and asserted in the collection.
2. **POST does not persist data** (reference API is read-only in practice): after creating post `id = 101`, `GET /posts/101` returns 404. Behavior documented as *expected for this test API, not a defect* — recorded to demonstrate "expected vs actual" analysis.
3. **No server-side validation on POST**: sending `title` as a number or an empty body still returns 201. **Would be a defect in a production API** (missing 400 Bad Request). Documented in the table below.
4. **Response time** of all requests < 800 ms; largest is `/posts` (~[300] ms) — acceptable for a test environment.

## Findings table

| # | Description | Expected | Actual | Severity | Verdict |
|---|---|---|---|---|---|
| F-01 | POST /posts with empty body | 400 Bad Request with validation error | 201 Created, empty post created | Medium | Would be a defect in production |
| F-02 | GET /posts/101 after creating it | 200 with created post | 404 Not Found | — | Expected for a mock API |
| F-03 | POST /posts with `title` as number | 400 Bad Request | 201 Created | Low | Would be a defect in production |

## Conclusion

The collection verifies the main REST practices: status codes, response body structure, query parameters, required fields and response time. The exercise also demonstrates the difference between *defects* and *expected behavior of a mock service* — an important QA skill: the same response can be a bug in one system and acceptable in another.
