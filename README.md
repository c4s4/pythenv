Pythenv
=======

Pythenv runs a Python script in a temporary virtualenv created at runtime and deleted afterward.

<!--more-->

Using a requirements file
-------------------------

You can specify requirements in a [standard requirements file](https://pip.readthedocs.org/en/1.1/requirements.html), *requirements.txt*, such as:

```
foo==1.2.3
bar
```

To run a Python script *script.py* with these requirements, you would type:

```
$ pythenv requirements.txt script.py arg1 arg2
reating virtualenv...
Installing dependencies...
Running script...
```

Embedding requirements in script
--------------------------------

You can also embed requirements in the Python script, with a declaration in a comment that is a coma separated list of requirements:

```python
# requirements: foo==1.2.3, bar
```

You would run this script with follwing command:

```
$ pythenv script.py arg1 arg2
reating virtualenv...
Installing dependencies...
Running script...
```

How it works
------------

Pythenv will:

- Create a temporary virtualenv in */tmp* directory.
- Install dependencies in requirements.
- Run the script in created virtualnv.
- Delete temporary virtualenv.
- Return code returned by executed script.

If requirements are embedded in the script, a temporary requirements file will also be created in */tmp* directory.

*Enjoy!*
