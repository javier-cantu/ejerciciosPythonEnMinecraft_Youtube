# Ejercicio 036_introLoops
# Introduccion a los loops en Python
# Video en Youtube: 

# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# Necesitamos un bloque
# 251:14 es concreto rojo, lo que uso en eje x
blockType = 251,15

# Se obtiene la posicion del jugador con "getTilePos()" y se asigna a la variable "pos"
# Se manda al char la posicion
# Se hace una pause de 1 segundo
pos = mc.player.getTilePos()
mc.postToChat("Posicion inicial " + str(pos))
time.sleep(1)

# Se asignan a xi, yi, zi, los componentes de la posicion en cada eje. 
xi = pos.x
yi = pos.y
zi = pos.z

# Esto es una "for loop" que se ejecutara 16 veces
# Cada vez que se de una loop se construira un bloque
# Y se actualiza el valor de xi para pasar al siguiente bloque. 
for x in range(16):
    mc.setBlock(xi,yi-1,zi, blockType)
    xi = xi + 1
    time.sleep(0.2)
