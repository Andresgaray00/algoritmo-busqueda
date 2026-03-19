datos = [0, 2, 5, 8, 11, 13, 15, 18, 20, 22, 25, 28, 31, 33, 36, 39, 40, 45, 47]

def buscar_numero(datos, numero):
    contador = 0
    encontrado = False

    while contador < len(datos):
        if datos[contador] == numero:
            encontrado = True
            break
        contador = contador + 1

    return encontrado


def pedir_numero():
    while True:
        entrada = input("Ingresa un numero positivo: ")

        if entrada.isdigit():
            numero = int(entrada)
            return numero
        else:
            print("Entrada invalida. Intenta nuevamente.")


seguir = True

while seguir:
    numero = pedir_numero()

    encontrado = buscar_numero(datos, numero)

    if encontrado:
        print("El numero fue encontrado")
    else:
        print("El numero no esta en la lista")

    opcion = input("¿Quieres buscar otro numero? (si/no): ")

    if opcion.lower() == "no":
        seguir = False