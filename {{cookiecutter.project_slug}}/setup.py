#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()


requirements = [
    'pybuilder==0.11.12'
    # TODO: put package requirements here
]

setup_requirements = [
    'pybuilder==0.11.12'
    # TODO({{ cookiecutter.github_username }}): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pybuilder==0.11.12'
    # TODO: put package test requirements here
]

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n',
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    include_package_data=True,
    install_requires=requirements,

    zip_safe=False,
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
