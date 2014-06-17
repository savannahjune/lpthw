#defines a variable

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

#determines limit of how many cars can be driven
cars_not_driven = cars - drivers

#determines how many cars can be driven
cars_driven = drivers

#determines how many people can get a lift
carpool_capacity = cars_driven * space_in_a_car

average_passengers_per_car = passengers / cars_driven



print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study Drills: carpool_capacity was defined but car_pool_capacity was not