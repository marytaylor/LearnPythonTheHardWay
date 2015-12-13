x = "\\ text"
y = "\'This is in a single quote'"
z = " \"This is in a double quote\""

p = "\a not sure what this is? \a???"
# returned as "not sure what this is? ???"
d = "\b this should have a backspace\b"
q = "this is a form feed \f not sure what that is"
# returned as "this is a form feed
#                                                             not sure what that is"

a = "This is a character named name in the Unicode database (Unicode Only) \N{name} I guess that is the right format?  Maybe \N{something}"
b = "This is a carriage return. \r I think this should have a space after it."
# this printed as " I think this should have a space after it." so it appears the first sentence was removed. Try w below this to see."
w = "This is a carriage return. \r I think this should have a space after it. \r This? print print print"
# this printed as "This? print print printe a space after it."
c = "\t This is tabbed in!!!"

m = "This is a character with a 16-bit hex value xxxx (Unicode Only) or maybe like this? "
a = "Character with 32-bit hex value xxxxxxxx (Unicode Only) should that be one?"
r = "This is a ASCII vertical tab (VT) \v"
# variable r printed with a space after, kind of like a new line.

k = "This is a character with octal value ooo or maybe \002 or \100"
l = "This is a character with hex value \u{ABCD}"

print x, y, z, p, d, q

print a
print b
# added w in to try out carriage returns
print w
print c

print m
print a
print r

print k
print l

# Need to look into octal values and hex values
