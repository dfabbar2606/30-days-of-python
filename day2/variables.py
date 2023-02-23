'Day 2: 30 Days of python programming'
firstname = 'Daniel'
lastname = 'Fabregat Barragán'
fullname = 'Daniel Fabregat Barragán'
country = 'España'
city = 'Jerez'
age = 17
year = 1958
is_married = False
is_true = True
is_light_on = True
firstname, lastname, fullname, country, age, is_married = 'Daniel', 'Fabregat Barragán', 'Daniel Fabregat Barragán', 'España', 17, False
print(firstname, lastname, country, age, is_married)
print('firstname:', firstname)
print('lastname: ', lastname)
print('country: ', country)
print('age: ', age)
print('married: ', is_married)


print(type(age))
print(type(firstname))
print(type(country))
print(type(lastname))
print(type(is_married))
print(type(fullname))
print(type(city))
print(type(year))
print(type(is_true))
print(type(is_light_on))

print(len(firstname))
print(len(firstname)), len(lastname)

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

radio = int(input("dame el radio_del_cuadrado:"))
radio_del_cuadrado = radio * radio 
pi = 3,14
area_del_circulo = pi * radio_del_cuadrado
print(area_del_circulo)

circuferencia_del_circulo = 2 * pi * radio
print(circuferencia_del_circulo)

firstname = input("¿cual es tu nombre?")
lastname = input("¿cuales son tus apellidos?")
country = input("¿De que pais eres?")
age = input("cual es tu edad?")

print("hola,mi nombre es", firstname, lastname, " soy de ",country, "y tengo", age, "años"  )