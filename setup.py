from setuptools import setup, find_packages
#from typing import List


# Declaring variables for setup functions
#PROJECT_NAME = "house_price_prediction"
#VERSION = "0.0.3"
#AUTHOR = "Pratyush Mahato"
#DESCRIPTION = "This ML project predicts the price of a house"

#REQUIREMENTS_FILE_NAME = "requirements.txt"


#def get_requirements_list() -> List[str]:
#   """
#    Description: This function is going to return list of requirements mentioned in requirements.txt file
#
#    return This function is going to return a list which contain names of libraries mentioned in requirements.txt file 
 #   """
  #  with open(REQUIREMENTS_FILE_NAME) as requirements_file:
   #     return requirements_file.readlines().pop("-e .")



#setup(
#name= PROJECT_NAME,
#version= VERSION,
#author= AUTHOR,
#description = DESCRIPTION,
#packages= find_packages(),
#install_requires = get_requirements_list()

#)

from setuptools import find_packages, setup

setup(
    name="house_price_prediction",
    version="0.0.5",
    author="Pratyush Mahato",
    description="This ML project predicts the price of a house",
    packages=find_packages(),
    install_requires=[],
)


