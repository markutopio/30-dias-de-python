
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

-1
len(it_companies)

-2
it_companies.add("Twitter")

-3
it_companies.update(["Tiktok", "Omegle", "Linux"]) #si no se pone con [] las companies salen desordenadas en el set

-4
it_companies.remove("Twitter")

-5
C = A.union(B)
print(C)

-6
A.intersection(B)

-7
A.issubset(B)

-8
A.isdisjoint(B)

-9 
print(A.update(B) and B.update(A))

-10
A.symmetric_difference(B)

-11
del A
del B
del it_companies
del age