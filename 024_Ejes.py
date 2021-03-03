# Ejercicio 24_
# Se crean los ejes para mostrar direcciones

#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#Necesitamos importar time
import time

time.sleep(5)

# Green Y
blockType = 251,5
# Eje Y
time.sleep(2)
mc.setBlocks(0, 4, 0, 0, 24, 0, blockType)

# Red X
blockType = 251,14
# Eje X
time.sleep(2)
mc.setBlocks(1, 4, 0, 25, 4, 0, blockType)

# Blue Z
blockType = 251,11
# Blue Z
time.sleep(2)
mc.setBlocks(0, 4, 1, 0, 4, 25, blockType)

time.sleep(2)
#Bloque 1, 4, 1
mc.setBlock(1, 4, 1, 251,4)
