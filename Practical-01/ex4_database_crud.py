import os
import sqlite3

os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/app.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# Drop old single-table lab table if it exists
cursor.execute("DROP TABLE IF EXISTS users")

# ---------- 1. CREATE: two related tables ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    salary REAL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
""")

# Clean previous rows for repeatable runs
cursor.execute("DELETE FROM employees")
cursor.execute("DELETE FROM departments")
cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('employees', 'departments')")

# ---------- 2. INSERT departments ----------
cursor.executemany("INSERT INTO departments (name) VALUES (?)", [
    ("Engineering",),
    ("HR",),
    ("Finance",),
])
conn.commit()

dept_ids = {
    row["name"]: row["id"]
    for row in cursor.execute("SELECT id, name FROM departments")
}

# ---------- 3. INSERT employees (linked to departments) ----------
cursor.executemany(
    "INSERT INTO employees (name, salary, department_id) VALUES (?, ?, ?)",
    [
        ("Alice", 75000, dept_ids["Engineering"]),
        ("Bob", 50000, dept_ids["HR"]),
        ("Charlie", 90000, dept_ids["Finance"]),
    ],
)
conn.commit()
print("[CREATE] Seeded departments and employees.")

# ---------- 4. READ with JOIN ----------
print("\n--- [READ] Employees with Department (JOIN) ---")
for row in cursor.execute("""
    SELECT e.id, e.name, e.salary, d.name AS department
    FROM employees e
    LEFT JOIN departments d ON e.department_id = d.id
    ORDER BY e.id
"""):
    print(f"ID: {row['id']} | Name: {row['name']:<10} | "
          f"Salary: ${row['salary']:,.2f} | Dept: {row['department']}")

# ---------- 5. UPDATE ----------
cursor.execute("UPDATE employees SET salary = ? WHERE name = ?", (82000, "Bob"))
conn.commit()
print("\n[UPDATE] Updated Bob's salary to $82,000.")

# ---------- 6. DELETE ----------
cursor.execute("DELETE FROM employees WHERE name = ?", ("Charlie",))
conn.commit()
print("[DELETE] Deleted Charlie.")

# ---------- 7. Final read ----------
print("\n--- Final Records ---")
for row in cursor.execute("""
    SELECT e.id, e.name, e.salary, d.name AS department
    FROM employees e
    LEFT JOIN departments d ON e.department_id = d.id
    ORDER BY e.id
"""):
    print(f"ID: {row['id']} | Name: {row['name']:<10} | "
          f"Salary: ${row['salary']:,.2f} | Dept: {row['department']}")

conn.close()