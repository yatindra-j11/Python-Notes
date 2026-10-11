### `import`
Brings an entire module into the current namespace so its functions, classes, and variables can be accessed using dot notation. Used when you want access to everything in a module, or want to keep names namespaced to avoid clashes with your own code.
```python
import module_name
import module_name as alias
module_name.function_name()
```

### `from ... import`
Imports specific names (functions, classes, variables) directly from a module into the current namespace, so they can be used without the module prefix. Useful when you only need a few things from a module and want shorter, cleaner references.
```python
from module_name import name1, name2
from module_name import name as alias
from module_name import *   # imports everything (avoid in large projects)
```

### Creating Modules
A module is simply any Python file (`.py`) containing functions, classes, or variables that can be reused across other files by importing it. Python treats every `.py` file as a module automatically — no extra setup is required.
```python
# mymodule.py
def greet():
    ...

# another_file.py
import mymodule
mymodule.greet()
```

### Creating Packages
A package is a directory containing multiple related modules, grouped together and marked as a package using an `__init__.py` file (which can be empty or contain package-level init code). Packages allow large projects to be organized hierarchically and imported using dotted paths.
```
mypackage/
    __init__.py
    module1.py
    module2.py
```
```python
from mypackage import module1
from mypackage.module1 import function_name
```

### `pip` (Pip Installs Packages)
Python's standard package manager used to install, upgrade, and remove third-party libraries from the Python Package Index (PyPI). It also manages dependency versions and can generate/install from requirement files for reproducible environments.

**Common pip commands / workflow:**
```bash
pip install package_name              # install a package
pip install package_name==1.2.3       # install specific version
pip install --upgrade package_name    # upgrade a package
pip uninstall package_name            # remove a package
pip list                              # list installed packages
pip show package_name                 # show package details
```

### Virtual Environments
An isolated Python environmen~t with its own interpreter and site-packages directory, used to keep a project's dependencies separate from the system Python and from other projects, avoiding version conflicts. It's recommended to always use virtual environments in your projects and install packages inside the venvs. 

**Setup and usage flow:**
```bash
python -m venv venv_name              # create a virtual environment

# activate it
venv_name\Scripts\activate            # Windows
source venv_name/bin/activate         # macOS/Linux
venv_name\Scripts\activate.bat        # Command prompt
venv_name\Scripts\Activate.ps1        # Windows Powershell

pip install package_name              # install packages inside the venv

pip freeze > requirements.txt         # export installed packages to a file
pip install -r requirements.txt       # install all packages from a file

deactivate                            # exit the virtual environment
```
By convention we name virtual envs as **".venv"** (Recommended)

## Check package documentation
Checking a package's documentation can help you understand its application and purpose — what functions/classes it offers, their parameters, and expected behavior.

```python 
print(requests.get.__doc__)
```
Go to:
*"https://pypi.org/project/<package-name>/"*
Every package's PyPI page usually links to its official docs, GitHub repo, and shows the README.
Or you can search *"<package name> python docs"* on google. 

 