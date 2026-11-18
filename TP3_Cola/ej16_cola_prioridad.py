# Cola de prioridad
'''
16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la siguiente situación:
a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
c. cargue dos documentos del staff de TI.
d. cargue un documento del gerente.
e. imprima los dos primeros documentos de la cola.
f. cargue dos documentos de empleados y uno de gerente.
g. imprima todos los documentos de la cola de impresión.
'''

from ED_heap import HeapMax

cola_impresion = HeapMax()

# --------- CREACIÓN DE FUNCIONES PARA FORMATO --------- #

class Color:
    RESET   = '\033[0m'
    NEGRITA = '\033[1m'
    CIAN    = '\033[96m'
    ROJO    = '\033[38;2;171;29;29m'     #AB1D1D
    AMARILLO= '\033[38;2;227;187;45m'    #E3BB2D
    AZUL    = '\033[38;2;0;48;176m'      #0030B0
    VERDE   = '\033[38;2;12;120;0m'      #0C7800
    VIOLETA = '\033[38;2;88;31;122m'     #581F7A

def print_seccion(titulo, ancho=140, relleno="-", color=Color.VERDE):
    print(f'\n{color}{f" {titulo} ".center(ancho, relleno)}{Color.RESET}')

def print_seccion_extra(titulo, ancho=140, relleno=" ", color=Color.VERDE):
    print(f'{color}{f" {titulo} ".center(ancho, relleno)}{Color.RESET}')

#################################################  EJECUCIÓN DE PRUEBAS DEL ENUNCIADO  #################################################
print(f'\n{Color.CIAN}{f' EJERCICIO 16: COLA DE IMPRESIÓN '.center(140, "=")}{Color.RESET}')

# a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
print_seccion('a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'Documentos cargados: ')

documento_1 = ['Informe de ventas', 1]
cola_impresion.arrive(documento_1[0], documento_1[1])
print(f' → Documento #1: {documento_1[0]} | Prioridad: {documento_1[1]}')

documento_2 = ['Planilla de gastos', 1]
cola_impresion.arrive(documento_2[0], documento_2[1])
print(f' → Documento #2: {documento_2[0]} | Prioridad: {documento_2[1]}')

documento_3 = ['Carta para cliente', 1]
cola_impresion.arrive(documento_3[0], documento_3[1])
print(f' → Documento #3: {documento_3[0]} | Prioridad: {documento_3[1]}')

# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
print_seccion('b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if cola_impresion.size() > 0:
    documento = cola_impresion.attention()
    print(f'  → {documento[1]}')
else:
    print(f'  → No hay elementos en la cola de impresión.')

# c. cargue dos documentos del staff de TI.
print_seccion('c. cargue dos documentos del staff de TI.')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'Documentos cargados: ')

documento_4 = ['Manual de redes', 2]
cola_impresion.arrive(documento_4[0], documento_4[1])
print(f' → Documento #4: {documento_4[0]} | Prioridad: {documento_4[1]}')

documento_5 = ['Script backup', 2]
cola_impresion.arrive(documento_5[0], documento_5[1])
print(f' → Documento #5: {documento_5[0]} | Prioridad: {documento_5[1]}')

# d. cargue un documento del gerente.
print_seccion('d. cargue un documento del gerente.')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'Documento cargado: ')

documento_6 = ['Presupuesto anual', 3]
cola_impresion.arrive(documento_6[0], documento_6[1])
print(f' → Documento #6: {documento_6[0]} | Prioridad: {documento_6[1]}')

# e. imprima los dos primeros documentos de la cola.
print_seccion('e. imprima los dos primeros documentos de la cola.')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if cola_impresion.size() > 0:
    documento = cola_impresion.attention()
    print(f'  → {documento[1]}')
else:
    print(f'  → No hay elementos en la cola de impresión.')

if cola_impresion.size() > 0:
    documento = cola_impresion.attention()
    print(f'  → {documento[1]}')
else:
    print(f'  → No hay elementos en la cola de impresión.')

# f. cargue dos documentos de empleados y uno de gerente.
print_seccion('f. cargue dos documentos de empleados y uno de gerente.')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
print(f'Documentos cargados: ')

documento_7 = ['Acta reunión', 1]
cola_impresion.arrive(documento_7[0], documento_7[1])
print(f' → Documento #7: {documento_7[0]} | Prioridad: {documento_7[1]}')

documento_8 = ['Listado de clientes', 1]
cola_impresion.arrive(documento_8[0], documento_8[1])
print(f' → Documento #8: {documento_8[0]} | Prioridad: {documento_8[1]}')

documento_9 = ['Plan estratégico', 3]
cola_impresion.arrive(documento_9[0], documento_9[1])
print(f' → Documento #9: {documento_9[0]} | Prioridad: {documento_9[1]}')

# g. imprima todos los documentos de la cola de impresión.
print_seccion('g. imprima todos los documentos de la cola de impresión.')
print(f'{Color.VIOLETA}Resultado:{Color.RESET}')
if cola_impresion.size() > 0:
    while cola_impresion.size() > 0:
        documento = cola_impresion.attention()
        print(f'  → {documento[1]}')
else:
    print(f'  → No hay elementos en la cola de impresión.')

print(f'\n{Color.CIAN}{f" FIN DE EJECUCIÓN DEL PROGRAMA ".center(140, "=")}{Color.RESET}')