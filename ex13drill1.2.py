# Write a script that uses more arguments

from sys import argv

# For some reason "= argv" has to be at the end of this line.  It did not work
#    in the front.
script, test1, test2, test3, test4, test5 = argv

print script
print test1
print test2
print test3
print test4
print test5
