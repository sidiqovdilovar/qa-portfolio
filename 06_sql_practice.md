# SQL for QA — 12 practice tasks

**Purpose:** demonstrate the data-validation skills a QA engineer needs: verify that the UI shows exactly what the database stores, find orphan records, check totals.

**Where to run:** [sqliteonline.com](https://sqliteonline.com/) or any PostgreSQL/MySQL instance.

## Schema

```sql
CREATE TABLE customers (
    id         INTEGER PRIMARY KEY,
    full_name  TEXT,
    email      TEXT,
    city       TEXT,
    created_at DATE
);

CREATE TABLE products (
    id     INTEGER PRIMARY KEY,
    title  TEXT,
    price  DECIMAL(10,2)
);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER,
    status      TEXT,           -- 'new' | 'paid' | 'cancelled'
    created_at  DATE
);

CREATE TABLE order_items (
    id         INTEGER PRIMARY KEY,
    order_id   INTEGER,
    product_id INTEGER,
    quantity   INTEGER,
    price      DECIMAL(10,2)
);
```

## Tasks

| # | Task | Query (write yours here) | Result |
|---|---|---|---|
| 1 | All customers from a specific city (e.g. Moscow) | | |
| 2 | Emails of customers registered in the last 30 days | | |
| 3 | Products cheaper than 100, sorted by price ascending | | |
| 4 | Number of orders per customer (only customers with ≥2 orders) | | |
| 5 | Total revenue of paid orders | | |
| 6 | Orders without any items (orphan orders — potential defect) | | |
| 7 | Average order value by status | | |
| 8 | Top 5 most ordered products by total quantity | | |
| 9 | Customers who never placed an order | | |
| 10 | Orders whose stored total differs from the sum of their items (data inconsistency check) | | |
| 11 | Duplicate emails among customers (validation defect) | | |
| 12 | Cancelled orders with paid items (business-logic inconsistency) | | |

## Reference solutions (compare after writing your own)

```sql
-- 1
SELECT * FROM customers WHERE city = 'Moscow';

-- 2
SELECT email FROM customers WHERE created_at >= DATE('now', '-30 days');

-- 3
SELECT title, price FROM products WHERE price < 100 ORDER BY price ASC;

-- 4
SELECT customer_id, COUNT(*) AS orders_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) >= 2;

-- 5
SELECT SUM(oi.quantity * oi.price) AS revenue
FROM order_items oi
JOIN orders o ON o.id = oi.order_id
WHERE o.status = 'paid';

-- 6
SELECT o.* FROM orders o
LEFT JOIN order_items oi ON oi.order_id = o.id
WHERE oi.id IS NULL;

-- 7
SELECT status, AVG(total) AS avg_total FROM (
    SELECT o.id, o.status, SUM(oi.quantity * oi.price) AS total
    FROM orders o JOIN order_items oi ON oi.order_id = o.id
    GROUP BY o.id, o.status
) t
GROUP BY status;

-- 8
SELECT p.title, SUM(oi.quantity) AS total_qty
FROM order_items oi JOIN products p ON p.id = oi.product_id
GROUP BY p.title
ORDER BY total_qty DESC
LIMIT 5;

-- 9
SELECT c.* FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;

-- 10
SELECT o.id, SUM(oi.quantity * oi.price) AS items_total
FROM orders o JOIN order_items oi ON oi.order_id = o.id
GROUP BY o.id
HAVING items_total != (SELECT total FROM (SELECT id, SUM(quantity*price) AS total FROM order_items GROUP BY id) x WHERE x.id = o.id);  -- adapt to your schema

-- 11
SELECT email, COUNT(*) FROM customers GROUP BY email HAVING COUNT(*) > 1;

-- 12
SELECT DISTINCT o.id FROM orders o
JOIN order_items oi ON oi.order_id = o.id
WHERE o.status = 'cancelled' AND oi.quantity > 0;
```

**Why this matters for QA:** tasks 6, 10, 11, 12 are typical checks a tester runs to find defects invisible in the UI — e.g. duplicates caused by a broken double-click guard, or totals that don't match because of a rounding bug.
