# Ejercicio 024_BlockDirection
# Donde se muestra como cambiar la orientacion de la posicion del bloque

# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


blockType = 53
# 53 es Oak Wood Stairs


# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(5, 4, 5, 53) # Direccion -X o WEST

# El bloque con [data] despues de la coma
mc.setBlock(5, 4, 7, 53,0) # Direccion -X o WEST hacia donde se pone el Sol
mc.setBlock(5, 4, 9, 53,1) # Direccion +X o EAST donde sale el Sol
mc.setBlock(5, 4, 11, 53,2) # Direccion -Z o NORTE
mc.setBlock(5, 4, 13, 53,3) # Direccion +Z o SOUTH
mc.setBlock(5, 4, 15, 53,4) # Direccion -X o WEST Inverso
mc.setBlock(5, 4, 17, 53,5) # Direccion +X o EAST Inverso
mc.setBlock(5, 4, 19, 53,6) # Direccion -Z o NORTE Inverso
mc.setBlock(5, 4, 21, 53,7) # Direccion +Z o SOUTH Inverso


# Cualquier valor de [data] que no existe se convierte en 0
# y se pone el bloque hacia -X
mc.setBlock(5, 4, 24, 53,8)
mc.setBlock(5, 4, 26, 53,9)
mc.setBlock(5, 4, 28, 53,10)
mc.setBlock(5, 4, 30, 53,11)
