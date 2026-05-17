from setuptools import setup, find_packages

setup(
    name="aca",
    version="0.1.0",
    description="Axiomatic Criterion Atlas",
    author="Ernesto Rosati",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.10",
)