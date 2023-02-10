"""
9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad.
"""


#Programa para ingresar la información de ciertos empleados (en este caso 2) e insertarlo en un diccionario.


label = ("NOMBRE", "TELEFONO", "AÑO DE INGRESO A LA EMPRESA", "APELLIDO", "EDAD")
info = {}
dic = []
i = 4
while(i>=0):
    for data in label:
        info.__setitem__(data, input(f"INGRESE EL {data}\n --> "))
    dic.append(info)
    i-=3

print(dic)