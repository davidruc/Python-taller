"""
Escriba un bloque cualquiera de código en Python en donde
utilice 2 condicionales (if) anidados.
"""

#programa para determinar si se insertó un valor numerico que se encuentre entre dos constantes matemáticas

a = input("Escoja un número del 1 al 4: ")
a = float(a)
pi = 3.1416
e = 2.71


if a <= pi:
    print(f" Tu numero:{a}, es menor que pi={pi}")
    if a >= e:
        print(f"Tu numero:{a}, se encuentra entre pi y euler")  
else:
    print(f"elegiste un numero mayor que pi = {pi}")    