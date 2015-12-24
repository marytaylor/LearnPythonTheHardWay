the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    #append is a function that lists understand
    elements.append(i)

# now we print them out too
for i in elements:
    print "Elements was: %d" % i

# Drill1: Take a look at how you used range. Look up the range function to
#   understand it.
# Ran pydoc range: lists all values within the range given. Last value given
#   in range is not included due to the 0 value.

# Drill2: Could you have avoided that for-loop entirely on line 22 and just
#   assigned range(0,6) directly to elements?
# Yes and no.  I can assign the range directly to elements (which I tested) by
#   changing elements = range(0, 6).  However, the for loop is still necessary
#   for printing the text and iterating through elements.

# Drill3: Find the Python documentation on lists and read about them. What other
#   operations can you do to lists besides append?
# append() -> append object to end
# count() -> return number of occurrences of value
# extend() -> extend list by appending elements from the iterable
# index() -> return first index of value; index(value, [start, [stop]])
# insert() -> insert object before index; insert(index, object)
# pop() -> remove and return item at index; pop(index)
# remove() -> remove first occurence of value; remove(value)
# reserve() -> reverse in place
# sort() -> sort table
