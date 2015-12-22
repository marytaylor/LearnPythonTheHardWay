# Remember these commands:
# close - closes the file. Like File-> Save in your editor
# read - Reads the content of the file.  You can assign the result to a variable.
# readline - Reads just one line of a text file.
# truncate - Empties the file.  Watch out if you care about the file.
# write('stuff') - Writes "stuff" to the file.

# Using the sys module import the arguments vector
from sys import argv

# These are the arguments within the arguments vector.
script, filename = argv

# Print the text and the value of filename with the r format.
print "We're going to erase %r." % filename
# Print text.
print "If you don't want that, hit CTRL-C (^C)."
# Print text.
print "If you do want that, hit RETURN."

# As the user for input.
raw_input("?")

# Print text.
print "Opening the file..."
# Declare a variable that opens the filename with the format of w.
target = open(filename, 'w')

# Print text.
print "Truncating the file.  Goodbye!"
# Empty the target variable.
target.truncate()

# Print text.
print "Now I'm going to ask you for three lines."

# Declare a variable that asked for input and stores it in that variable.
line1 = raw_input("line 1: ")
# Declare a variable that asked for input and stores it in that variable.
line2 = raw_input("line 2: ")
# Declare a variable that asked for input and stores it in that variable.
# When running this script I received an error because I typed - instead of =.
line3 = raw_input("line 3: ")

# Print text.
print "I'm going to write these to the file."

# Write/print the value stored in the line1 variable.
target.write(line1)
# Write a new line.
target.write("\n")
# Write/print the value stored in the line2 variable.
target.write(line2)
# Write a new line.
target.write("\n")
# Write/print the value stored in the line3 variable.
target.write(line3)
# Write a new line.
target.write("\n")

# Print text.
print "And finally, we close it."
# Close and Save the target variables.
target.close()

# Drill 5: is target.truncate() necessary? - I removed it first to try and it
#    still performed the same exact task by saving the new lines.  It is not
#    necessary because we are using the w format.
