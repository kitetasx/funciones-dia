# Ejemplo para calcular el area del triangulo

# Variables de entrada
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

#proceso
def calcularAreaTriangulo(b,a):
    area =(b*a)/2
    return area
# Invocar la funcion
resultado = calcularAreaTriangulo(base,altura)
#Salida
print(f"El area del triangulo cuya base {base} y altura {altura} es: {resultado}")

#Funcion con argumentos predeterminados
def my_funcion(country = "Colombia"):
    print("I am from"+country)

 #Invocar la funcion
my_funcion()
my_funcion("Sweden")

# Argumentos arbitrarios
def mostarEstudiantes(*args):
    print("El estudiante: "+args[2])

# Invocar la funcion
mostarEstudiantes("Emil","Tobias","Linus","Bill","Andres")


def mostrarCarros(carro1, carro2, carro3):
    print("El carro es: " + carro2)
mostrarCarros(carro1 = "bmw", carro3 = "ferrari", carro2 = "ford")

def mostrarCliente(**kwargs):
    print("Su apellido es: " + kwargs["apellido"])

mostrarCliente(nombre = "Tobias", apellido = "Refesnes")

def mifuncion():
    pass

x = min(5, 10, 15)
y = max(5, 10, 15)
print(x)
print(y)


num1 = pow(7, 4)
print(num1)

import math
num2 = math.sqrt(34)
print(num2)

import math
num3 = math.ceil(7.8)
num4 = math.floor(7.8)
print(num3)# returns 8
print(num4) #resturns 7

