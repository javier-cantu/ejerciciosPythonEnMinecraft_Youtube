# 041_randomCubes.py
# Usamos numeros aleatorios para determinar los lados de un cubo
# Se construyen varios cubos de diferentes tamaños con una "for loop"
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

# Se obtiene la posicion del jugador para construir cerca.
pos_jugador = mc.player.getTilePos()
# Se asignan los valores iniciales a 3 variables
xi = pos_jugador.x
yi = pos_jugador.y
zi = pos_jugador.z

# Se modifican los valores un poco para que no aparescan
# en el mismo ligar que esta el jugador.
xi = xi + 5
yi = yi + 5
zi = zi + 5

# Material
blockType = 5

# Loop que se repetira 10 veces
for i in range(10):
    # Generamos 3 valores random entre 1 y 10
    # Asignarlos a 3 variables. 
    lado_1 = random.randint(1, 10)
    lado_2 = random.randint(1, 10)
    lado_3 = random.randint(1, 10)
    mc.setBlocks(xi, yi, zi, xi+lado_1, yi + lado_2, zi + lado_3, blockType)
    # Avanza z en 15
    zi = zi + 15
    time.sleep(1)
