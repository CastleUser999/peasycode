import setuptools 

with open("README.md", "r") as fh: 
	description = fh.read() 

setuptools.setup( 
	name="peasycode", 
	version="0.0.1", 
	author="Bryce Garrido", 
	author_email="idiotfriendgroup@gmail.com", 
	packages=["test_package"], 
	description="A sample test package", 
	long_description=description, 
	long_description_content_type="text/markdown", 
	url="https://github.com/CastleUser999/peasycode/tree/main", 
	license='MIT', 
	python_requires='>=3.8', 
	install_requires=[] 
) 
