#!/usr/bin/env bash 

# Generate package
python setup.py sdist build

# Generate wheel
python setup.py bdist_wheel --universal

# Upload package via twine
twine upload dist/*