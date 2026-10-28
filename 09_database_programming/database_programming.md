# Phase 11: Database Programming — Notes

### Beginner Introduction
**Database** — an organized, persistent store of data that outlives your program. Python talks to a database through a *driver* library.

**Two main families**
- **SQL (relational)** — data in tables with rows and columns, queried using SQL (SQLite, MySQL, PostgreSQL).
- **NoSQL (document)** — data as flexible JSON-like documents grouped in collections (MongoDB).

**Typical workflow for SQL databases**
```
connect -> create cursor -> execute query -> commit (if data changed) -> fetch results -> close
```

**Always use parameterized queries** — never build SQL by pasting user input into a string; it allows *SQL injection* attacks.
```python
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))     # safe
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")        # unsafe
```

---

## SQLite
A lightweight, file-based relational database that needs no server. The `sqlite3` module is built into Python, which makes it ideal for learning, small apps, and prototypes.

### Connect
Opens (or creates) a database file and returns a connection; a cursor executes queries through it.
```python
import sqlite3

conn = sqlite3.connect("database.db")      # file database
conn = sqlite3.connect(":memory:")         # temporary in-memory database
cursor = conn.cursor()
...
conn.close()

# auto-commit/rollback, but does NOT close the connection
with conn:
    ...
```

### Create Tables
```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS table_name (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        column1 TEXT NOT NULL,
        column2 INTEGER DEFAULT 0,
        column3 REAL UNIQUE
    )
""")
conn.commit()
```
**Common SQLite types**
```
INTEGER   TEXT   REAL   BLOB   NULL
```

### CRUD
```python
# Create
cursor.execute("INSERT INTO table_name (col1, col2) VALUES (?, ?)", (v1, v2))
cursor.executemany("INSERT INTO table_name (col1, col2) VALUES (?, ?)", list_of_tuples)

# Read
cursor.execute("SELECT * FROM table_name WHERE col1 = ?", (value,))
cursor.fetchone()          # one row (tuple) or None
cursor.fetchall()          # list of all rows
cursor.fetchmany(n)        # next n rows

# Update
cursor.execute("UPDATE table_name SET col1 = ? WHERE id = ?", (value, id))

# Delete
cursor.execute("DELETE FROM table_name WHERE id = ?", (id,))

conn.commit()              # required to save Create/Update/Delete
cursor.rowcount            # rows affected
cursor.lastrowid           # id of last inserted row
```
**Access rows by column name**
```python
conn.row_factory = sqlite3.Row
row["column_name"]
```

### Transactions
A group of operations treated as a single unit: either **all** succeed (`commit`) or **none** apply (`rollback`). Follows **ACID** (Atomicity, Consistency, Isolation, Durability).
```python
try:
    cursor.execute(...)
    cursor.execute(...)
    conn.commit()          # save all changes
except sqlite3.Error:
    conn.rollback()        # undo all changes since last commit
finally:
    conn.close()

# context manager shortcut: commits on success, rolls back on exception
with conn:
    conn.execute(...)
    conn.execute(...)
```

---

