# responsible for creating the ml package
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
# setup(
#     name='mlproject',
#     version='0.0.1',
#     author='Madan',
#     author_email='madan.tiwary26@gmail.com',
#     packages=find_packages(),
#     install_requires=['pandas','numpy','seaborn']
# )

'but suppose in some project we need 100 such libraries. it is not feasible to write everything'
'for this we write a function'

def get_requirements(file_path:str) -> List[str]:
    'this function returns the list of requirements'
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements
    

setup(
    name='ml-project',
    version='0.0.1',
    author='Madan Gopal Tiwary',
    author_email='madan.tiwary26@gmail.com',
    install_requires=get_requirements('requirements.txt')
)