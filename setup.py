from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

version = {}
with open(path.join(here, "dicomcrop", "__version__.py")) as f:
    exec(f.read(), version)

setup(

  name='dicomcrop',

  version=version["__version__"],

  description='Prepare bedside medical images for machine learning and image interpretation.',

  long_description=long_description,

  long_description_content_type='text/markdown',

  url='https://github.com/falcucci/dicomcrop',

  author='Alexsander Falcucci',

  author_email='alex.falcucci@gmail.com',

  license = "Apache Software License 2.0",


  classifiers=[
    'Intended Audience :: Healthcare Industry',
    'Topic :: Scientific/Engineering :: Medical Science Apps.',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],

  keywords='dicom bedside pocus ffmpeg opencv echo cardiac cancer hospital',

  packages=find_packages(),

  python_requires='>=3.6',

  install_requires=[
      'cffi',
      'cryptography',
      'dicom2jpg',
      'et-xmlfile',
      'fire',
      'numpy',
      'opencv-python',
      'openpyxl',
      'Pillow',
      'pycparser',
      'pydicom',
      'PyJWT',
      'pylibjpeg',
      'pylibjpeg-libjpeg',
      'pylibjpeg-openjpeg',
      'six',
      'termcolor'
  ],
entry_points={  # Optional
    'console_scripts': [
        'dicomcrop=dicomcrop.cli:main',
    ],
},

)
