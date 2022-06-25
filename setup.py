from setuptools import find_packages, setup

__version__ = "0.1.0"


setup(
    name="FastAPI-App",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "fastapi==0.78.0",
    ],
)
