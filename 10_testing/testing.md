# Phase 14: Testing — Notes

### Beginner Introduction
**Testing** — writing code that automatically checks that your other code behaves as expected, so you catch bugs early and can change code safely later.

**Unit test** — a small test that checks one piece of behavior (usually one function or method) in isolation.

**Arrange – Act – Assert (AAA)** — the standard structure of a test:
```
Arrange   set up the data/objects needed
Act       run the code being tested
Assert    check the result is what you expected
```
**Good test habits**
- One test checks one behavior, with a descriptive name (`test_add_returns_sum`).
- Tests must be independent (order shouldn't matter).
- Test normal cases, edge cases (empty, zero, `None`), and error cases.

---

### `unittest`
Python's built-in testing framework, based on classes. Test classes inherit from `unittest.TestCase`, and test method names must start with `test`.
```python
import unittest

class TestClassName(unittest.TestCase):

    def setUp(self):                  # runs before EACH test
        ...

    def tearDown(self):               # runs after EACH test
        ...

    @classmethod
    def setUpClass(cls):              # runs once before all tests in the class
        ...

    @classmethod
    def tearDownClass(cls):           # runs once after all tests in the class
        ...

    def test_something(self):
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
```
**Running tests**
```bash
python -m unittest                              # auto-discover tests
python -m unittest test_file.py                 # one file
python -m unittest test_file.TestClass          # one class
python -m unittest test_file.TestClass.test_method
python -m unittest -v                           # verbose
```
**Skipping and grouping**
```python
@unittest.skip("reason")
@unittest.skipIf(condition, "reason")
@unittest.expectedFailure

with self.subTest(i=value):           # run many cases inside one test
    ...
```

---

### `pytest`
A third-party testing framework with simpler syntax: plain functions and plain `assert` statements, no classes required. It also has powerful fixtures, parametrization, and plugins. It can run `unittest` tests too.
```bash
pip install pytest
```
**Naming rules** — files `test_*.py` (or `*_test.py`), functions `test_*`, classes `Test*`.
```python
def test_something():
    assert actual == expected
```
**Running tests**
```bash
pytest                          # run all tests
pytest test_file.py             # one file
pytest test_file.py::test_name  # one test
pytest -v                       # verbose
pytest -s                       # show print() output
pytest -x                       # stop at first failure
pytest -k "keyword"             # run tests matching a name expression
pytest -m marker_name           # run tests with a marker
pytest --maxfail=n
pytest --cov=package_name       # coverage (needs: pip install pytest-cov)
```
**Fixtures** — reusable setup/teardown code, passed to tests by naming them as parameters.
```python
import pytest

@pytest.fixture
def fixture_name():
    resource = ...            # setup
    yield resource            # value given to the test
    ...                       # teardown (runs after the test)

def test_something(fixture_name):
    ...

@pytest.fixture(scope="function")   # function (default), class, module, package, session
```
**`conftest.py`** — a special file where fixtures are placed to share them across multiple test files automatically (no import needed).

**Parametrization** — run one test with many inputs.
```python
@pytest.mark.parametrize("input, expected", [
    (value1, result1),
    (value2, result2),
])
def test_something(input, expected):
    assert function(input) == expected
```
**Markers**
```python
@pytest.mark.skip(reason="...")
@pytest.mark.skipif(condition, reason="...")
@pytest.mark.xfail                    # expected to fail
@pytest.mark.custom_name              # custom marker (register in pytest.ini)
```
**Handy built-in fixtures**
```python
tmp_path          # temporary directory (pathlib.Path)
capsys            # capture printed output -> capsys.readouterr()
monkeypatch       # temporarily modify objects, env vars, dicts
```

---

### Mocking
Replacing real objects (databases, APIs, files, clock) with fake **mock** objects during a test, so tests are fast, predictable, and don't touch external systems. Mocks also record how they were called, so you can verify behavior.
```python
from unittest.mock import Mock, MagicMock, patch
```
**Creating mocks**
```python
m = Mock()                          # flexible fake object
m = MagicMock()                     # Mock + supports magic methods (__len__, __getitem__ ...)
m.return_value = value              # what calling the mock returns
m.side_effect = Exception("msg")    # raise an exception when called
m.side_effect = [v1, v2, v3]        # return different values on each call
m.attribute = value
```
**`patch`** — temporarily replaces an object with a mock for the duration of a test. Patch the name **where it is used (looked up)**, not where it is defined.
```python
# decorator (mock is passed as an argument)
@patch("module_name.object_name")
def test_something(mock_object):
    mock_object.return_value = value
    ...

# context manager
with patch("module_name.object_name") as mock_object:
    ...

# patch an attribute/method of an object
patch.object(ClassName, "method_name")
patch.dict(os.environ, {"KEY": "value"})
```
**Verifying calls**
```python
mock.assert_called()
mock.assert_called_once()
mock.assert_called_with(arg1, kwarg=value)
mock.assert_called_once_with(arg1)
mock.assert_any_call(arg1)
mock.assert_not_called()

mock.call_count
mock.call_args
mock.call_args_list
```
**pytest-mock** — a plugin that gives a `mocker` fixture (a cleaner wrapper over `unittest.mock`).
```bash
pip install pytest-mock
```
```python
def test_something(mocker):
    mock_obj = mocker.patch("module_name.object_name")
    mock_obj.return_value = value
```
**`monkeypatch` (pytest built-in)**
```python
monkeypatch.setattr(obj, "attr", value)
monkeypatch.setenv("KEY", "value")
monkeypatch.delenv("KEY")
```

---

### Assertions
Statements that check a condition is true; if false, the test **fails** and reports the difference.

**Python `assert` (used by pytest)**
```python
assert condition
assert condition, "message shown on failure"

assert a == b
assert a != b
assert a > b
assert item in collection
assert value is None
assert isinstance(obj, ClassName)
```
**`pytest.raises`** — assert that an exception is raised.
```python
with pytest.raises(ExceptionType):
    code_that_should_fail()

with pytest.raises(ExceptionType, match="regex"):
    ...

with pytest.raises(ExceptionType) as exc_info:
    ...
exc_info.value
```
**`pytest.approx`** — compare floats safely (avoids rounding errors like `0.1 + 0.2`).
```python
assert result == pytest.approx(expected)
assert result == pytest.approx(expected, rel=1e-3, abs=1e-6)
```
**`pytest.warns`**
```python
with pytest.warns(WarningType):
    ...
```
**`unittest` assertion methods**
```python
self.assertEqual(a, b)
self.assertNotEqual(a, b)
self.assertTrue(x)
self.assertFalse(x)
self.assertIs(a, b)
self.assertIsNone(x)
self.assertIsNotNone(x)
self.assertIn(item, collection)
self.assertNotIn(item, collection)
self.assertIsInstance(obj, ClassName)
self.assertGreater(a, b)
self.assertLess(a, b)
self.assertAlmostEqual(a, b, places=7)    # floats
self.assertListEqual(list1, list2)
self.assertDictEqual(dict1, dict2)
self.assertRaises(ExceptionType, function, *args)

with self.assertRaises(ExceptionType):
    ...
```