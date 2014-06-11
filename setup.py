"""
Just install with

	pip install numpy_display

and then type the following in your IPython notebook:

	import numpy_display

Then your numpy matrices will be formatted as HTML tables.
"""
from setuptools import setup
setup(
	author="Petter Strandmark",
	author_email="petter.strandmark@gmail.com",
	description="Formats numpy matrices in an IPython Notebook",
	license="Public Domain",
	keywords=['ipython', 'notebook', 'numpy'],
	url='https://github.com/PetterS/numpy_display',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Other Environment',
		'Intended Audience :: End Users/Desktop',
		'License :: Public Domain',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Text Processing :: Markup :: HTML',
		'Topic :: Scientific/Engineering',
	],

	name="numpy_display",
	version="1.2.0",
	py_modules=["numpy_display"],

	install_requires=["numpy"]
)
