from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
name="pneumoniaDisease",
version="0.0.1",
author="Sankrita Patel",
author_email="sankritapatel6960@outlook.com",
install_requires=get_requirements('requirements.txt'),
package=find_packages()
)