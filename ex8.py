#Here I will type the definition of a %r from the python documentation (https://docs.python.org/2/library/functions.html#func-repr)
# %r is repr(object) = Return a string containing a printable representation of an object.  This is the same value
#yielded by conversions (reverse quotes). It is sometimes useful to be able to access this operations as an ordinary
#function.  For many types, this function makes an attempt to return a string that would yield an object with the
#same value when passed to eval(), oterwise the representation is a string enclosed in angle brackets that contains
#the same of the type of the object together with additional information often including the name and address of the
#object. A class can control what this function returns for its instancse by defining a _repr_() method.

#this declares a variable that uses string formatters with r which returns a printable representation of an object.
formatter = "%r %r %r %r"

# this prints the array I declared using the formatter variable
print formatter % (1, 2, 3, 4)
# this prints the array I declared using the formatter variable
print formatter % ("one", "two", "three", "four")
# this prints the array I declared using the formatter variable
print formatter % (True, False, False, True)
# this prints the array I declared using the formatter variable
print formatter % (formatter, formatter, formatter, formatter)
# This prints the array with strings that I declared using the formatter variable
print formatter % (
        "I had this thing.",
        "That you could type up right.",
        #this one line will display double quotes instead of single quotes. When I remove the ' it shows up in single quotes.
        "But it didn't sing.",
        "So I said goodnight."
)
