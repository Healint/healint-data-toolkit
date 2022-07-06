#!/usr/bin/env python
from setuptools import setup, find_packages
from healint_data_toolkit import __version__


# Load the package's __version__.py module as a dictionary.
setup(
    name="healint-data-toolkit",
    version=__version__,
    description="A development toolkit for Healint",
    url="https://github.com/Healint/healint-data-toolkit",
    author="Shadowsong27",
    author_email="syk950527@gmail.com",
    license="MIT License",
    classifiers=["Development Status :: 1 - Planning"],
    keywords="",
    packages=find_packages(exclude=["test*"]),
    install_requires=[
        "toml==0.10.0",
        "attrs==19.1.0",
        "click==7.0",
        "psycopg2-binary==2.8.3",
        "sqlalchemy==1.3.0",
        "requests==2.22.0",
        "lxml==4.9.1",
        "bs4==4.8.0",
    ],
    package_data={},
    data_files=[],
    entry_points="""
        [console_scripts]
        toolkit=healint_data_toolkit.bin.manage:cli
    """,
)
