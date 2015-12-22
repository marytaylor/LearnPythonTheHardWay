from sys import argv

script, filename = argv

print "We are going to read the file %r that you created." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("Ready to read?")

print "Reading the file..."
# I kept receiving an error when first trying to run this.  This is because I
#     used the wrong format of w.  Instead I need to use r for the reading method.
# w is for writing. r is for reading and w+ lets you read and write.

# Interesting comment found online:
# If you are to use a dual-mode such as r+ or w+, you need to familiarize
# yourself with the .seek() method too, as using both reading and writing
# operations will move the current position in the file and you'll most likely
# want to move that current file position explicitly between such operations.
target = open(filename, 'r')

# I first tried to input 'filename' within the read method.  It is not necessary.
x = target.read()
print x

target.close()
