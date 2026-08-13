# setup.py

from setuptools import setup, find_packages

setup(
    name="devpulse",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "rich>=13.7.0"
    ],
    entry_points={
        "console_scripts": [
            "devpulse = devpulse.main:main",
        ],
    },
)