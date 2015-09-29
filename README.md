Pythenv
=======

Pythenv is a script to run a Python script within a virtualenv created at runtime and deleted afterward. Requirements may be passed as a requirements file on command line or embedded in the script after shebang, as follows:

```python
#!/usr/bin/env python
# requirements: foo==1.2.3, bar

print("Hello World!")
```

If you use requirements file, you would call the script as follows:

```bash
$ pythenv requirements.txt script.py arg1 arg2...
```

If requirements are embedded in the script, one would call it as:

```bash
$ pythenv script.py arg1 arg2...
```

Pythenv will:

- Create a temporary virtualenv in */tlo* directory.
- Install dependencies in requirements.
- Run the script in created virtualnv.
- Delete temporary virtualenv.
- Return code returned by executed script.

*Enjoy*
