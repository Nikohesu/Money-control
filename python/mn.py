from flask import Flask
#imprimir nombre
print ("Jhoan Nicolas")
#suma de dos variables
def suma(a,b):
    return a+b
#multiplicacion de tres varibles
suma(5,3)
def mul(a,b,c):
    return a*b*float(c)
mul(4,8,2.5)
#divicion
def div(a,b):
    return float(a)/float(b)
div(3.5,9.6)
#lista
obj_class= ["computadores","estudiantes","tablero"]

#tupla
valb = (0,1)

#diccionario

rol= {"jhoan": "estudiante","diana":"profesor"}

#set
myfriends = set(["ruben","stefanny","jennifer"]        )


#funcion
def mostrar ():
    return print("hello world")

mostrar()