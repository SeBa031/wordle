# Wordle

# Importar libreria random
import random

# Definimos una lista de palabras de 5 letras a adivinar 
lista_de_palabras = ["PERRO", "CABRA", "HUEVO", "SILLA", "LIMON", "FRUTA", "GORDO", "FLACO"]

# Seleccionarmos una palabra de la lista de palabras de manera aleatoria
palabra_secreta = random.choice(lista_de_palabras)

# Definimos la cantidad de intentos 
cantidad_de_intentos = 6

# Definimos la cantidad de letras que debe tener la palabra a ingresar
cantidad_de_letras = 5

# Imprimir mensaje de bienvenida
print("WORDLE EN ESPAÑOL (5 LETRAS)")

# Empezar el proceso de pedir palabras y compararlas
for numero_de_intento in range(cantidad_de_intentos):
    # Variable para entrar y salir del bucle
    bandera = True

    # Se pide al usuario que ingrese una palabra mientras que la palabra tenga una cantidad de letras distinta a 5
    while bandera:
        # Pedimos al usuario que ingrese una palabra
        intento = input(f"\n [Intento Nro: {numero_de_intento + 1} / {cantidad_de_intentos}] --> Ingrese una palabra: ")

        # Verificamos si la palabra tiene exactamente 5 letras
        if len(intento) != 5:
            # Si no tiene exactamente 5 letras se imprime un mensaje y se sigue repitiendo el bucle solicitando una palabra 
            print("La palabra ingresada debe tener 5 letras")
        
        else:
            # Si tiene exactamente 5 letras se cambia el valor de bandera y se sale del bucle
            bandera = False

    # Creamos una variable que guarda si la respuesta es correcta, parcialmente correcta o incorrecta
    letras_verificadas = []

    # Empezamos las comparaciones entre la palabra ingresada y la palabra secreta
    for i in range(cantidad_de_letras):
        if intento[i].upper() == palabra_secreta[i]:
            letras_verificadas.append("✅") # Si la letra esta en la posicion correcta se agrega verde a letras_verificadas
        elif intento[i].upper() in palabra_secreta: 
            letras_verificadas.append("🟨") # Si la respuesta no esta en la posicion correcta, pero la letra existe en la palabra se agrega amarillo a letras_verificadas
        else:
            letras_verificadas.append("🟥") # Si la letra no existe en la palabra se agrega rojo a letras_verificadas

    # Se imprime el resultado del intento
    print(f"La palabra que ingresaste fue '{intento.upper()}' y tus aciertos son --> {''.join(letras_verificadas)}")

    # Verificar si la palabra ingresada es igual a la palabra secreta
    if intento.upper() == palabra_secreta:
        print("\nGanaste")
        break

# Si se llega al limite de intentos imprimir un mensaje de que diga perdiste
else:
    print(f"\nTe quedaste sin intentos. Perdiste --> La palabra era {palabra_secreta}")
