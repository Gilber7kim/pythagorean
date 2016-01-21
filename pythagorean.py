#Pythagorean Theorem
# a**2 + b**2 = c**2
# This is a step to get data about the first and the second sides from the user. Command float is a way to insert a number as raw_input.
a = float(raw_input("What is the length of the first side? -"))
b = float(raw_input("What is the length of the second side? -"))
#This is a process to define what c_squared is.
c_squared = a**2 + b**2
#Since the length of the hypotenuse is root a**2 + b**2, the expqonent (**) of the c_squared should be 0.5
c = c_squared**0.5
# This step shows the length of the hypotenuse.
print "The length of the hypotenuse is %r" % c
