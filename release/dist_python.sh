#!/usr/bin/env bash 

# Generate package
python setup.py sdist build

# Generate wheel
python setup.py bdist_wheel --universal

# Upload source package
python setup.py sdist upload

# Upload pre-compiled package
python setup.py bdist_wheel upload