rm -rf dist
rm -rf dicomcrop.egg-info
python3 setup.py sdist bdist_wheel && twine upload dist/*
