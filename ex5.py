name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
     age, height, weight, age + height + weight)

#Calculate height from inches to centimeters
height_in_cm = height * 2.54

#Calculate weight from pounts to kilograms
weight_in_kg = weight * 0.453592

print "Zed's height in centimeters is %o." % height_in_cm
print "Zed's weight in kilograms is %o." % weight_in_kg
