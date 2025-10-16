from setuptools import setup, find_packages
from typing import List
hypen_e = '-e .'# this inside requirement.txt will trigger the setup.py file
def find_requirements(folder_path:str)->List[str]:
    requirements = []
    with open(folder_path, mode='r') as req:
        requirements = req.readlines()
        requirements = [obj.replace("\n",'') for obj in requirements]
        requirements=requirements.remove(hypen_e)
    return requirements        

setup( name = 'ML-Project',
      version='1.0.0',
      author= 'BlueGod',
      author_email='roboticsengineer01@gmail.com',
       packages = find_packages(),
      install_requires = find_requirements('requirements.txt')
)