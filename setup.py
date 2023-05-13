from setuptools import setup, find_packages

setup(
name='python',
version='0.1',
packages=find_packages(exclude=['tests*']),
licence='MIT',
description = 'EDSA example python package',
long_description = open('README.md').read(),
install_requires = ['numpy'],
url = 'https://github.com/spark1401/python',
author ='Sameer Parker',
author_email = 'spark1401@gmail.com'

)