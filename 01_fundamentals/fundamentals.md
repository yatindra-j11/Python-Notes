# Python Fundamentals — Notes
[Youtube Playlist](https://youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&si=jNjT-0d4BbPFtgqy)

## Phase 1: Python fundamentals 
### Variables
Named references used to store data in memory.
```python
variable_name = value
```

**Naming rules** — must start with a letter/underscore, no spaces, case-sensitive, no reserved keywords.
```python
_name, name1, my_var   # valid
1name, my-var, class   # invalid
```

**Multiple assignment** — assign multiple variables in one line.
```python
a, b, c = 1, 2, 3
x = y = z = 0
```

### Data Types
- **int** — whole numbers.
```python
x = 10
```
- **float** — decimal/floating-point numbers.
```python
x = 10.5
```
- **str** — sequence of characters (text).
```python
x = "text"
```
- **bool** — logical `True`/`False` value.
```python
x = True
```
- **complex** — numbers with real and imaginary parts.
```python
x = 2 + 3j
```
- **None** — represents absence of a value.
```python
x = None
```

### Operators
- **Arithmetic** — perform math operations.
```python
+  -  *  /  //  %  **
```
- **Comparison** — compare two values, return bool.
```python
==  !=  >  <  >=  <=
```
- **Logical** — combine boolean expressions.
```python
and  or  not
```
- **Assignment** — assign/update variable values.
```python
=  +=  -=  *=  /=  //=  %=  **=
```
- **Membership** — test if value exists in a sequence.
```python
in  not in
```
- **Identity** — compare object identity (memory location).
```python
is  is not
```
- **Bitwise** — operate on binary representations.
```python
&  |  ^  ~  <<  >>
```

### Input & Output
- **`input()`** — read input from the user as a string.
```python
input("prompt: ")
```
- **`print()`** — display output to console.
```python
print(value, sep=" ", end="\n")
```
- **Formatting**
  - f-strings — embed expressions inside string literals.
    ```python
    f"{variable}"
    ```
  - `.format()` — insert values into placeholders in a string.
    ```python
    "{}".format(variable)
    ```

### Type Conversion
- **`int()`** — convert to integer.
- **`float()`** — convert to float.
- **`str()`** — convert to string.
- **`bool()`** — convert to boolean.
```python
int(x); float(x); str(x); bool(x)
```

---

## Phase 2: Control Flow

### Conditional Statements
- **if** — executes block if condition is true.
- **elif** — checks another condition if previous ones are false.
- **else** — executes if all above conditions are false.
- **Nested if** — an if statement inside another if.
```python
if condition:
    ...
elif condition:
    ...
else:
    ...
```

### Loops
- **for** — iterates over a sequence.
```python
for item in sequence:
    ...
```
- **while** — repeats block while condition is true.
```python
while condition:
    ...
```
- **break** — exits the loop immediately.
- **continue** — skips to the next iteration.
- **pass** — placeholder that does nothing.
```python
break
continue
pass
```

---

## Phase 3: Data Structures

### Strings
- **Indexing** — access a character by position.
```python
s[i]
```
- **Slicing** — extract a substring/range.
```python
s[start:stop:step]
```
- **String methods** — built-in functions to manipulate strings.
```python
s.upper(); s.lower(); s.strip(); s.split(); s.replace(old, new); s.join(iterable)
```

### Lists
Ordered, mutable collection of items.
```python
lst = [1, 2, 3]
```
- **CRUD operations**
```python
lst.append(x)     # create
lst[i]             # read
lst[i] = x         # update
lst.remove(x)      # delete
```
- **List methods**
```python
lst.append(); lst.extend(); lst.insert(); lst.pop(); lst.sort(); lst.reverse()
```
- **Nested lists** — a list containing other lists.
```python
lst = [[1, 2], [3, 4]]
```

### Tuples
Ordered, immutable collection of items.
```python
t = (1, 2, 3)
```

### Sets
Unordered collection of unique items.
```python
s = {1, 2, 3}
```

### Dictionaries
Unordered collection of key-value pairs.
```python
d = {"key": "value"}
```

### Comprehensions
- **List comprehension** — create a list in a single expression.
```python
[expr for item in iterable if condition]
```
- **Dictionary comprehension** — create a dict in a single expression.
```python
{key_expr: val_expr for item in iterable if condition}
```
- **Set comprehension** — create a set in a single expression.
```python
{expr for item in iterable if condition}
```

---

## Phase 4: Functions

Reusable named blocks of code that perform a task.

- **Defining functions**
```python
def func_name(params):
    ...
```
- **Parameters** — variables listed in a function definition.
```python
def func(param1, param2):
    ...
```
- **Return values** — output sent back from a function.
```python
return value
```
- **Scope** — the region where a variable is accessible (local/global).
```python
global var_name
```
- **Functions as first-class objects** — functions can be assigned, passed, returned like any value.
```python
f = func_name
```
- **Lambda functions** — anonymous, single-expression functions.
```python
lambda args: expression
```
- **Higher order functions** — functions that take/return other functions.
```python
def hof(func, arg):
    return func(arg)
```
- **Recursion** — a function calling itself.
```python
def func():
    func()
```
- **`*args`** — collects extra positional arguments into a tuple.
```python
def func(*args):
    ...
```
- **`**kwargs`** — collects extra keyword arguments into a dict.
```python
def func(**kwargs):
    ...
```
---

## Python Namespace 
A mapping of names (identifiers) to objects — it keeps track of which name refers to which variable, function, or class, so names don't collide with each other. Python maintains multiple namespaces (built-in, global/module-level, local/function-level) and resolves a name using the **LEGB rule** (Local → Enclosing → Global → Built-in).
```python
x = 10          # global namespace

def func():
    x = 20      # local namespace (separate from global x)
    print(x)

print(dir())         # lists names in current namespace
print(globals())     # dict of global namespace
print(locals())      # dict of local namespace
```