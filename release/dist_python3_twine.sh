#!/usr/bin/env bash 

# Generate package
python3 setup.py sdist build

# Generate wheel
python3 setup.py bdist_wheel --universal

# Upload package via twine
twine upload dist/*