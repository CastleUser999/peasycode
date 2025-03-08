# PeasyCode
PyPI or Python Package Index is used to create this package to publish it,
PeasyCode is a Python package to generate code while running the code by simply running 
``` import peasycode
if __name__ = "__main__":
   peasycode.main()
```
You see that i used ```main``` to run it.
The output of that code will be:
```
Choose a Action
1. Add line
2. Delete line
3. Edit line
4. Run
5. Exit
```
For example, we import a module name "time" by navigating with a location of 1/8/1/time
# Installation
```
pip install peasycode
```
# License
This package has the license of MIT
# Generating
Peasycode generates code about 10 seconds when using action 4 and stores the file as a "pyscdlst" file like testing.pyscd with contents of ["# hello", "x = 100"]
