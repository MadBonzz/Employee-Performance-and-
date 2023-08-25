from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    #returns list of libraries
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replce("\n", " ") for req in requirements]

setup(
    name= 'Performance and Attriton',
    version= '0.0.1',
    author= 'Shourya',
    author_email= 'shourya242@gmail.com',
    packages= find_packages,
    libraries=get_requirements('requirements.txt')
)
