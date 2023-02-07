"""
9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad.
"""


label = ("NOMBRE", "TELEFONO")
info = {}
dic = []
i = 1
while(i>=0):
    for data in label:
        info.__setitem__(data, input(f"INGRESE EL {data}\n |"))
    dic.append(info)
    i-=1

print(dic)