from setuptools import find_packages, setup

from typing import List

hypen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements'''
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)



setup(
    name = "mlproject",
    version = "0.0.1",
    author = "sibashish",
    author_email = "sibashish958@gmail.com",
    packages = find_packages(),
    # install_requires = [
    #     'numpy',
    #     'pandas',
    #     'matplotlib',
    #     'seaborn',
    #     'scikit-learn'],
    # As it can be very long when we require many packages, we can use a requirements.txt file
    #we will create a function which can read the requirements.txt file and return the list of packages
    install_requires = get_requirements('requirements.txt'),
)