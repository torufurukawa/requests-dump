from setuptools import setup

version = '0.1.3'
name = 'requests-dump'
short_description = '`requests-dump` provides hook functions for requests.'
long_description = open('README.rst').read()

classifiers = [
    'Development Status :: 1 - Planning',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Topic :: Software Development',
]

setup(
    name=name,
    version=version,
    description=short_description,
    long_description=long_description,
    classifiers=classifiers,
    keywords=['http'],
    author='Toru Furukawa',
    author_email='torufurukawa@gmail.com',
    url='https://github.com/torufurukawa/requests-dump',
    license='MIT',
    install_requires=['requests >= 2.2.1']
)
