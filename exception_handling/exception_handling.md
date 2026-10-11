# Phase 7: Exception Handling — Notes

### Exception Handling (Overview)
A mechanism to catch and respond to runtime errors so the program doesn't crash unexpectedly. Errors raised during execution are called exceptions, and handling them lets you recover gracefully or fail with a clear message.
```python
try:
    ...
except ExceptionType:
    ...
else:
    ...
finally:
    ...
```

### `try`
Wraps the code that might raise an exception; if an error occurs, execution jumps to the matching `except` block.
```python
try:
    risky_code
```

### `except`
Catches and handles exceptions raised in the `try` block. You can catch specific exception types, multiple types, or capture the exception object using `as`.
```python
except ExceptionType:
    ...

except ExceptionType as e:           # access the error object
    ...

except (Type1, Type2):               # catch multiple types
    ...

except Exception:                    # catch-all for most errors
    ...
```

### `else`
Runs only if the `try` block completes **without** raising any exception. Useful for code that should execute only on success.
```python
else:
    ...
```

### `finally`
Runs **always**, whether an exception occurred or not. Commonly used for cleanup tasks like closing files or releasing resources.
```python
finally:
    ...
```

### `raise`
Manually triggers an exception, either a built-in one or a custom one. Can also re-raise the current exception inside an `except` block.
```python
raise ExceptionType("message")

raise                                # re-raise the current exception

raise NewException("msg") from e     # chain exceptions
```

### Custom Exceptions
User-defined exception classes created by inheriting from `Exception` (or one of its subclasses), used to represent application-specific errors.
```python
class CustomError(Exception):
    pass

# with custom message/attributes
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

raise CustomError("message")
```

### Common Built-in Exceptions (Quick Reference)
```python
ValueError           # right type, inappropriate value
TypeError            # operation on wrong type
ZeroDivisionError    # division by zero
IndexError           # list index out of range
KeyError             # missing dictionary key
FileNotFoundError    # file doesn't exist
ImportError          # import fails
AttributeError       # invalid attribute access
```