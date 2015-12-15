# argv is a argument variable.  This variable holds the arguments you pass to
#       your Python script when you run it.

# sys is a module.  some people call them libraries.
from sys import argv


#This "unpacks" argv and assigns it to 4 variables
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# When I first ran this in terminal I did not give enough values.  I had to run
#    the program by typing the file name and listing variables.
#This is the error I received:
# File "ex13.py", line 9, in <module>
#   script, first, second, third = argv
# ValueError: need more than 3 values to unpack

# It wouldn't run because there was nothing to unpack and there were not enough
#   variables to meet the criteria for unpacking.
