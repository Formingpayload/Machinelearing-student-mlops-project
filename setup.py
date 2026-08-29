from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''

    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requriements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity student project",
    version="0.0.1",
    author="Umair",
    long_description="Note source of dataset is unconfirmed, could be artifical and so dont draw conclusion from it. The main purpose is to showcase MLOPS with ETL pipelines for this project.",
    packages=find_packages(),
    install_requires=get_requirements()
)


            