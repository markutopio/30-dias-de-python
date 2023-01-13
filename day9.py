-1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are qualified to drive at this age")

else:
    print("Sorry, you have to get older, so you will get the permission")

-2
otherage = int(input("Enter your age : "))
my_age  =17

if otherage == my_age:
    print("We have the same age!")

elif otherage > my_age:
    print("You are older than me")

elif otherage < my_age:
    print("Im older than you")


-3
a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

if a < b:
    print("b is bigger")

elif a > b:
    print("a is bigger")

elif b == a:
    print("They are the same number")

-4
nota = int(input("Type your mark: "))

if nota in range(0,49):
    print("Suspenso")

elif nota in range(50,59):
    print("Suficiente")

elif nota in range(60,69):
    print("Bien")

elif nota in range(70,79):
    print("Notable")

elif nota in range(80,89):
    print("Notable alto")

elif nota in range(90,100):
    print("Sobresaliente")

-5
mes = input("Type a month: ")


if mes in ["march", "april", "may"]:
    print("Spring")

elif mes in ["june", "july", "august"]:
    print("Summer")

elif mes in ["septiembre", "october", "november"]:
    print("Autumn")

elif mes in ["december", "january", "february"]:
    print("Winter")


-6
fruits = ["banana", "orange", "mango", "lemon"]

fruta = input("Type a fruit: ")

if fruta in fruits:
    print("Already exists in the list")

else:
    print("That does not appear in the list")