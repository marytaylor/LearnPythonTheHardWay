# Using the sys module import the "arguments vector" (or to python argv)
#from sys import argv

# Listing the arguments within the arguments vector.  In this case I am using
#    the script and the filename.
#script, filename = argv

# Labeling a variable call txt.  This variable will use the open function and
#   the parameter for that function is filename.  Technically, this is creating
#   a file object when it is "opening" it.
#txt = open(filename)

# Print an output which displays the filename.
#print "Here's your file %r:" % filename
# Read the text variable and then print its output.
#print txt.read()

# Output some text with the print function.
print "Type the filename again:"
# Define a variable which asks the user for input.
file_again = raw_input("> ")

# Define a variable which opens the input given.
txt_again = open(file_again)
# Read the variable that opens the input given from the user.
print txt_again.read()

# Drill 1: What out in english what each line does. - Completed

# Drill 2: Part of Drill 1 - Completed

# Drill 3: Commands = Functions = Methods - Not really a "Drill"

# Drill 4: Get rid of lines 10-15 where raw input is used to run the script again.
# ^for the above I have commented out those lines.  I realize that this is not
# best practice for coding but I didn't want to lose the data. - Completed.

# Drill 5: Now use only the raw_input and rerun the script. Why is one way of
#    getting the filename better than another? - Without using the sys module it
#    appears that this file runs faster.  Also, it is easier to execute because
#    it do not require arguments in the very beginning.  This makes it more
#    user friends because I doesn't ask for arguments without knowing what kind
#    of arguments are required.

# Drill 6: Start python to start the python shell, and use open from the prompt
#    just like in this program.  Notice how you can open files and run read on
#    them from within python?

# I ran into a couple of errors when trying to do this.  First I tried to use
#    the open method in the wrong format.  It must have 2 arguments like this:
#    open(filename, mode).  Also, they have to be in the form of strings so I
#    had to use ''s around them.  Then I received the following error:
#    "ValueError: mode string must begin with one of 'r', 'w', 'a' or 'U', not
#    's'".  So I could not use the mode s.  Finally the file was opened but I
#    received this message "<open file 'ex15_sample.txt', mode 'r' at
#    0x1057e16f0>".  So it did not read the file as I expected.  I then stored
#    the open file in a variable and then used the read method on the variable
#    like this: t.read().

# Drill 7: Have your script also call close() on the txt and txt_again
#    variables. It's important to close files when you are done with them.
#    t.close()

# Could have also done this:
# filename = 'ex15_sample.txt'
# txt = open(filename)
# print txt.read
# txt.close
