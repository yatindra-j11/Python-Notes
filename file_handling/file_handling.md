# Phase 6: File Handling — Notes

### File Modes
Specify how a file is opened using the second argument of `open()`.
```python
"r"    # read (default), error if file doesn't exist
"w"    # write, creates file or overwrites existing content
"a"    # append, creates file or adds to the end
"r+"   # read and write
"b"    # binary mode (combine, e.g. "rb", "wb")
```

### Read Files
Opens an existing file and retrieves its contents as a string (or lines). Using the `with` statement is recommended since it closes the file automatically.
```python
with open("file.txt", "r") as f:
    data = f.read()           # entire content as a string
    line = f.readline()       # one line at a time
    lines = f.readlines()     # all lines as a list

# iterate line by line
with open("file.txt", "r") as f:
    for line in f:
        ...
```

### Write Files
Opens a file for writing; creates it if it doesn't exist and **overwrites** existing content if it does.
```python
with open("file.txt", "w") as f:
    f.write("text")
    f.writelines(list_of_strings)
```

### Append
Opens a file for writing without erasing existing content; new data is added at the end.
```python
with open("file.txt", "a") as f:
    f.write("text")
```

### CSV
Handles comma-separated tabular data using the built-in `csv` module. Use `newline=""` when writing to avoid blank lines on Windows.
```python
import csv

# read
with open("file.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        ...

# write
with open("file.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(row_list)
    writer.writerows(list_of_rows)

# dictionary-based
csv.DictReader(f)
csv.DictWriter(f, fieldnames=[...])
```

### JSON
Handles structured data (stored as key-value pairs, similar to Python dictionaries) using the built-in `json` module.
```python
import json

# read file -> Python object
with open("file.json", "r") as f:
    data = json.load(f)

# write Python object -> file
with open("file.json", "w") as f:
    json.dump(data, f, indent=4)

# string conversion
json.loads(json_string)     # JSON string -> Python object
json.dumps(python_object)   # Python object -> JSON string
```