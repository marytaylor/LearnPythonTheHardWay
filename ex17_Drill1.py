# This script is really annoying. There's no need to ask you before doing the
# copy, and it prints too much out to the screen. Try to make the script more
# friendly to use by removing features.

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file).read()
# I used the above but it could also be done this way:
# in_file = open(from_file); indata = in_file.read()
# By adding .read() I had to remove the close() method at the end of this script
#    because it is automatically done.

out_file = open(to_file, 'w')
out_file.write(to_file)

print "Alright, all done."

out_file.close()
