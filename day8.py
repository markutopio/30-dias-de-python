-1
dog = {}

-2
dog["Name"] = "Carlota"
dog["Color"] = "Grey and black"
dog["Breed"] = "Pug"
dog["legs"] = "4 and short legs"
dog["Age"] = "10"
print(dog)

-3
student_dictionary = {}
student_dictionary["First_name"] = "Marco"
student_dictionary["Last_name"] = "Palma"
student_dictionary["gender"] = "Male"
student_dictionary["Age"] = "17"
student_dictionary["marital status"] = "currently alone"
student_dictionary["skills"] = "Have patience"
student_dictionary["country"] = "Spain"
student_dictionary["city"] = "Jerez de la Frontera"
student_dictionary["address"] = "11592, 198"
print(len(student_dictionary))

-4
print(student_dictionary["skills"])

-5
print(type(student_dictionary["skills"]))

-6
student_dictionary["skills"] = "Also runs fast"

-7
key = student_dictionary.keys()

-8
values = student_dictionary.values
print(values)

-9
print(student_dictionary.items())

-10
student_dictionary.pop("gender")

-11
del student_dictionary
