#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = setuptools.find_packages()

setuptools.setup(
    name="legobricks",
    version="0.1.0",
    author="Ralf Waspe",
    author_email="rwaspe@me.com",
    description="Control micropython LEGO bricks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xavierxeon/legobricks",
    license='MIT',
    packages=packages,
    install_requires=['colorama', 'pyside2'],
    include_package_data=True,
    zip_safe=False,
)