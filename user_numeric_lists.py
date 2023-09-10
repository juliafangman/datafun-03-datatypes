"""
Modify this docstring.

"""


#Task 3. Numeric Lists

# import some standard modules first - how many can you make use of?
import math

import statistics
import util_datafun_logger

#List 1  #List of ages of women's tennis players in the US Open 2023
list_1 = [28,23,22,34,25,33,26,30,26,29,27,25,33,22,29,33,25,27,29,26,32,36]

#Listx #the year's Djokovic has played
list_X = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
#Listy #the amount of games Djokovic has won each year
list_Y = [41, 42, 55, 41, 54, 53, 32, 65, 82, 61, 74, 75, 70, 61, 78, 64]

#the mean, mode, median, standard deviation, & variance of List 1
mean = statistics.mean(list_1)
mode = statistics.mode(list_1)
median = statistics.median(list_1)
std_deviation = statistics.stdev(list_1)
variance = statistics.variance(list_1)

print(f"Mean:{mean}")
print(f"Mode:{mode}")
print(f"Median:{median}")
print(f"Standard Deviation:{std_deviation}")
print(f"Variance:{variance}")

#Calculate the Correlation between listx and listy
mean1 = sum(list_X) / len(list_X)
mean2 = sum(list_Y) / len(list_Y)

numerator = sum((x - mean1) * (y-mean2) for x, y in zip(list_X, list_Y))
denominator1 = sum((x-mean1) ** 2 for x in list_X)
denominator2 = sum((y-mean2) ** 2 for y in list_Y)

correlation_coefficient = numerator / ((denominator1 * denominator2) ** 0.5)
print(f"Pearson Correlation Coefficient: {correlation_coefficient}")

#Calculate the slope and intercept of the best fit line
slope = (list_Y[2] - list_Y[1]) / (list_X[2] - list_X[1])
print(f"Slope:{slope}")

Y_intercept = (list_Y[2]) - (slope * list_X[2])
print(f"Y intercept:{Y_intercept}")

#Set a future time = 15
list_X.append(list_X[15]+15)

#Predict they y value at the future time y=mx+b where m is the slope and by is the y intercept
list_Y.append((slope * list_X[16]) + Y_intercept)

#Lists 3. Lists - Using Python Built-in Functions
import math
import statistics

minX = min(list_X)
maxX = max(list_X)
lenX = len(list_X)
sumX = sum(list_X)
meanX = statistics.mean(list_X)
setX = set(list_X)
sortedX = sorted(list_X)
sortedXrev = sorted(list_X, reverse=True)

print(f"min{minX}")
print(f"max{maxX}")
print(f"len{lenX}")
print(f"sum{sumX}")
print(f"mean{meanX}")
print(f"set{setX}")
print(f"sorted{sortedX}")
print(f"sorted{sortedXrev}")

#Lists 4. List Methods

#lst #Number of aces by Rafael Nadal from 2003 to 2022
lst = [37,57,219,240,238,283,219,310,267,160,221,181,222,116,283,124,310,157,116,225]

lst.append(12) #aces in 2023
lst2 = [3,0,0] #My estimate of the number of aces for Nadal for 2024 to 2026
lst.extend(lst2)
lst.insert(2, 97)
lst.remove(37)
lst.count(310)
lst.sort()
lst.sort(reverse=True)
copied_lst = lst.copy()
first_item = lst.pop(0)
last_item = lst.pop(22)

#List 5. List Transformations - Using filter() and map()
even_numbers = list(filter(lambda x: x % 2 == 0, lst))
print(even_numbers)

import math
def cuberoot(x):
    return (x ** (1/3))

cuberoot_lst = map(cuberoot, lst)
print(cuberoot_lst)

def volume(x):
    return (x ** 3)
volume_lst = map(volume, lst)
print(volume_lst)

#Lists 6. List Transformations - Using List Comprehension
more_than_100 = [x for x in lst if x>100]
print(more_than_100)

triple_value = [x*3 for x in lst]
print(triple_value)


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Replace this with calls to your functions." )



