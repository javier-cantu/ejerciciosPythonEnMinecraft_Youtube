# Ejercicio 033_getTilePos_intro getTilePos obtiene la posicion del jugador y la manda al chat
# Video en Youtube: 

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
mc.postToChat("La posición del jugador es: = " + " X = " + str(x) + "  Y = " +str(y) + "  Z = " + str(z))
