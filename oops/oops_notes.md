[OOPS YT playlist by Corey Schafer](https://youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&si=AbQjrqcNvH3Ga6Xe)

# Object-Oriented Programming (OOP) — Python Notes
OOP is a programming paradigm that logically groups related data (attributes) and the functions (methods) that operate on that data into objects, making code easier to reuse, extend, and maintain.Example:
```python
class BankAccount:
    bank_name = "ABC Bank" # Class variable

    def __init__(self, account_holder, balance): # Constructor
        self.account_holder = account_holder
        self.balance = balance

    def show_details(self):
        print(f"Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")
```
## Classes
Blueprint/template used to create objects that bundle data and behavior.
```python
class ClassName:
    pass
```

## Objects
An instance of a class, holding actual data.-
```python
obj = ClassName()
```

## Constructors
Special method auto-called when an object is created, used to initialize it.
```python
def __init__(self, param1, param2,...):
    ...
```

## Attributes
Variables that store data belonging to a class or an instance.
```python
self.attribute_name = value
```
**"self"** is a reference to the current instance. Through it, you can access the current instance's attributes and methods, (distinguish instance attributes from local variables). called "this" in java,C++,js etc.

## Methods
Functions defined inside a class that define object behavior.
```python
def method_name(self, args):
    ...
```

## Instance Variables
Variables unique to each object, usually set via `self` inside methods.
```python
self.var_name = value
```

## Class Variables
Variables shared by all instances of a class, defined at class level.
```python
class ClassName:
    var_name = value
```

## Instance Methods
Methods that act on instance data; take `self` as the first parameter.
```python
def method(self, args):
    ...
```

## Class Methods
Methods bound to the class rather than an instance; take `cls` as first parameter.
```python
@classmethod
def method(cls, args):
    ...
```

## Static Methods
Methods that don't access instance or class state; behave like plain functions inside a class.
```python
@staticmethod
def method(args):
    ...
```

### Combined Syntax: Class, Constructor, Attributes & Methods
```python
class ClassName:
    class_variable = value                 # class variable

    def __init__(self, param1, param2):    # constructor
        self.param1 = param1               # instance variable/attribute
        self.param2 = param2

    def instance_method(self):             # instance method
        ...

    @classmethod
    def class_method(cls):                 # class method
        ...

    @staticmethod
    def static_method():                   # static method
        ...

obj = ClassName(arg1, arg2)                # object creation
obj.instance_method()
ClassName.class_method()
ClassName.static_method()
```

## Inheritance
Mechanism where a class (child) acquires properties/behavior of another class (parent).
```python
class Child(Parent):
    pass
```

## Method Overriding
Redefining a parent class's method in the child class using the same name/signature.
```python
class Child(Parent):
    def method_name(self):
        ...
```

## Polymorphism
Ability of objects of different classes to be used through a common interface, each responding in its own way.
```python
for obj in [obj1, obj2]:
    obj.method_name()
```

## Encapsulation
Bundling data and methods together while restricting direct access using access-control conventions.
```python
self._protected_var = value
self.__private_var = value
```

## Abstraction
Hiding implementation details and exposing only essential features via abstract classes/methods.
```python
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def method_name(self):
        pass
```

## Multiple Inheritance
A class inheriting from more than one parent class.
```python
class Child(Parent1, Parent2):
    pass
```

## Method Resolution Order (MRO)
The order in which Python searches classes for a method/attribute in multiple inheritance (C3 linearization).
```python
ClassName.__mro__
ClassName.mro()
```