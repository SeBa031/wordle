# WORDLE
### Reglas del juego

El juego te pedira que ingreses una palabra que tenga exactamente 5 letras, en caso de ingresar una palabra con mas de 5 letras o menos de 5 letras saltara un mensaje que diga *La palabra ingresada debe tener 5 letras*, este intento fallido no consumira un intento (tienes 6 intentos en total para adivinar la palabra).

Una vez ingresada la palabra de 5 letras esta sera comparada con la palabra secreta, y se retornara una serie de emojis donde, el color verde representa que la letra esta en la posicion correcta, el color amarillo representa que la letra existe en la letra pero esta en la posicion incorrecta, y el color rojo representa que la letra no existe en la palabra.

Si la palabra ingresada coincida con la palabra secreta se termina el juego y salta un mensaje de *Ganaste* en caso de que la palabra no coincida y te quedes sin intentos el juego acaba y saltara el mensaje de *Perdiste*.