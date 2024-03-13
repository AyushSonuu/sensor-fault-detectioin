from setuptools import setup
from setuptools import find_packages
from typing import List

__VAERSION__ = '0.0.0'
NAME = "sensor"
AUTHOR_NAME = "AYUSH"
AUTHOR_EMAIL = "ayush.sonu@impressico.com"
HYPHEN_E_DOT = "-e ."


def get_requirements() -> List[str]:
    """
    This function returns list of requirements
    :return: list of requirements
    """
    requirements_list = []
    with open('requirements.txt', 'r') as f:
        requirements_list = f.readlines()
        requirements_list = [x.replace("\n", "") for x in requirements_list
                             if len(x.replace("\n", "")) > 0]
        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)
    return requirements_list


setup(
    name=NAME,
    version=__VAERSION__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    url="https://github.com/AyushSonuu/sensor-fault-detectioin",
    license="MIT",
    description="A library for reading sensors",
    install_requires=get_requirements(),
)
