# Use the sys module to import the arguments vector
from sys import argv

# The arguents vector will need the script and a file.
script, input_file = argv

# Define a function called print all that reads the file.
def print_all(f):
    print f.read()

# Define a function called rewind that sets the file position to the value given.
# In this case the value is 0 setting it to the "absolute" or first position.
# other values are 1 and 2.
def rewind(f):
    f.seek(0)

# Define a function called print_a_line that takes 2 variables.
def print_a_line(line_count, f):
# the first variable is listed and it reads the specific line.
    print line_count, f.readline(),
    # adding that 2nd comma avoids a space between each line in the terminal.
    # thats because readline() automatically adds a \n

# Define a variable that opens the input_file given at the beginning.
current_file = open(input_file)

# Print text.
print "First let's print the whole file: \n"

# Use the print_all function on the current_file variable (which reads our input
#   file from the beginning).
print_all(current_file)

# Print text.
print "Now let's rewind, kind of like a tape."

# Use the rewind function on the current_file. This sets the file position to
#   the very beginning of the file.
rewind(current_file)

# Print text.
print "Let's print three lines:"

# Set current line to 1
current_line = 1
# Prints line number and the text on line 1
print_a_line(current_line, current_file)

# Set current line to 2
current_line += 1
# Prints line number and the text on that line.
print_a_line(current_line, current_file)

# Set current line to 3
current_line += 1
# Prints line number and the text on that line.
print_a_line(current_line, current_file)

# Drill 1: Write English comments for each line to understand what that line does.
# Drill 2: current_line becomes line_count because it is the first argument
#   passed into the print_a_line function.
# Drill 3: nothing to write for this
# Drill 4: nothing to write for this - wrote it in my comments previously.
# Drill 5: Look up += and replace it in this script.
