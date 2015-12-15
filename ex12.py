age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
# Try running "pydoc raw_input" and quit it by typing "q"
# This lets you access the python documentation
# Try running pydoc for open, file, os, and sys; write anything interesting you find.

# open() opens a file and returns the object
# file() opens a file for the modes of r, w, or a for reading, writing or appending.
# file() creates files if it doesn't exist
# file() adding + allows reading and writing simultaneously
# Thoughts: open and file seem really similar; whats the difference?
# os seems to be for mac, NT or Posix operating systems?
# os is a file within the python library
# "Programs that import and use 'os' stand a better chance of being portable
#       between different platforms."
# os looks like it may be used for environment errors
# sys "module provides access to some objects used of maintained by the
#       the interpreter and to functions that interact strongly with the interpreter."
# sys seems to have a few different functions, I may use them later on but none
#       seem to be of interest to me at the moment.
