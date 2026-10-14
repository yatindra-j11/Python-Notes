# Phase 10: Built-in Libraries — Notes

### `os`
Provides functions to interact with the operating system: working with directories, environment variables, and file paths.
```python
import os

os.getcwd()                    # current working directory
os.chdir(path)                 # change directory
os.listdir(path)               # list directory contents
os.mkdir(path)                 # create a directory
os.makedirs(path, exist_ok=True)  # create nested directories
os.remove(path)                # delete a file
os.rmdir(path)                 # delete an empty directory
os.rename(old, new)            # rename file/directory
os.environ.get("VAR")          # read environment variable
os.path.join(a, b)             # build a path
os.path.exists(path)           # check if path exists
os.path.isfile(path)           # is a file
os.path.isdir(path)            # is a directory
os.path.splitext(path)         # split name and extension
```

### `pathlib`
Object-oriented, cross-platform way to handle filesystem paths, as an alternative to `os.path`.
```python
from pathlib import Path

p = Path("folder/file.txt")
p.exists()
p.is_file(); p.is_dir()
p.name; p.stem; p.suffix; p.parent
p.read_text(); p.write_text("text")
p.mkdir(parents=True, exist_ok=True)
p.iterdir()                    # iterate directory contents
p.glob("*.txt")                # pattern search
Path.cwd(); Path.home()
p / "subfolder" / "file.txt"   # join paths
```

### `shutil`
High-level file operations such as copying, moving, and deleting files and entire directory trees.
```python
import shutil

shutil.copy(src, dst)            # copy a file
shutil.copytree(src, dst)        # copy a directory
shutil.move(src, dst)            # move file/directory
shutil.rmtree(path)              # delete a directory and its contents
shutil.make_archive(name, "zip", root_dir)   # create archive
```

### `datetime`
Handles dates, times, and time differences, including formatting and parsing.
```python
from datetime import datetime, date, time, timedelta

datetime.now()
date.today()
datetime(year, month, day, hour, minute, second)
dt.strftime("%Y-%m-%d %H:%M:%S")          # datetime -> string
datetime.strptime(string, "%Y-%m-%d")     # string -> datetime
dt + timedelta(days=1, hours=2)           # date arithmetic
dt.year; dt.month; dt.day; dt.weekday()
```

### `math`
Provides mathematical functions and constants for numeric calculations.
```python
import math

math.sqrt(x); math.pow(x, y)
math.ceil(x); math.floor(x)
math.factorial(n); math.gcd(a, b)
math.log(x, base); math.log10(x)
math.sin(x); math.cos(x); math.tan(x)
math.pi; math.e; math.inf
```

### `random`
Generates pseudo-random numbers and makes random selections.
```python
import random

random.random()                  # float in [0.0, 1.0)
random.randint(a, b)             # int between a and b (inclusive)
random.uniform(a, b)             # float between a and b
random.choice(sequence)          # one random item
random.choices(sequence, k=n)    # n items with replacement
random.sample(sequence, k=n)     # n unique items
random.shuffle(list)             # shuffle in place
random.seed(value)               # reproducible results
```

### `statistics`
Basic statistical calculations on numeric data.
```python
import statistics

statistics.mean(data)
statistics.median(data)
statistics.mode(data)
statistics.stdev(data)           # sample standard deviation
statistics.variance(data)
```

### `collections`
Specialized container datatypes that extend built-in lists, dicts, and tuples.
```python
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

Counter(iterable)                          # count occurrences
defaultdict(default_factory)               # dict with default values
deque(iterable)                            # double-ended queue
deque.append(); deque.appendleft(); deque.pop(); deque.popleft()
namedtuple("Name", ["field1", "field2"])   # tuple with named fields
```

### `itertools`
Tools for creating efficient iterators for looping, combining, and grouping data.
```python
import itertools

itertools.count(start, step)
itertools.cycle(iterable)
itertools.repeat(value, times)
itertools.chain(iter1, iter2)
itertools.permutations(iterable, r)
itertools.combinations(iterable, r)
itertools.product(iter1, iter2)
itertools.groupby(iterable, key)
itertools.islice(iterable, start, stop, step)
itertools.accumulate(iterable)
```

### `functools`
Higher-order functions and utilities for working with and modifying other functions.
```python
from functools import reduce, partial, lru_cache, wraps

reduce(function, iterable, initial)    # cumulative reduction
partial(function, *args, **kwargs)     # fix some arguments
@lru_cache(maxsize=None)               # memoization decorator
@wraps(func)                           # preserve function metadata
```

### `re` (Regular Expressions)
Pattern matching and text manipulation using regular expressions.
```python
import re

re.match(pattern, string)              # match at start of string
re.search(pattern, string)             # first match anywhere
re.findall(pattern, string)            # list of all matches
re.finditer(pattern, string)           # iterator of match objects
re.sub(pattern, replacement, string)   # replace matches
re.split(pattern, string)              # split by pattern
re.compile(pattern)                    # precompile a pattern

# match object
m.group(); m.groups(); m.start(); m.end()
```
**Common pattern syntax:**
```python
.    # any character          \d   # digit             \w   # word character
^    # start of string        \s   # whitespace        \b   # word boundary
$    # end of string          *    # 0 or more         +    # 1 or more
?    # 0 or 1                 {n,m}  # n to m times     []   # character set
|    # OR                     ()   # group              \D \W \S  # negations
```

### `json`
Reads and writes JSON (JavaScript Object Notation) data, converting between JSON and Python objects.
```python
import json

json.load(file)                  # file -> Python object
json.dump(obj, file, indent=4)   # Python object -> file
json.loads(json_string)          # string -> Python object
json.dumps(obj)                  # Python object -> string
```

### `csv`
Reads and writes CSV (comma-separated values) files.
```python
import csv

csv.reader(file)
csv.writer(file)
csv.DictReader(file)
csv.DictWriter(file, fieldnames=[...])
writer.writerow(row); writer.writerows(rows)
```

### `logging`
A flexible system for recording messages about program events, with severity levels, output destinations, and formatting, preferred over `print()` for debugging and monitoring.
```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log"
)

logging.debug("message")
logging.info("message")
logging.warning("message")
logging.error("message")
logging.critical("message")

# named logger
logger = logging.getLogger(__name__)
```
**Levels (low → high):**
```python
DEBUG < INFO < WARNING < ERROR < CRITICAL
```