## MySQL / PostgreSQL
Full client-server relational databases: the database runs as a separate server, so you connect with host, credentials, and a database name. The workflow and cursor API are very similar to `sqlite3` (Python's DB-API standard).

### Database Connectivity
**Install a driver**
```bash
pip install mysql-connector-python    # MySQL (official)
pip install pymysql                   # MySQL (alternative)
pip install psycopg2-binary           # PostgreSQL
pip install psycopg[binary]           # PostgreSQL (psycopg 3, newer)
```
**MySQL**
```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="db_name",
    port=3306
)
cursor = conn.cursor()
```
**PostgreSQL**
```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="username",
    password="password",
    dbname="db_name",
    port=5432
)
cursor = conn.cursor()
```
**Close**
```python
cursor.close()
conn.close()
```
**Keep credentials out of code**
```python
import os
password = os.environ.get("DB_PASSWORD")
```

### SQL with Python
Running SQL statements through the cursor. The main difference from SQLite is the **placeholder style**.
```
SQLite                 ?
MySQL / PostgreSQL     %s     (used for all data types, not just strings)
```
```python
# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS table_name (
        id SERIAL PRIMARY KEY,         -- PostgreSQL
        -- id INT AUTO_INCREMENT PRIMARY KEY,   -- MySQL
        column1 VARCHAR(100) NOT NULL
    )
""")

# Insert
cursor.execute("INSERT INTO table_name (col1) VALUES (%s)", (value,))
cursor.executemany("INSERT INTO table_name (col1) VALUES (%s)", list_of_tuples)

# Select
cursor.execute("SELECT * FROM table_name WHERE col1 = %s", (value,))
rows = cursor.fetchall()

# Update / Delete
cursor.execute("UPDATE table_name SET col1 = %s WHERE id = %s", (value, id))
cursor.execute("DELETE FROM table_name WHERE id = %s", (id,))

conn.commit()
conn.rollback()
```
**Get rows as dictionaries**
```python
conn.cursor(dictionary=True)                              # MySQL
from psycopg2.extras import RealDictCursor
conn.cursor(cursor_factory=RealDictCursor)                # PostgreSQL
```
**Context managers (PostgreSQL / psycopg2)**
```python
with conn:                      # transaction: commit/rollback automatically
    with conn.cursor() as cursor:
        cursor.execute(...)
```
**Connection pooling and ORMs (next step)**
```python
# SQLAlchemy — write Python classes instead of raw SQL
from sqlalchemy import create_engine
engine = create_engine("postgresql://user:password@host/db_name")
```

---

## MongoDB
A NoSQL document database storing data as JSON-like documents (BSON) inside **collections**, which sit inside **databases**. No fixed schema: documents in the same collection can have different fields.

**SQL ↔ MongoDB terms**
```
Database   ->  Database
Table      ->  Collection
Row        ->  Document
Column     ->  Field
```

### PyMongo
The official Python driver for MongoDB.
```bash
pip install pymongo
```
```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
client = MongoClient("mongodb+srv://user:password@cluster.mongodb.net/")   # Atlas (cloud)

db = client["database_name"]            # created lazily on first insert
collection = db["collection_name"]

client.list_database_names()
db.list_collection_names()
client.close()
```
**Documents and `_id`** — every document gets a unique `_id` (an `ObjectId`) automatically.
```python
from bson.objectid import ObjectId
{"_id": ObjectId("...")}
```

### CRUD
```python
# Create
collection.insert_one({"field": "value"})
collection.insert_many([{...}, {...}])
result.inserted_id; result.inserted_ids

# Read
collection.find_one({"field": "value"})
collection.find({"field": "value"})                  # returns a cursor; loop over it
collection.find({}, {"field": 1, "_id": 0})          # projection (choose fields)
collection.find().sort("field", 1).limit(n).skip(n)  # 1 = ascending, -1 = descending
collection.count_documents({"field": "value"})

# Update
collection.update_one({"field": "value"}, {"$set": {"field": "new"}})
collection.update_many({filter}, {"$set": {...}})
collection.replace_one({filter}, {new_document})

# Delete
collection.delete_one({"field": "value"})
collection.delete_many({filter})

# result info
result.matched_count; result.modified_count; result.deleted_count
```
**Query operators**
```python
{"age": {"$gt": 18}}                      # $gt  $gte  $lt  $lte  $ne  $eq
{"city": {"$in": ["A", "B"]}}             # $in  $nin
{"$and": [{...}, {...}]}                  # $and  $or  $not  $nor
{"field": {"$exists": True}}
{"name": {"$regex": "^A"}}
```
**Update operators**
```python
{"$set": {"field": value}}                # set a field
{"$unset": {"field": ""}}                 # remove a field
{"$inc": {"field": 1}}                    # increment
{"$push": {"array_field": value}}         # add to array
{"$pull": {"array_field": value}}         # remove from array
```

### Aggregation Basics
A **pipeline** of stages where each stage transforms the documents and passes the result to the next, used for grouping, filtering, and calculating summaries (similar to `GROUP BY` in SQL).
```python
pipeline = [
    {"$match": {"field": "value"}},                                     # filter
    {"$group": {"_id": "$group_field", "total": {"$sum": "$amount"}}},  # group + calculate
    {"$sort": {"total": -1}},                                           # sort
    {"$limit": 5}                                                       # limit
]
results = collection.aggregate(pipeline)
for doc in results:
    ...
```
**Common stages**
```
$match     filter documents (like WHERE)
$group     group by a field and compute values
$sort      order documents
$project   include/exclude/reshape fields
$limit     keep first n documents
$skip      skip first n documents
$unwind    split an array field into separate documents
$lookup    join with another collection
$count     count documents
```
**Group accumulators**
```
$sum   $avg   $min   $max   $first   $last   $push   $addToSet
```
**Field references** — a `$` prefix inside a pipeline means "the value of this field".
```python
"$field_name"
```