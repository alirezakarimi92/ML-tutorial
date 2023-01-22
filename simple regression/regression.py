# here we start to create some code in regression
from numpy import sqrt 
# for every ML code we need 4 Item:
# 1. the most importatn item: a Data set 
# 2. a hypothesis which is a parametric function & our task is finding its parameters
# 3. a cost function which make a relation between "Data Set" & "Parameters of hypothesis"
# 4. an optimization method which optimize the cost function
print ('Happy birthday the most real man in the life')
a=int (input ('a as coeficient of 2nd order equation: '))
b=int(input ('b as coeficient of 2nd order equation: '))
c=int(input ('c as coeficient of 2nd order equation: '))

delta = b**2 - 4*a*c

if delta == 0:
    print("this equation has just one root: ", -b/(2*a))
elif delta< 0:
    print("this equation has no real roots")
else:
    print("this equation has two roots: " , (-b + sqrt(delta))/(2*a))
    print("and" , (-b - sqrt(delta))/(2*a))  
