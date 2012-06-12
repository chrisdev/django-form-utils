from setuptools import setup,find_packages
import subprocess



PACKAGE = "form_utils"  

long_description = open('README.rst').read() + open('CHANGES.rst').read()
VERSION = __import__(PACKAGE).__version__
setup(
    name='django-form-utils',
    version=VERSION,
    description='Form utilities for Django',
    long_description=long_description,
    author='Carl Meyer',
    author_email='carl@dirtcircle.com',
    url='http://bitbucket.org/carljm/django-form-utils/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    include_package_data=True,
    
    test_suite='tests.runtests.runtests'
)
