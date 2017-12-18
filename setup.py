"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name='pertimental',
    packages = ['pertimental'],
    version='0.3.5.dev1',
    description='A Python Persian Text Sentiment Analyser.',
    long_description=long_description,
    url='https://github.com/pbarjoueian/pertimental',
    author='Peyman Barjoueian',
    author_email='p.barjoueian@gmail.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='nlp persian sentiment',

    package_data={
        'pertimental':
            ['model/Model.pkl'],
    },

    install_requires=['six', 'scikit-learn', 'nltk', 'libwapiti', 'hazm'],

    entry_points={
        'console_scripts': [
            'pertimental=pertimental:main',
        ],
    },
)
