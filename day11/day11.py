import math
-1
def add_two_numbers(a,b):
    return a + b

-2
def area_of_a_circle(r):
    return 3.1416 * r**2
    
-3
def add_all_nums(aas):
    for i in aas:
        aas = aas + 1
        print(aas)

-4
def from_celsius_to_fahrenheit(celsius):
    return(celsius * 9 / 5) + 32

-5
def check_season(mes):
    if mes in ["march", "april", "may"]:
        return("Spring")
    
    elif mes in ["june", "july", "august"]:
        return("Summer")

    elif mes in ["septiembre", "october", "november"]:
        return("Autumn")

    elif mes in ["december", "january", "february"]:
        return("Winter")



-8
def print_list(lss):
    lss = []
    for i in lss:
        print(i)

-9
def reverse_list(lia):
    return lia[::-1]


-10
def capitalize_list_items(x):
    for i in x:
        x[x.index(i)] = i.capitalize()

-11
def add_item(lss, ff):
    lss.append(ff)
    return lss

-12
def remove_item(lsx,fa):
    lsx.remove(fa)
    return lsx

-13
def sum_of_numbers(d):
    sum_of_numbers = 0
    for i in range(d+1):
        sum_of_numbers = sum_of_numbers + 1
    return sum_of_numbers


-1
def is_prime(b):
    if b <= 1:
        return False
    
    div = math.floor(math.sqrt(b))
    for i in range(2, 1+ div):
        if b % i == 0:
            return False
        
    return True


-2
def check_a_list(lsi):
    return len(set(lsi)) == len(lsi)
