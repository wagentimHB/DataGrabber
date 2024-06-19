import setuptools

with open('requirements.txt', 'r') as f:
    install_requires=f.read().splitlines()

setuptools.setup(name='DataGrabber', packages='DataGrabber', install_requires=install_requires)