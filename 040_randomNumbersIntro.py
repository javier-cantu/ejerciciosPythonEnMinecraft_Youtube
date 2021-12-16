# Ejercicio 040_randomNumbersIntro
# Introduccion a los numeros aleatorios
# Video en Youtube: 

# Nos conectamos
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# Modulo time
import time

# Ahora importamos el modulo random
# que nos da acceso a los numeros aleatorios
import random

time.sleep(3)

for i in range(10):
    # Con la funcion "randomint()" se regresa un numero aleatorio de tipo int, entre los valores que se pongan dentro de los ()
    num_random = random.randint(1, 100)
    mc.postToChat("El numero random es: " + str(num_random))
    print(num_random)
    time.sleep(1)

mc.postToChat("Fin de los numeros aleatorios")
