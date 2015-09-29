#!/usr/bin/env python
# encoding: UTF-8
# requirements: PyYAML

import yaml


def main():
    print(yaml.dump({'a': 1, 'b': 2}))


if __name__ == '__main__':
    main()
