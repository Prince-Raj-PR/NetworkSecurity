from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:

    requirement_lst:List[str]=[]

    try:
        with open('requirements.txt','r') as file:
            #Read Lines From File
            lines = file.readlines()
            #Process Each lines
            for line in lines:
                requirement = line.strip()
                #Ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
         print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Prince Raj",
    author_email="prince.raj160418@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

