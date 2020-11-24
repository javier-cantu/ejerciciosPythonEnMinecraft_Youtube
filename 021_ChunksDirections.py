# Ejercicio 021_ChunksDirections
# Ilustrar la direccion de cada coordenada al pintar chunks
# Se dibujan areas de 16x16 bloques en cada dirección
# (X+, Z+) / (X- Z+) / (X+ Z-) / (X- Z-)

#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#Necesitamos importar time
import time

# Variables de Bloques que vamos a usar
blockType1 = 35,5   # Lana Verde
blockType2 = 35,4   # Lana Amarilla
blockType3 = 35,1   # Lana Naranja
blockType4 = 35,14  # Lana Roja


# Pausa de 1 segundos
time.sleep(1)
##########################################
# Pintar Primer chunck x+ z+
# x inicial es 0 y z inicial 0
x = 0
y = 62
z = 0
#Creamos la coordenada final
# Cada chunck mide 16 entonces es del 0 al 15
# x fineal es 15 y z final 15
x2 = 15
y2 = 62
z2 = 15
# Construir el bloque usando 2 coordenadas.
mc.setBlocks(x, y, z, x2, y2, z2, blockType1)


# Pausa de 1 segundos
time.sleep(1)
##########################################
# Pintar Segundo chunck x- z+
# x inicial es -1 y z inicial 0
x = -1
y = 62
z = 0
#Creamos la coordenada final
# Cada chunck mide 16 entonces es del -1
# Como es X negativa se va hasta el -16
x2 = -16
y2 = 62
z2 = 15
# Construir el bloque usando 2 coordenadas.
mc.setBlocks(x, y, z, x2, y2, z2, blockType2)


# Pausa de 1 segundos
time.sleep(1)
##########################################
# Pintar Tercer chunck x+ z-
# x inicial es 0
# z inicial es -1
x = 0
y = 62
z = -1
#Creamos la coordenada final
# Cada chunck mide 16 entonces
# Como es X positiva es hasta 15
# Como es Z negativa es hasta -16
x2 = 15
y2 = 62
z2 = -16
# Construir el bloque usando 2 coordenadas.
mc.setBlocks(x, y, z, x2, y2, z2, blockType3)


# Pausa de 1 segundos
time.sleep(1)
##########################################
# Pintar Tercer chunck x- z-
# x inicial es -1
# z inicial es -1
x = -1
y = 62
z = -1
#Creamos la coordenada final
# Cada chunck mide 16 entonces
# Como es X negativa es hasta -16
# Como es Z negativa es hasta -16
x2 = -16
y2 = 62
z2 = -16
# Construir el bloque usando 2 coordenadas.
mc.setBlocks(x, y, z, x2, y2, z2, blockType4)
