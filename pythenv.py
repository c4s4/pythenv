#!/usr/bin/env python
# encoding: UTF-8

from __future__ import print_function

import os
import re
import sys
import atexit
import tempfile
import subprocess


HELP = '''pythenv [requirements.txt] script.py [args...]
requirements.txt   The requirements file to run script
script.py          The Python script to run
args..             The script arguments'''


def error(message, code):
    print(message)
    print(HELP)
    sys.exit(code)


def run(command):
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode:
        raise Exception("Error running command '%s': %s" %
                        (' '.join(command), stderr.strip()))
    return stdout


def parse_dependencies(py_file):
    source = None
    with open(py_file) as stream:
        source = stream.read()
    match = re.search(r'^#\s*requirements:\s+(.*?)$',
                      source, flags=re.MULTILINE)
    if match:
        requirements = match.group(1)
    else:
        error("Requirements not found in Python source file", 1)
    text = '\n'.join([l.strip() for l in requirements.split(",")])
    _, tmp_file = tempfile.mkstemp(prefix='pythenv-requirements-',
                                   suffix='.txt', dir='/tmp')
    with open(tmp_file, 'w') as stream:
        stream.write(text)
    atexit.register(os.remove, tmp_file)
    return tmp_file


def create_virtualenv():
    print("Creating virtualenv...", file=sys.stderr)
    env_dir = tempfile.mkdtemp(prefix='pythenv-env-', dir='/tmp')
    run(('virtualenv', env_dir))
    atexit.register(run, ('rm', '-rf', env_dir))
    return env_dir


def install_reqs(env_dir, reqs_file):
    print("Installing dependencies...", file=sys.stderr)
    run((os.path.join(env_dir, 'bin', 'pip'), 'install', '-r', reqs_file))


def run_script(env_dir, script_file, args):
    print("Running script...", file=sys.stderr)
    command = [os.path.join(env_dir, 'bin', 'python'), script_file] + args
    return subprocess.call(command)


def main(script_file, reqs_file, args):
    env_dir = create_virtualenv()
    install_reqs(env_dir, reqs_file)
    code = run_script(env_dir, script_file, args)
    sys.exit(code)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        error("You must pass script to run on command line", 1)
    elif sys.argv[1].endswith('.py'):
        dep_file = parse_dependencies(sys.argv[1])
        main(sys.argv[1], dep_file, sys.argv[2:])
    elif sys.argv[1].endswith('.txt') and sys.argv[2].endswith('.py'):
        main(sys.argv[2], sys.argv[1], sys.argv[3:])
    else:
        error(None, 1)
