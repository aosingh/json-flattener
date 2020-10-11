from setuptools import find_packages, setup

from jflat import __version__


DISTNAME = 'jflat'
AUTHOR = 'Abhishek Singh'
MAINTAINER = 'Abhishek Singh'
MAINTAINER_EMAIL = 'aosingh@asu.edu'
DEPENDENCIES = ['click', 'pytest']
URL = 'https://github.com/aosingh/json-flattener'
PACKAGES = ['jflat']

CLASSIFIERS = [
    'Programming Language :: Python :: 3.6'
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Operating System :: POSIX :: Linux'
]

DESCRIPTION = ('Python utility to flatten a JSON object')


setup(name=DISTNAME,
      author=AUTHOR,
      author_email=MAINTAINER_EMAIL,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      description=DESCRIPTION,
      url=URL,
      version=__version__,
      packages=find_packages(exclude=("tests",)),
      package_dir={'jflat': 'jflat'},
      include_package_data=True,
      entry_points = {
      'console_scripts': [
          'jflat=jflat.cli:main'
      ]
      },
      install_requires=DEPENDENCIES,
      classifiers=CLASSIFIERS)