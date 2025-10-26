from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements() -> List[str]:
    """
    This file will read requirements.txt and return them as list
    """
    with open('requirements.txt') as requirement_file:
        requirements = requirement_file.readlines()
    requirements = [req.strip() for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    description='End to End Machine Learning Project with Deployment',
    version='0.0.1',
    author="Mahesh",
    author_email='maheshjaviniki@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)