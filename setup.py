from setuptools import find_packages, setup

setup(
    name='censusdata',
    version='0.1.0',
    url='https://github.com/spencer-keating-work/censusdata.git',
    author='Spencer Keating',
    author_email='keating@econw.com',
    description='Fork of the CensusData package with 2020 ACS variables.',
    packages=find_packages(),    
    install_requires=['pandas'],
)
