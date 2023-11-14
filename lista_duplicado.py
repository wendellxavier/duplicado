# verificar a lista e retornar o numero duplicado, se não tiver irar retorna -1

listas = [
    [1,2,3,4,5,6,7,8,9,10],
    [1,1,3,4,5,6,7,3,1,10],
    [4,2,3,4,2,6,7,8,4,10],
    [7,2,3,8,5,6,7,8,9,2],
    [5,2,3,4,5,6,7,8,9,10],
    [6,2,3,4,5,6,2,8,9,5],
    [1,2,3,4,1,6,3,8,9,2],
    [8,2,4,4,5,6,7,8,9,7],
    [1,1,3,9,5,6,7,8,9,10],
]

def encontrar_duplicado(parametro_lista):
    numeros_checados = set()
    primeiro_duplicado = -1
    for numero in parametro_lista:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)


    return primeiro_duplicado

for lista in listas:
    print(lista, encontrar_duplicado(lista))