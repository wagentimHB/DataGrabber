from setuptools import setup, find_packages

# Function to read requirements.txt
def parse_requirements(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        return [line for line in lines if line and not line.startswith('#')]

setup(
    name='DataGrabber',
    version='0.1',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt'),
)
