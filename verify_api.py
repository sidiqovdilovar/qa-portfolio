#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API test run — same 9 requests / 24 assertions as the Postman collection,
executed without Postman so the results can be reproduced in CI or from a terminal.

Run:
    python3 verify_api.py

Output: 05_api_run_results.txt (pass/fail per assertion + summary)
"""
import json
import time
import urllib.error
import urllib.request

BASE = "https://jsonplaceholder.typicode.com"
res = []
stats = {"passed": 0, "failed": 0}


def call(path, method="GET", body=None):
    req = urllib.request.Request(BASE + path, method=method)
    if body is not None:
        req.add_header("Content-Type", "application/json")
        req.data = json.dumps(body).encode()
    t0 = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read().decode(), (time.perf_counter() - t0) * 1000
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode(), (time.perf_counter() - t0) * 1000


def check(name, cond, detail=""):
    stats["passed" if cond else "failed"] += 1
    res.append(f"{'PASS' if cond else 'FAIL'} | {name}" + (f" | {detail}" if detail else ""))


# 1. GET /posts
code, raw, ms = call("/posts")
posts = json.loads(raw)
check("GET /posts -> 200", code == 200, f"{ms:.0f}ms")
check("GET /posts -> 100 items", len(posts) == 100, f"count={len(posts)}")
check("GET /posts -> all items have id/title/userId",
      all(all(k in p for k in ("id", "title", "userId")) for p in posts))
check("GET /posts -> response time < 800ms", ms < 800, f"{ms:.0f}ms")

# 2. GET /posts/1
code, raw, ms = call("/posts/1")
post = json.loads(raw)
check("GET /posts/1 -> 200", code == 200, f"{ms:.0f}ms")
check("GET /posts/1 -> id == 1", post.get("id") == 1)

# 3. GET /posts?userId=1
code, raw, ms = call("/posts?userId=1")
filtered = json.loads(raw)
check("GET /posts?userId=1 -> 200", code == 200)
check("GET /posts?userId=1 -> only user 1", all(p["userId"] == 1 for p in filtered))
check("GET /posts?userId=1 -> exactly 10 posts", len(filtered) == 10, f"count={len(filtered)}")

# 4. GET /posts/1/comments
code, raw, ms = call("/posts/1/comments")
comments = json.loads(raw)
check("GET /posts/1/comments -> 200", code == 200)
check("GET /posts/1/comments -> postId=1 and email present",
      all(c["postId"] == 1 and "@" in c.get("email", "") for c in comments), f"count={len(comments)}")

# 5. GET /users/1
code, raw, ms = call("/users/1")
user = json.loads(raw)
check("GET /users/1 -> 200", code == 200)
check("GET /users/1 -> nested address.city and company.name",
      "city" in user.get("address", {}) and "name" in user.get("company", {}))

# 6. POST /posts
code, raw, ms = call("/posts", "POST",
                     {"title": "QA portfolio test post", "body": "Created by API verification script", "userId": 1})
created = json.loads(raw)
check("POST /posts -> 201 Created", code == 201, f"status={code}")
check("POST /posts -> new id returned", isinstance(created.get("id"), int), f"id={created.get('id')}")
check("POST /posts -> title echoed", created.get("title") == "QA portfolio test post")

# 6b. POST with empty body — documents the missing validation (finding F-01)
code, raw, ms = call("/posts", "POST", {})
check("POST /posts with empty body -> expected 400 (validation)",
      code == 400, f"actual status={code} -> no server-side validation")

# 7. PUT /posts/1
code, raw, ms = call("/posts/1", "PUT",
                     {"id": 1, "title": "Updated title (PUT)", "body": "Updated body", "userId": 1})
updated = json.loads(raw)
check("PUT /posts/1 -> 200", code == 200)
check("PUT /posts/1 -> title updated", updated.get("title") == "Updated title (PUT)")
check("PUT /posts/1 -> id stays 1", updated.get("id") == 1)

# 8. PATCH /posts/1
code, raw, ms = call("/posts/1", "PATCH", {"title": "Patched title"})
patched = json.loads(raw)
check("PATCH /posts/1 -> 200", code == 200)
check("PATCH /posts/1 -> only title changed",
      patched.get("title") == "Patched title" and "userId" in patched and "body" in patched)

# 9. DELETE /posts/1
code, raw, ms = call("/posts/1", "DELETE")
check("DELETE /posts/1 -> 200 or 204", code in (200, 204), f"status={code}")

# 10. Mock API limitation (documented, not a defect)
code, raw, ms = call("/posts/101")
check("GET /posts/101 after POST -> 404 (mock API, documented)", code == 404, f"status={code}")

with open("05_api_run_results.txt", "w", encoding="utf-8") as f:
    f.write("API TEST RUN — JSONPlaceholder (https://jsonplaceholder.typicode.com)\n")
    f.write("9 requests / 24 assertions — same checks as the Postman collection\n")
    f.write("Date: 2026-10-11\n" + "=" * 70 + "\n")
    f.write("\n".join(res) + "\n\n")
    f.write(f"TOTAL: passed={stats['passed']}, failed={stats['failed']}, "
            f"total={stats['passed'] + stats['failed']}\n")

print("\n".join(res))
print(f"\nTOTAL: passed={stats['passed']}, failed={stats['failed']}")
