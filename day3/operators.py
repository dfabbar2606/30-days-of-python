age = 17
float = 1.84
complex =  2 + 3j

base = int(input("dame la base del triangulo:"))
altura = int(input("dame la altura del triangulo:"))
area_del_triangulo = 0.5*base*altura
print(area_del_triangulo)

a = int(input("dame el lado a:"))
b = int(input("dame el lado b:"))
c = int(input("dame el lado c:"))
perimetro_del_triangulo = a+b+c
print(perimetro_del_triangulo)

longitud = int(input("dame la longitud del rectangulo:"))
ancho = int(input("dame el ancho del rectangulo:"))
area_del_rectangulo = longitud*ancho
print(area_del_rectangulo)
perimetro_del_rectangulo = 2*(longitud+ancho) 
print(perimetro_del_rectangulo)

radio=int(input("dame el radio del circulo:"))
pi = 3.14
area_del_circulo= pi*radio*radio
print(area_del_circulo)
circuferencia = 2*pi*radio
print(circuferencia)

x = int(input("dame el valor de x:"))
m = 2
y = m*x-2
print(y)

x = 2
y = 2
m = (y*2-y*1)/(x*2-x*1)
print(m)

x = 6
y = 10
m=(y*2-y*1)/(x*2-x*1)
print(m)

import math
x_1 = 2
x_2 = 6
y_1 = 2
y_2 = 10
d = math.sqrt(((x_2 - x_1)**2 + (y_2 - y_1)**2))
print(d)
