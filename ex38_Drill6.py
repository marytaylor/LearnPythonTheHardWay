#6. Find 10 examples of things in the real world that would fit in a list. Try
#   writing some scripts to work with them.
import collections

# Example 1 Students in a class
students = ['Dave', 'Chaz', 'Mary', 'Jason', 'Betsey', 'Peter']
print "Here is the class role call:", students

# Example 2 days in the week
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print "How many days are in a week?", len(days)

# Example 3
store_inventory = ['pants', 'shirt', 'shirt', 'pants', 'tank top', 'sunglasses',
'overalls', 'shirt', 'sunglasses']
counter = collections.Counter(store_inventory)
print "How many items of each are in store?"
print(counter)

# Example 4
categories = ['horror', 'comedy', 'romance', 'education', 'action', 'youth']
print "Here are the categories to choose from:"
categories.sort()
print categories

# Example 5
subarus = ['BRZ', 'Impreza', 'Legacy', 'Forester', 'Crosstrek', 'Outback']
subarus.append('WRX')
print "These are the current 2016 Subaru models:"
print subarus

# Example 6
vending_machine = ['chips', 'M&Ms', 'apple', 'granola bar']
print "What would you like to buy?", vending_machine
raw_input("> ")
print "Thank you!"

# Example 7
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'r', 'x', 'y', 'z']
alphabet.reverse()
print alphabet

# Example 8
list = ['1', '2', '3', '4']
print list.index('3')

# Example 9
beers = ['Red Oak', 'Hoegarden', 'Stella', 'Budweiser', 'Miller', 'Goose Island']
beers.pop(4)
print beers

# Example 10
num = []
for i in range(1, 10):
    num.append(raw_input('Enter a number: '))
print num
