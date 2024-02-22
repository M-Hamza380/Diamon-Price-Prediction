from setuptools import setup, find_packages
from typing import List

Hypen_E_Dot = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
        this function will return list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)
    
    return requirements

setup(
    name= 'mlRegression',
    version= '0.0.1',
    author= "Muhammad Hamza Anjum",
    author_email= "hamza.anjum380@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt'),
)

