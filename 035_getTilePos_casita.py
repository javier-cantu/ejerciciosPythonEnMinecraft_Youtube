# Ejercicio 034_getTilePos_2 getTilePos obtiene la posicion del jugador, la manda al chat, y construye un bloque
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




# Materiales para usar
# A todos se les dio un nombre
# Para no tener que usar solo numeros
cobblestone = 4
oakwoodlog = 17
oakwoodplank = 5
glass = 20
aire = 0
oakwoodstairs = 53
glasspane = 102
torch = 50

##########################################
# Primero  determinamos la coordenada incial
# Este sera nuestro punto de referencia
x = -10
y = 4
z = -10

time.sleep(1)
##########################################
# Construccion bloque por bloque
# Tenemos que tener y ver un plano 
# con solo la imaginacion es dificil pero posible

# Capa o Nivel 1
mc.setBlock(x+0, y, z, 41)
mc.setBlock(x+1, y, z, cobblestone)
mc.setBlock(x+2, y, z, cobblestone)
mc.setBlock(x+3, y, z, cobblestone)
mc.setBlock(x+4, y, z, oakwoodlog)

mc.setBlock(x+0, y, z-1, cobblestone)
mc.setBlock(x+1, y, z-1, oakwoodplank)
mc.setBlock(x+2, y, z-1, oakwoodplank)
mc.setBlock(x+3, y, z-1, oakwoodplank)
mc.setBlock(x+4, y, z-1, cobblestone)

mc.setBlock(x+0, y, z-2, cobblestone)
mc.setBlock(x+1, y, z-2, oakwoodplank)
mc.setBlock(x+2, y, z-2, oakwoodplank)
mc.setBlock(x+3, y, z-2, oakwoodplank)
mc.setBlock(x+4, y, z-2, cobblestone)

mc.setBlock(x+0, y, z-3, cobblestone)
mc.setBlock(x+1, y, z-3, oakwoodplank)
mc.setBlock(x+2, y, z-3, oakwoodplank)
mc.setBlock(x+3, y, z-3, oakwoodplank)
mc.setBlock(x+4, y, z-3, cobblestone)

mc.setBlock(x+0, y, z-4, oakwoodlog)
mc.setBlock(x+1, y, z-4, cobblestone)
mc.setBlock(x+2, y, z-4, cobblestone)
mc.setBlock(x+3, y, z-4, cobblestone)
mc.setBlock(x+4, y, z-4, oakwoodlog)



# Capa o Nivel 2
mc.setBlock(x+0, y+1, z, oakwoodlog)
mc.setBlock(x+1, y+1, z, cobblestone)
mc.setBlock(x+3, y+1, z, cobblestone)
mc.setBlock(x+4, y+1, z, oakwoodlog)

mc.setBlock(x+0, y+1, z-1, cobblestone)
mc.setBlock(x+4, y+1, z-1, cobblestone)

mc.setBlock(x+0, y+1, z-2, cobblestone)
mc.setBlock(x+4, y+1, z-2, cobblestone)

mc.setBlock(x+0, y+1, z-3, cobblestone)
mc.setBlock(x+4, y+1, z-3, cobblestone)

mc.setBlock(x+0, y+1, z-4, oakwoodlog)
mc.setBlock(x+1, y+1, z-4, cobblestone)
mc.setBlock(x+2, y+1, z-4, cobblestone)
mc.setBlock(x+3, y+1, z-4, cobblestone)
mc.setBlock(x+4, y+1, z-4, oakwoodlog)



# Capa o Nivel 3
mc.setBlock(x+0, y+2, z, oakwoodlog)
mc.setBlock(x+1, y+2, z, cobblestone)
mc.setBlock(x+3, y+2, z, cobblestone)
mc.setBlock(x+4, y+2, z, oakwoodlog)

mc.setBlock(x+0, y+2, z-1, cobblestone)
mc.setBlock(x+4, y+2, z-1, cobblestone)

mc.setBlock(x+0, y+2, z-2, glass)
mc.setBlock(x+4, y+2, z-2, glass)

mc.setBlock(x+0, y+2, z-3, cobblestone)
mc.setBlock(x+4, y+2, z-3, cobblestone)

