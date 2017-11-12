#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
	name='ffmap',
	version='0.0.2',
	license='GPL',
	description='FFF-MAP',
	author='Dominik Heidler',
	author_email='dominik@heidler.eu',
	url='http://github.com/asdil12/ff-map',
	packages=find_packages(),  
	include_package_data=True,  
	install_requires=[  
		"flask",  
		"requests",  
		"lxml",  
		"python-dateutil",  
		"numpy",  
		"scipy",  
		"tilestache",  
		"pymongo",  
	],  
	entry_points={  
		'console_scripts': [  
			'ffmap = ffmap.__main__:main',  
		],  
	},  
)

