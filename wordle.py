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