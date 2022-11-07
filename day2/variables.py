from __future__ import division
from cProfile import run
from cmath import exp
from math import remainder
from numpy import product
from regex import R


1
#Day 2: 30 Days of python programming #1.2
first_name = "marco" #1.3
last_name = "palma" #1.4
full_name = "marco palma" #1.5
country = "spain" #1.6
city = "jerez de la frontera" #1.7
age = "17" #1.8
year = "2022" #1.9
is_married = "false" #1.10
is_true = "yes" #1.11
is_light_on = "no" #1.12
a1, a2, a3, = 6, 4, 2 #1.13

2.1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a1, a2, a3))

2.2
print(len(first_name))

2.3
print(len(first_name))
print(len(last_name))

2.4
num_one = 5
num_two = 4

#2.4.1
total = num_one + num_two

#2.4.2
diff = num_one + num_two

#2.4.3
product = num_two * num_one

#2.4.4
division = num_one / num_two

#2.4.5
remainder = num_two / num_one

#2.4.6
exp = num_one**num_two

#2.4.7
floor_division = num_one//num_two

#2.5
#2.5.1

radio = 30
area_of_circle = 3.1416 * radio ** 2
print(area_of_circle)

#2.5.2

circumference_of_circle = 3.1416 * 2 * radio
print(circumference_of_circle)

#2.5.3
r=input("¿cual es el radio")
radioA=int(r)
area=3.1416 * radioA ** 2
print(area)

#2.6
