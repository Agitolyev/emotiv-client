#!/usr/bin/env python
from setuptools import setup, find_packages

import emotiv_client

setup(
    name="emotiv_client",
    version=emotiv_client.__version__,
    description="Python client for emotiv devices",
    author="Alexandr Agitolyev",
    author_email="alex.agitolyev@gmail.com",
    license="MIT",
    url="https://github.com/Agitolyev/emotiv-client",
    packages=find_packages(),
    install_requires=["websockets", "asyncio"]
)
