from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requiremnts=[req.replace('/n', '') for req in requirements]

        if "-e ." in requirements:
            requirements.remove('-e .')

    return requirements


setup(
    name = 'end-end-pipline',
    version='0.0.1',
    author='Braimah',
    author_email='eseoghenabraimah@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)