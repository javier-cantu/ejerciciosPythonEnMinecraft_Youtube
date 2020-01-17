# Ejercicio 015_setBlocksCubos 
# Crear un cubo grande con 2 coordenadas

#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#Necesitamos importar time
import time

##########################################
# Primero  determinamos la coordenada incial
x = -20
y = 4
z = -20

#Creamos la coordenada final
x2 = 20
y2 = 8
z2 = 20

# Tipo de Bloque 1 es el ID de piedra
blockType = 1

# Construir el bloque usando 2 coordenadas.
mc.setBlocks(x, y, z, x2, y2, z2, blockType)
