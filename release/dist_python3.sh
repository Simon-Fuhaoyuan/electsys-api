#!/usr/bin/env bash 

# Generate package
python3 setup.py sdist build

# Generate wheel
python3 setup.py bdist_wheel --universal

# Upload source package
python3 setup.py sdist upload

# Upload pre-compiled package
python3 setup.py bdist_wheel upload