mc.setBlock(x+0, y+2, z-4, oakwoodlog)
mc.setBlock(x+1, y+2, z-4, cobblestone)
mc.setBlock(x+2, y+2, z-4, glass)
mc.setBlock(x+3, y+2, z-4, cobblestone)
mc.setBlock(x+4, y+2, z-4, oakwoodlog)



# Capa o Nivel 4
mc.setBlock(x+0, y+3, z, oakwoodlog)
mc.setBlock(x+1, y+3, z, cobblestone)
mc.setBlock(x+2, y+3, z, cobblestone)
mc.setBlock(x+3, y+3, z, cobblestone)
mc.setBlock(x+4, y+3, z, oakwoodlog)

mc.setBlock(x+0, y+3, z-1, cobblestone)
mc.setBlock(x+4, y+3, z-1, cobblestone)

mc.setBlock(x+0, y+3, z-2, cobblestone)
mc.setBlock(x+4, y+3, z-2, cobblestone)

mc.setBlock(x+0, y+3, z-3, cobblestone)
mc.setBlock(x+4, y+3, z-3, cobblestone)

mc.setBlock(x+0, y+3, z-4, oakwoodlog)
mc.setBlock(x+1, y+3, z-4, cobblestone)
mc.setBlock(x+2, y+3, z-4, cobblestone)
mc.setBlock(x+3, y+3, z-4, cobblestone)
mc.setBlock(x+4, y+3, z-4, oakwoodlog)



# Capa o Nivel 5
# Stairs para techo
mc.setBlock(x-1, y+4, z+1, oakwoodstairs,3)
mc.setBlock(x+0, y+4, z+1, oakwoodstairs,3)
mc.setBlock(x+1, y+4, z+1, oakwoodstairs,3)
mc.setBlock(x+2, y+4, z+1, oakwoodstairs,3)
mc.setBlock(x+3, y+4, z+1, oakwoodstairs,3)
mc.setBlock(x+4, y+4, z+1, oakwoodstairs,3)
mc.setBlock(x+5, y+4, z+1, oakwoodstairs,3)

mc.setBlock(x-1, y+4, z-5, oakwoodstairs,2)
mc.setBlock(x+0, y+4, z-5, oakwoodstairs,2)
mc.setBlock(x+1, y+4, z-5, oakwoodstairs,2)
mc.setBlock(x+2, y+4, z-5, oakwoodstairs,2)
mc.setBlock(x+3, y+4, z-5, oakwoodstairs,2)
mc.setBlock(x+4, y+4, z-5, oakwoodstairs,2)
mc.setBlock(x+5, y+4, z-5, oakwoodstairs,2)

mc.setBlock(x-1, y+4, z-0, oakwoodstairs,0)
mc.setBlock(x-1, y+4, z-1, oakwoodstairs,0)
mc.setBlock(x-1, y+4, z-2, oakwoodstairs,0)
mc.setBlock(x-1, y+4, z-3, oakwoodstairs,0)
mc.setBlock(x-1, y+4, z-4, oakwoodstairs,0)

mc.setBlock(x+5, y+4, z-0, oakwoodstairs,1)
mc.setBlock(x+5, y+4, z-1, oakwoodstairs,1)
mc.setBlock(x+5, y+4, z-2, oakwoodstairs,1)
mc.setBlock(x+5, y+4, z-3, oakwoodstairs,1)
mc.setBlock(x+5, y+4, z-4, oakwoodstairs,1)

# Planks
mc.setBlock(x+0, y+4, z, oakwoodplank)
mc.setBlock(x+1, y+4, z, oakwoodplank)
mc.setBlock(x+2, y+4, z, oakwoodplank)
mc.setBlock(x+3, y+4, z, oakwoodplank)
mc.setBlock(x+4, y+4, z, oakwoodplank)

mc.setBlock(x+0, y+4, z-1, oakwoodplank)
mc.setBlock(x+4, y+4, z-1, oakwoodplank)

mc.setBlock(x+0, y+4, z-2, oakwoodplank)
mc.setBlock(x+4, y+4, z-2, oakwoodplank)

