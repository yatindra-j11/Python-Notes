# Phase 9: Advanced Python — Notes

### Iterators
An object that produces values one at a time and remembers its position. It implements `__iter__()` (returns the iterator itself) and `__next__()` (returns the next value, raising `StopIteration` when exhausted). Any object you can loop over with `for` is an *iterable*; calling `iter()` on it gives an iterator.
```python
it = iter(iterable)
next(it)

class IteratorName:
    def __iter__(self):
        return self
    def __next__(self):
        ...
        raise StopIteration
```

### Generators
Special functions that produce values lazily using `yield`, pausing and resuming their state between calls instead of building the whole result in memory. They automatically implement the iterator protocol.
```python
def generator_name(params):
    yield value

gen = generator_name()
next(gen)

# generator expression
(expr for item in iterable if condition)
```
- `yield from` — delegates to another iterable/generator.
```python
yield from iterable
```

### Closures
An inner function that remembers and accesses variables from its enclosing function's scope, even after the outer function has finished executing. `nonlocal` lets the inner function modify those variables.
```python
def outer(param):
    def inner():
        return param
    return inner

# modifying enclosing variable
nonlocal var_name
```

### Decorators
A function that takes another function, adds extra behavior around it, and returns the modified function, without changing the original code. Applied using the `@` syntax, which is shorthand for `func = decorator(func)`.
```python
def decorator_name(func):
    def wrapper(*args, **kwargs):
        ...
        result = func(*args, **kwargs)
        ...
        return result
    return wrapper

@decorator_name
def function_name():
    ...

# preserve original function metadata
from functools import wraps
@wraps(func)
```
- **Decorators with arguments** — add an extra outer layer.
```python
def decorator_name(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            ...
        return wrapper
    return decorator

@decorator_name(value)
def function_name():
    ...
```

### Context Managers
Objects that set up a resource on entering a `with` block and automatically clean it up on exit, even if an exception occurs. Commonly used for files, locks, and database connections.
```python
with expression as variable:
    ...

# class-based
class ContextName:
    def __enter__(self):
        return resource
    def __exit__(self, exc_type, exc_value, traceback):
        ...

# function-based
from contextlib import contextmanager

@contextmanager
def context_name():
    # setup
    yield resource
    # cleanup
```

### Magic (Dunder) Methods
Special methods with double underscores on both sides that Python calls automatically to define how objects behave with built-in operations, operators, and functions.
```python
__init__(self, ...)        # constructor
__str__(self)              # readable string, used by print()/str()
__repr__(self)             # developer string, used by repr()
__len__(self)              # len(obj)
__getitem__(self, key)     # obj[key]
__setitem__(self, key, v)  # obj[key] = v
__iter__(self)             # iter(obj)
__next__(self)             # next(obj)
__call__(self, ...)        # obj()
__enter__ / __exit__       # context manager protocol
__eq__(self, other)        # ==
__lt__(self, other)        # <
__add__(self, other)       # +
__sub__(self, other)       # -
__mul__(self, other)       # *
__contains__(self, item)   # in
```

### Dataclasses
A decorator that automatically generates boilerplate methods (`__init__`, `__repr__`, `__eq__`, etc.) for classes that mainly store data, based on type-annotated fields.
```python
from dataclasses import dataclass, field

@dataclass
class ClassName:
    field1: type
    field2: type = default_value
    field3: list = field(default_factory=list)

# options
@dataclass(frozen=True)    # immutable instances
@dataclass(order=True)     # enables comparison operators
```