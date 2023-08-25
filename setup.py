from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    #returns list of libraries
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replce("\n", " ") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name= 'Performance and Attriton',
    version= '0.0.1',
    author= 'Shourya',
    author_email= 'shourya242@gmail.com',
    packages= find_packages,
    libraries=get_requirements('requirements.txt')
)
