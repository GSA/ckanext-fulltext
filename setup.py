from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-fulltext',
	version=version,
	description="",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='',
	author_email='',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.fulltext'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
    
    [ckan.plugins]
    inforeg_solr_search=ckanext.fulltext.plugin:InforegFulltextSearch
 
	[paste.paster_command]
	fulltext=ckanext.fulltext.commands.fulltext:Fulltext

	""",
)



