Do not publish this project on PyPI.

# Install

Install locally by cloning in a virtual env and using pip to
install in editable mode. I named this `microspecapi` to avoid
conflict with the `microspec` package.

```powershell
> python -m venv api
> .\api\Scripts\activate
(api) > python -m pip install -U pip
(api) > pip list
Package      Version Location
------------ ------- ----------------------------------------------
microspec    0.1.1a8
microspecapi 0.0.0   c:\cygwin64\home\mike\chromation\microspec-api
pip          20.2.2
pyserial     3.4
setuptools   41.2.0
```

The `microspecapi` package defines a `microspec` module, not to
be confused with the `microspec` package which currently only
installs a `microspeclib` module (plus some utility scripts).

# Test the examples in the documentation

Now that `microspecapi` is installed, the doctests in
`microspec.__main__.py`. can be run from any directory:

```powershell
(api) > python -m microspec
```

Again, `microspec` refers to *this* project, *not* the project
with `microspeclib`.

When this project is integrated into `microspeclib`, the
`microspec` module will still refer to the module defined here.
There is no `microspec` module currently in the `microspec`
project, only a `microspeclib` module.

# Run the unit tests

Enter the repository directory and run `pytest`:

```powershell
(api) > cd microspec-api
(api) > pytest
...
microspec\tests\test_constants.py ....          [100%]
...
```

Use flag `--testdox` to read the list of tests as if they were
documentation:

```powershell
(api) > pytest --testdox

microspec\tests\test_constants.py

Values_of_status
 ✓ OK is 0
 ✓ ERROR is 1
 ✓ 0 maps to str OK
 ✓ 1 maps to str ERROR
 ✓ OK equals microspeclib StatusOK
 ✓ ERROR equals microspeclib StatusError

Values_of_led_setting
 ✓ OFF is 0
 ✓ GREEN is 1
 ✓ RED is 2
 ✓ 0 maps to str OFF
 ✓ 1 maps to str GREEN
 ✓ 2 maps to str RED
 ...
```
