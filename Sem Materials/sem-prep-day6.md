## **Material on `pymysql` (with Code Snippets)**

### **Introduction**

`pymysql` is a Python library that enables seamless interaction with MySQL or MariaDB databases. It is a **pure-Python implementation**, requiring no external MySQL client. `pymysql` is widely used in data analysis, web applications, and automated database operations because it allows Python code to connect, query, and manipulate relational databases efficiently.

---

### **Core Features**

#### 1. **Database Connection**

To work with MySQL, you first establish a connection:

```python
import pymysql

conn = pymysql.connect(
    host="localhost",
    user="rootuser",
    passwd="rootuser",
    db="mydatabase",
    autocommit=True
)
```

- `autocommit=True` ensures changes are saved automatically.
- Always close the connection after use:

```python
conn.close()
```

---

#### 2. **Executing Queries**

A **cursor** object executes SQL statements:

```python
cursor = conn.cursor()
cursor.execute("SELECT * FROM Orders WHERE status='completed';")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
```

- Use `DictCursor` to get results as dictionaries:

```python
cursor = conn.cursor(pymysql.cursors.DictCursor)
```

---

#### 3. **Inserting Data Safely**

Parameterized queries prevent SQL injection:

```python
insert_query = "INSERT INTO Orders (id, customer, total) VALUES (%s, %s, %s)"
cursor.execute(insert_query, (101, "Alice", 250.0))
```

---

#### 4. **Transactions**

Control database changes with `commit()` and `rollback()`:

```python
try:
    cursor.execute("UPDATE Orders SET status='completed' WHERE id=101")
    conn.commit()  # save changes
except pymysql.MySQLError:
    conn.rollback()  # undo changes on error
```

---

### **Common Use Cases**

- Fetching data for reporting or analytics.
- Transforming data in Python (e.g., using Pandas) and saving it back to MySQL.
- Automating database table creation, insertion, or updates.

---

### **Advantages**

- Pure Python → easy installation and cross-platform.
- Works well with data libraries like **Pandas** and **NumPy**.
- Supports context managers for cleaner code:

```python
with conn.cursor() as cursor:
    cursor.execute("SELECT * FROM Orders;")
    print(cursor.fetchall())
```

---

### **Conclusion**

`pymysql` provides a **flexible, secure, and Pythonic** way to interact with MySQL databases. Its ability to fetch, transform, and store data efficiently makes it invaluable for Python developers in data science, web development, and database automation.

## **Material on SQLite (with Code Snippets)**

### **Introduction**

SQLite is a lightweight, serverless, self-contained **relational database engine** that stores data in a single file on disk. Unlike traditional databases like MySQL, SQLite does not require a server process. It is ideal for small to medium applications, embedded systems, and rapid prototyping. Python provides built-in support for SQLite through the `sqlite3` module.

---

### **Core Features**

#### 1. **Database Connection**

Connecting to an SQLite database is simple:

```python
import sqlite3

# Connect to a file-based database (creates file if not exists)
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
```

- No username, password, or server needed.
- The database exists as a **single `.db` file**.

---

#### 2. **Creating Tables**

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY,
    customer TEXT,
    total REAL,
    status TEXT
)
""")
conn.commit()
```

---

#### 3. **Inserting Data**

```python
cursor.execute("INSERT INTO Orders (customer, total, status) VALUES (?, ?, ?)",
               ("Alice", 250.0, "completed"))
conn.commit()
```

- SQLite uses `?` placeholders for parameters instead of `%s`.

---

#### 4. **Fetching Data**

```python
cursor.execute("SELECT * FROM Orders WHERE status='completed'")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

---

#### 5. **Closing the Connection**

```python
cursor.close()
conn.close()
```

- Always close connections to ensure data is written to disk.

---

### **Common Use Cases**

- Embedded applications (desktop/mobile apps)
- Prototyping and testing before migrating to larger databases
- Lightweight data storage for scripts or small websites

---

### **Advantages**

- Serverless → no setup or configuration
- Cross-platform and file-based
- Built into Python → no extra library needed
- Lightweight and fast for small datasets

---

## **Key Differences: SQLite vs MySQL (`pymysql`)**

| Feature                 | SQLite                                    | MySQL (`pymysql`)                           |
| ----------------------- | ----------------------------------------- | ------------------------------------------- |
| **Server**              | Serverless, file-based                    | Client-server architecture                  |
| **Setup**               | Minimal, no installation needed           | Requires MySQL server setup                 |
| **Python Library**      | `sqlite3` (built-in)                      | `pymysql` (external library)                |
| **User Authentication** | None (file-based access)                  | Requires username/password                  |
| **Concurrency**         | Limited (single-writer, multiple readers) | High concurrency, supports multiple writers |
| **Best For**            | Small apps, prototyping, embedded systems | Large-scale apps, multi-user databases      |
| **Data Storage**        | Single `.db` file                         | Server-managed storage, multiple databases  |
| **Transactions**        | Supported                                 | Supported, often with explicit commit       |

**Summary:**

- SQLite is great for **small-scale or embedded applications** where simplicity and portability are priorities.
- MySQL via `pymysql` is better for **production-level, multi-user, concurrent applications** that need robust database management and security.
