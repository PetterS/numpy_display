
from setuptools import setup
setup(
	author="Petter Strandmark",
	author_email="petter.strandmark@gmail.com",
	description="Formats numpy matrices in an IPython Notebook",
	license="Public Domain",
	keywords=['ipython', 'notebook', 'numpy'],
	url='http://strandmark.net',
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Other Environment',
		'Intended Audience :: End Users/Desktop',
		'License :: OSI Approved :: Public Domain',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Text Processing :: Markup :: HTML',
		'Topic :: Scientific/Engineering',
	],

	name="numpy_display",
	version="1.0.0",
	py_modules=["numpy_display"],
)
