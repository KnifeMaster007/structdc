from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='structdc',
    version='0.0.3',
    packages=['structdc'],
    url='https://github.com/KnifeMaster007/structdc',
    license='MIT',
    author='Ilia Galkin',
    author_email='km@j4u.su',
    python_requires='>=3.7',
    description='Data class mapper for C structures',
    long_description=long_description,
    long_description_content_type='text/x-rst'
)
