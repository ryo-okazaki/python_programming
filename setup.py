from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='python_programming',
    version='1.0.0',
    #packages=['lesson_package', 'lesson_package.talk', 'lesson_package.tools'],
    packages=find_packages(),
    url='http://example.com',
    license='free',
    author='PC_User',
    author_email='',
    description='sample package'
)