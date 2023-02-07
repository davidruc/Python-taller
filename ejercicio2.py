"""
2. En la jerarquía de operadores, cuáles son los que más
prioridad tienen cuando el intérprete de Python los evalúa?
"""


a = 2
b = 3
c = 4

print(f"\n La principal jerarquía la tiene las operaciones dentro de paréntesis. \n ejemplo: {a}*({b}-{c}) = {a*(b-c)}, lo que es distinto a {a}*{b}-{c} = {a*b-c}. \n\n Luego tenemos la exponeciación: {a}**{b}-{c} = {a**b-c}, primero se ejecuta {a}**{b}={a**b} y luego resta {c}. \n\n Luego tenemos la multiplicación y división, módulo o residuo, división entera \n Algunos ejemplos de como se superponen con operaciones de menor jerarquía: \n multiplicación \t {a} * {b} + {c} = {a*b+c} \n división \t\t {a} / {b} + {c} = {a/b+c} \n módulo \t\t {a} % {b} + {c} = {a%b+c}  \n División entera\t {a} // {b} + {c} = { a//b+c} \n\n Luego tenemos los operadores de suma y resta, siempre se ejecutarán de últimos en una operación matematica. \n\n También existen los operadores de comparación <, <=, >, >=, !=, == que sirven para comparar elementos. \n\n Y por último los operadores lógicos and y or. Donde and se ejecutará primero.") 

