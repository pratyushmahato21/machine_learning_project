from setuptools import setup
from typing import List


def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirements mentioned in requirements.txt file

    return This function is going to return a list which contain names of libraries mentioned in requirements.txt file 
    """
    with open(REQUIREMENTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines()

# Declaring variables for setup functions
PROJECT_NAME = "house_price_prediction"
VERSION = "0.0.1"
AUTHOR = "Pratyush Mahato"
DESCRIPTION = "This ML project predicts the price of a house"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"


setup(
name= PROJECT_NAME,
version= VERSION,
author= AUTHOR,
description = DESCRIPTION,
packages= PACKAGES,
install_requires = get_requirements_list()

)



    