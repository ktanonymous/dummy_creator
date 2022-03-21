from setuptools import setup, find_packages


setup(
    name='dummy_creator',
    version='1.0.0',
    author='ktanonymous',
    url='https://github.com/ktanonymous/dummy_creator/tree/main',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['numpy'],
    long_description='README.md',
)
