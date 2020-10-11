# Ejercicio 022_BlockDirection_M
# Donde se muestra como cambiar la orientacion de la posicion del bloque
# Pero se puede vambiar facilmente el tipo de bloque usando la variable "blockType"

# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()



blockType = 203
# Varios bloques interesantes con varios valores de [data]
# 53 = Oak Wood Stairs
# 203 = Purpur Block
# 63 Standing Sign Block este si tiene mas valores de [data]
# 59 Wheat Crops
# 92 Cake
# 104 Pumpkin Stem
# 69 Lever esta tambien tiene mas valores de [data]



# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(5, 4, 5, blockType) # Direccion -X o WEST

# El bloque con [data] despues de la coma
mc.setBlock(5, 4, 7, blockType,0) # Direccion -X o WEST hacia donde se pone el Sol
mc.setBlock(5, 4, 9, blockType,1) # Direccion +X o EAST donde sale el Sol
mc.setBlock(5, 4, 11, blockType,2) # Direccion -Z o NORTE
mc.setBlock(5, 4, 13, blockType,3) # Direccion +Z o SOUTH
mc.setBlock(5, 4, 15, blockType,4) # Direccion -X o WEST Inverso
mc.setBlock(5, 4, 17, blockType,5) # Direccion +X o EAST Inverso
mc.setBlock(5, 4, 19, blockType,6) # Direccion -Z o NORTE Inverso
mc.setBlock(5, 4, 21, blockType,7) # Direccion +Z o SOUTH Inverso



# Cualquier valor de [data] que no existe se convierte en 0
# y se pone el bloque hacia -X
mc.setBlock(5, 4, 24, blockType,8)
mc.setBlock(5, 4, 26, blockType,9)
mc.setBlock(5, 4, 28, blockType,10)
mc.setBlock(5, 4, 30, blockType,11)
