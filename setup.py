from setuptools import find_packages, setup
from typing import List


HYPEN_DOT ='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requriements =[]
    with open(file_path) as file_obj:
        requriements = file_obj.readlines()
        requriements =[req.replace("\n", "")for req in requriements]

        if HYPEN_DOT in requriements:
            requriements.remove(HYPEN_DOT)

    return requriements


setup(
    name='mlproject',
    version='0.0.1',
    author='Samrawit',
    author_email='hairaer02@gmail.com',
    packages= find_packages(),
    install_requiers=get_requirements('requirements.txt')

)