mc.setBlock(x+0, y+4, z-3, oakwoodplank)
mc.setBlock(x+4, y+4, z-3, oakwoodplank)

mc.setBlock(x+0, y+4, z-4, oakwoodplank)
mc.setBlock(x+1, y+4, z-4, oakwoodplank)
mc.setBlock(x+2, y+4, z-4, oakwoodplank)
mc.setBlock(x+3, y+4, z-4, oakwoodplank)
mc.setBlock(x+4, y+4, z-4, oakwoodplank)



# Capa o Nivel 6
# Stairs
mc.setBlock(x+0, y+5, z, oakwoodstairs,3)
mc.setBlock(x+1, y+5, z, oakwoodstairs,3)
mc.setBlock(x+2, y+5, z, oakwoodstairs,3)
mc.setBlock(x+3, y+5, z, oakwoodstairs,3)
mc.setBlock(x+4, y+5, z, oakwoodstairs,3)

mc.setBlock(x+0, y+5, z-1, oakwoodstairs,0)
mc.setBlock(x+0, y+5, z-2, oakwoodstairs,0)
mc.setBlock(x+0, y+5, z-3, oakwoodstairs,0)
mc.setBlock(x+0, y+5, z-4, oakwoodstairs,0)

mc.setBlock(x+4, y+5, z-1, oakwoodstairs,1)
mc.setBlock(x+4, y+5, z-2, oakwoodstairs,1)
mc.setBlock(x+4, y+5, z-3, oakwoodstairs,1)
mc.setBlock(x+4, y+5, z-4, oakwoodstairs,1)

mc.setBlock(x+1, y+5, z-4, oakwoodstairs,2)
mc.setBlock(x+2, y+5, z-4, oakwoodstairs,2)
mc.setBlock(x+3, y+5, z-4, oakwoodstairs,2)
# Planks
mc.setBlock(x+1, y+5, z-1, oakwoodplank)
mc.setBlock(x+2, y+5, z-1, oakwoodplank)
mc.setBlock(x+3, y+5, z-1, oakwoodplank)
mc.setBlock(x+1, y+5, z-2, oakwoodplank)
mc.setBlock(x+3, y+5, z-2, oakwoodplank)
mc.setBlock(x+1, y+5, z-3, oakwoodplank)
mc.setBlock(x+2, y+5, z-3, oakwoodplank)
mc.setBlock(x+3, y+5, z-3, oakwoodplank)



# Capa o Nivel 7
# Stairs
mc.setBlock(x+1, y+6, z-1, oakwoodstairs,3)
mc.setBlock(x+2, y+6, z-1, oakwoodstairs,3)
mc.setBlock(x+3, y+6, z-1, oakwoodstairs,3)

mc.setBlock(x+1, y+6, z-3, oakwoodstairs,2)
mc.setBlock(x+2, y+6, z-3, oakwoodstairs,2)
mc.setBlock(x+3, y+6, z-3, oakwoodstairs,2)

mc.setBlock(x+1, y+6, z-2, oakwoodstairs,0)
mc.setBlock(x+3, y+6, z-2, oakwoodstairs,1)
# Plank
mc.setBlock(x+2, y+6, z-2, oakwoodplank)


time.sleep(1)
# Detalles
# Puerta, cama, antorchas
# Escaleras en frente de la puerta
mc.setBlock(x+2, y, z+1, oakwoodstairs,3)
# Puerta
mc.setBlock(x+2, y+2, z, 64,11)
mc.setBlock(x+2, y+1, z, 64,3)
# Cama
mc.setBlock(x+1, y+1, z-3, 26,10)
mc.setBlock(x+1, y+1, z-2, 26,2)
# Silla
mc.setBlock(x+3, y+1, z-3, oakwoodstairs,3)
# Antorchas
mc.setBlock(x+1, y+3, z+1, torch,3)
mc.setBlock(x+3, y+3, z+1, torch,3)
mc.setBlock(x+2, y+3, z-3, torch,3)




# Al final borramos la casita
time.sleep(10)
mc.setBlocks(x-1, y, z+1, x+5, y+6, z-5, 0)
