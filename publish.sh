rm -rf dist
rm -rf sonocrop.egg-info
python3 setup.py sdist bdist_wheel && twine upload dist/*
