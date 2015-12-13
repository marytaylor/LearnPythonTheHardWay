#Here I am declaring how many cars there are
cars = 100
# This is how many seats in each car
space_in_a_car = 4
#This is how many drivers there are and there can only be 1 driver per a car.
drivers = 30
#This is how many people that can ride in a car and this does not count the drivers
passengers = 90
#There are not enough drivers for all of the cars so I need to find out how many cars will not be driven with this
cars_not_driven = cars - drivers
#It looks like 30 of the cars are driveable
cars_driven = drivers
#This is how many seats are avaliable in the cars that can be driven
carpool_capacity = cars_driven * space_in_a_car
#If we were to put everyone in a car, 1 by 1 per each car.  Only 3 people would be in each car.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
