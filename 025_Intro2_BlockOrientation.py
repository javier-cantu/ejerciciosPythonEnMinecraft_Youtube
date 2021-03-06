# Ejercicio 025_Intro2_BlockOrientation
# Se muestran varios bloques y su orientacion

# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Estos son los IDs de los bloques que vamos a usar
blockType = 23 # Dispencer
#blockType = 29 # Sticky Piston
#blockType = 33 # Piston
#blockType = 61 # Furnace
#blockType = 63 # Standing sign
#blockType = 64 # Oak Door Block
#blockType = 65 # Ladder
#blockType = 65 # Rail
#blockType = 68 # Wall-mounted Sign Block
#blockType = 69 # Lever
#blockType = 107 # Oak Fence Gate
#blockType = 131 # Tripwire hook


# Coordenadas iniciales
x = -20
# Poner atención en la altura 63 es el nivel del agua
y = 63
z = -17


# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(x, y, z, blockType) # Direccion -X o OESTE
# El bloque con [data] despues de la coma
mc.setBlock(x, y, z+2, blockType,0) # Direccion -X o OESTE hacia donde se pone el Sol
mc.setBlock(x, y, z+4, blockType,1) # Direccion +X o ESTE donde sale el Sol
mc.setBlock(x, y, z+6, blockType,2) # Direccion -Z o NORTE
mc.setBlock(x, y, z+8, blockType,3) # Direccion +Z o SUR
mc.setBlock(x, y, z+10, blockType,4) # Direccion -X o OESTE Invetido
mc.setBlock(x, y, z+12, blockType,5) # Direccion +X o ESTE Invertido
mc.setBlock(x, y, z+14, blockType,6) # Direccion -Z o NORTE Invertido
mc.setBlock(x, y, z+16, blockType,7) # Direccion +Z o SUR Invertido
mc.setBlock(x, y, z+18, blockType,8) # Cualquier valor de [data] que no existe se convierte en 0
mc.setBlock(x, y, z+20, blockType,9) # y se pone el bloque hacia -X
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15) 
