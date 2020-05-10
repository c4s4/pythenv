# Pythenv

Pythenv runs a Python script in a temporary virtualenv created at runtime and deleted afterward.

<!--more-->

## Usage

### Using a requirements file

You can specify requirements in a [standard requirements file](https://pip.readthedocs.org/en/1.1/requirements.html), *requirements.txt*, such as:

```
foo==1.2.3
bar
```

To run a Python script *script.py* with these requirements, you would use *-r* option:

```
$ pythenv -r requirements.txt script.py arg1 arg2
```

### Embedding requirements in script

You can also embed requirements in the Python script, with a declaration in a comment that is a coma separated list of requirements:

```python
# requirements: foo==1.2.3, bar
```

You would run this script with following command:

```
$ pythenv script.py arg1 arg2
```

# Installation

To run *pythenv*, you must have installed:

- A python virtual machine (tested with versions *2.7.10* and *3.5.0*).
- virtualenv to create virtual environment (*pyvenv* will be called instead for Python *3.3* and above).
- PIP to install requirements.

To install *pythenv*, drop the script *pythenv* somewhere in your *PATH* (in a directory such as */usr/local/bin* or */opt/bin/* for instance).

# How it works

Pythenv will:

- Create a temporary virtualenv in */tmp* directory.
- Install dependencies in requirements.
- Run the script in created virtualenv.
- Delete temporary virtualenv.
- Return code returned by executed script.

If requirements are embedded in the script, a temporary requirements file will also be created in */tmp* directory.

*Enjoy!*
