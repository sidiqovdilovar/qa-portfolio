# API Testing Findings — JSONPlaceholder

**Target:** https://jsonplaceholder.typicode.com
**Collection:** [`postman/qa_portfolio_collection.json`](postman/qa_portfolio_collection.json) — 9 requests, 24 assertions
**Run date:** 2026-10-11 · **Result: 23 passed / 1 failed** (the failure is a documented finding, not a broken test)
**Raw log:** [`05_api_run_results.txt`](05_api_run_results.txt)

---

## What was tested

| # | Request | Checks performed | Result |
|---|---|---|---|
| 1 | `GET /posts` | 200 · 100 items · required fields (`id`, `title`, `userId`) · response time < 800 ms | ✅ 67 ms |
| 2 | `GET /posts/1` | 200 · `id = 1` · `Content-Type: application/json` | ✅ 33 ms |
| 3 | `GET /posts?userId=1` | 200 · only user 1 · exactly 10 posts | ✅ |
| 4 | `GET /posts/1/comments` | 200 · `postId = 1` · valid email format | ✅ 5 comments |
| 5 | `GET /users/1` | 200 · nested `address.city` and `company.name` present | ✅ |
| 6 | `POST /posts` | 201 Created · server returns new `id` · title echoed | ✅ `id = 101` |
| 7 | `PUT /posts/1` | 200 · title updated · `id` unchanged | ✅ |
| 8 | `PATCH /posts/1` | 200 · only `title` changed, other fields intact | ✅ |
| 9 | `DELETE /posts/1` | 200/204 · empty body | ✅ 200 |

## Findings

### F-01 — No server-side validation on POST (medium)

| | |
|---|---|
| **Request** | `POST /posts` with an **empty JSON body** `{}` |
| **Expected** | `400 Bad Request` with a validation error |
| **Actual** | `201 Created` — the API accepts and "creates" a record with no data |
| **Severity** | Medium · **would be a defect in a production API** |
| **Assertion status** | The test **fails by design** — it documents the gap rather than hiding it |

The same behaviour occurs when `title` is sent as a number instead of a string: the API still
returns `201`. A production service would be expected to reject non-conforming payloads.

### F-02 — Data is not persisted (expected for this mock API, documented)

After `POST /posts` returns `201` with `id = 101`, a follow-up `GET /posts/101` returns `404`.
This is **expected behaviour of a read-only mock service** — not a defect. It is recorded because
the distinction between *"a defect"* and *"expected behaviour of the environment"* is exactly what
a QA engineer is expected to make; asserting the wrong expectation would produce a false bug report.

### F-03 — Response times (observation)

All requests responded in 33–67 ms; the heaviest is `GET /posts` (100 items, 67 ms) — well within
the 800 ms threshold asserted in the collection.

---

## How the collection works

Each request contains a `test` script with assertions; run it to get a pass/fail report:

- **Postman:** import the collection → **Collection Runner** → Run
- **Script equivalent:** `python3 verify_api.py` (produces [`05_api_run_results.txt`](05_api_run_results.txt))

### Example assertion (request 3 — filtering)

```javascript
pm.test('All returned posts belong to userId 1', function () {
    pm.response.json().forEach(function (post) {
        pm.expect(post.userId).to.eql(1);
    });
});
pm.test('User 1 has exactly 10 posts', function () {
    pm.expect(pm.response.json().length).to.eql(10);
});
```

## Conclusion

The suite verifies the core REST practices: status codes, response schema, query-parameter
filtering, required fields and response time. It also demonstrates the difference between a
**defect** (F-01), an **expected limitation of the environment** (F-02) and a **clean pass** (F-03) —
the judgement call that separates a tester who files noise from one who files verified bugs.
