"""
10. En su casa le solicitan que realice un algoritmo en Python,
que permita calcular el valor a pagar por concepto de
energía eléctrica. Los datos que se conocen son los
siguientes:
- Mes de consumo - Valor kw
-Total kw consumido en el mes - estrato
"""


KwPORMES_X_Estrato = [1, 224, 320, 400, 560, 780, 1200]
Estrato = int(input(f"Cuál es su estrato?: "))
MesesXPagar = int(input(f"Cuál es el número de meses que debe cancelar?: "))
KwConsumidos = int(input(f"Cuantos kw consumió en esos meses?: "))
costoXestrato = KwPORMES_X_Estrato[Estrato]
calculoValor = costoXestrato*KwConsumidos*MesesXPagar

print(f"Usted debe cancelar: ${calculoValor} pesos")