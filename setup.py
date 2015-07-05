from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='clarity',
    version='0.0.0',
    description='A.I. Discovery & Exploration Library',
    long_description=long_description,
    url='https://github.com/legel/clarity',
    author='Lance Legel',
    author_email='lancelegel@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
	'Topic :: Scientific/Engineering :: Artificial Intelligence',
	'Topic :: Scientific/Engineering :: Information Analysis',
	'Topic :: Scientific/Engineering :: Mathematics',
	'Topic :: Scientific/Engineering :: Physics',
	'Topic :: Scientific/Engineering :: Visualization',
	'Intended Audience :: Developers',
	'Intended Audience :: Education',
	'Intended Audience :: Information Technology',
	'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='machine learning',
    packages=["clarity", "clarity.sense", "clarity.learn", "clarity.visualize"]
)

