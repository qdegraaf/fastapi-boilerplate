from setuptools import find_packages, setup

__version__ = "0.1.0"


setup(
    name="FastAPI-App",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "fastapi==0.78.0",
    ],
    extras_require={
        "dev": [
            "mypy==0.960",
            "uvicorn[standard]==0.18.1",
        ],
        "format": [
            "black==22.3",
            "isort==5.10.1",
        ],
        "test": [
            "coverage[toml]>=6.2",
            "pytest>=7.0.0",
            "pytest-mock>=3.6.1",
            "requests>=2.27.0",
        ],
    },
)
