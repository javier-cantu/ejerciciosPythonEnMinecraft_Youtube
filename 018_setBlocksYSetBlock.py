# Ejercicio 018_setBlocksYSetBlock
# Crear una torre con setBlocks
# Ponerle detalle con setBlock

#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#Necesitamos importar time
import time


# Materiales para usar
# Tipo de Bloque 1 es el ID de piedra
# Tipo de Bloque 41 es e ID del bloque de oro
blockType = 1
blockType2 = 41


# BASE
##########################################
# Primero  determinamos la coordenada incial
x = -20
y = 4
z = -20

#Creamos la coordenada final
x2 = 20
y2 = 12
z2 = 20

# Construir el bloque usando 2 coordenadas.
mc.setBlocks(x, y, z, x2, y2, z2, blockType)

# Poner bloques de detalle con setblock
time.sleep(3)
mc.setBlock(x, y2+1, z, blockType2)
mc.setBlock(x2, y2+1, z2, blockType2)
mc.setBlock(x2, y2+1, z, blockType2)
mc.setBlock(x, y2+1, z2, blockType2)



# CENTRO
##########################################
# Primero  determinamos la coordenada incial
x = -10
y = 13
z = -10

#Creamos la coordenada final
x2 = 10
y2 = 20
z2 = 10

# Tipo de Bloque 1 es el ID de piedra
blockType = 1

# Construir el bloque usando 2 coordenadas.
mc.setBlocks(x, y, z, x2, y2, z2, blockType)

# Poner bloques de detalle con setblock
time.sleep(3)
mc.setBlock(x, y2+1, z, blockType2)
mc.setBlock(x2, y2+1, z2, blockType2)
mc.setBlock(x2, y2+1, z, blockType2)
mc.setBlock(x, y2+1, z2, blockType2)



# TORRE
##########################################
# Primero  determinamos la coordenada incial
x = -5
y = 21
z = -5

#Creamos la coordenada final
x2 = 5
y2 = 55
z2 = 5

# Tipo de Bloque 1 es el ID de piedra
blockType = 1

# Construir el bloque usando 2 coordenadas.
mc.setBlocks(x, y, z, x2, y2, z2, blockType)

# Poner bloques de detalle con setblock
time.sleep(3)
mc.setBlock(x, y2+1, z, blockType2)
mc.setBlock(x2, y2+1, z2, blockType2)
mc.setBlock(x2, y2+1, z, blockType2)
mc.setBlock(x, y2+1, z2, blockType2)
