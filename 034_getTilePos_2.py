# Ejercicio 034_getTilePos_2 getTilePos obtiene la posicion del jugador, la manda al chat, y construye un bloque
# Video en Youtube: https://youtu.be/v38Lor4GSoQ

# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# Con "mc.player.getTilePos()" se obtiene la posicion del "tile" o block donde se encuentra el jugador.  
# Esta funcion regresa la posición como un vector
# La "tile position" se guarda como un integer que representa la posición exacta de un block o "tile" en el mundo. 
# Se puede separar este vector en valores individuales para cada eje, x, y, z. 
# https://pimylifeup.com/minecraft-pi-edition-api-reference/

# Se le asigna el valor del vector a la variable "pos"
pos = mc.player.getTilePos()

# Se asigna un material para el block
blockType1 = 1

# Se manda al chat el valor de "pos"
mc.postToChat(pos)
# Pausa de 1 segundo
time.sleep(1)

# Luego separamos el vector en 3 valores
# Con pos.x se accesa al componente X del vector
# hacemos lo mismo con cada eje y se asiga cada valor a una variable diferente
# xi, yi, zi, representan los valores iniciales
xi = pos.x
yi = pos.y
zi = pos.z

# Se manda al chat la posicion del blocke donde estan los pies del jugador. 
mc.postToChat("La posicion del jugador es: = " + " X = " + str(xi) + "  Y = " +str(yi) + "  Z = " + str(zi))

# Se construye un block en esa misma posición
mc.setBlock(xi, yi, zi, blockType1)
