from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

# Used 'echo "text here" > example.txt to' to create file.
# Used cat example.txt to view the file I created.

# When first trying to run this script, I received this error:
# Traceback (most recent call last):
#   File "ex17.py", line 12, in <module>
#     print "The input file is %d bytes long" % len(indata)
# I forgot to add ()'s after 'indata = in_file.read()'

# Drill 3: Read about cat.  Use man cat in terminal.
# cat -- concatenate and print files

# Drill 4: Find out why you had to write out_file.close() in the code.
# Read an interesting forum about this.  If I remove the close() methods in this
#    script then it will still close and save exactly as it did.  The reason we
#    have to add it in is because it "promises" to save the file.  OS's will
#    standardily close and save but depending on what processes are running it
#    is not always dependable.
# Also, it is good practice to close the out_file after reading it and before
#    opening the output file.  So the placement we used is not best practice.
#    This is helpful in scenarios when the file may have the same name or
#    relative path.

# Drill 5: Go read up on Python's import statement, and start python to try it out.
