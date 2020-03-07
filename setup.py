#!/usr/bin/env python

"""The setup script."""
import os

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

# requirements = ["certifi==2019.11.28",
#                 "chardet==3.0.4",
#                 "idna==2.9",
#                 "lxml==4.5.0",
#                 "python-dateutil==2.8.1",
#                 "requests==2.23.0",
#                 "six==1.14.0",
#                 "urllib3==1.25.8"]

with open(os.path.join(os.getcwd(), "requirements.txt")) as req:
    requirements = req.readlines()

test_requirements = []
setup_requirements = []

setup(
    author="Shlomi Kushchi",
    author_email='shlomik@example.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="a small web crawler for the pastebin.com website",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='simple_pastebin_parser',
    name='simple_pastebin_parser',
    packages=find_packages(include=['simple_pastebin_parser', 'simple_pastebin_parser.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/shlomikushchi/simple_pastebin_parser',
    version='v0.3.4',
    zip_safe=False,
)
