numbers = 1,2,3,4,5,6,7,8,9,10

-1
for number in numbers:
    print(number)

count = 0
while count <= 10:
    print(count)
    count = count + 1


-2
new_numbers = 10,9,8,7,6,5,4,3,2,1,0

for number in new_numbers:
    print(number)

new_count = 10
while new_count >= 0:
    print(new_count)
    new_count  = new_count - 1


-3
hags = "#"

for i in range(1,9):
    i = i * hags
    print(i)

-4
hags_2 = "#"

for i in range(1,9):
    for r in range(1,9):
        print(hags_2, end="")


-5
for i in range(0,11):
    print(i, "x", i, "=", i*i)


-6
list = ["Python", "Numpy", "Pandas", "Diango", "Flask"]

for contents in list:
    print(contents)

-7
for i in range(0,101):
    print(i)


-8
for num in range(0,5005):
    num = num + 1
    print("All is ", num)


-9
listt = ["Finland, Iceland, Ireland, the Netherlands, Poland, Switzerland, Thailand, New Zealand"]

for country in listt:
    if "land" in country:
        print(country)
