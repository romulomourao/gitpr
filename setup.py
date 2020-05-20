import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='gitpr',
     version='0.2',
     scripts=['gitpr'] ,
     author="Romulo Mourão",
     author_email="romulo.dam@gmail.com",
     description="Github PR Utility",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/romulomourao/gitpr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Development Status :: 3 - Alpha",
     ],
 )
