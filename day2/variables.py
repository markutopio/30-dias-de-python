
from cProfile import run
from calendar import c

#Day 2 of 30 Days of python


first_name="Marco"
last_name="De La Rosa"
full_name="Marco_Palma"
country="España"
city="Jerez De La Frontera"
age=17
year=2022
is_married="no"
is_true="yes"
is_light_on="no"
letters="c","d"

#level 2

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
print(type(letters))


print(len(first_name))
print(len(last_name))



num_one=5 
num_two=4

num_total=num_one+num_two
print(num_total)

num_diff=num_one-num_two
print(num_diff)

num_product=num_one * num_two
print(num_product)

num_divide=num_one/num_two
print(num_divide)

num_exp=num_two**num_one
print(num_exp)

division_floor=num_one//num_two
print(division_floor)


radius=30
area_of_circle=3.14 * radius**2
print(area_of_circle)

circumference_of_circle=2 * 3.14 * radius
print(circumference_of_circle)


r=input("¿cual es el radio?")
r2= int(r)
area=3.14 * r2 ** 2
print(area)


help('keywords')