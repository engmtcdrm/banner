# Build and Distribute
```sh
python -m build

# have Twine test the distribution
twine check dist/*

# test pypi site
python -m twine upload --repository testpypi dist/*

python -m twine upload --repository pypi dist/*
```


# Run Test Environment
```sh
python -m venv env

.\env\Scripts\activate

# test pypi site
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps banner

python -m pip install pytest

python -m pytest
```