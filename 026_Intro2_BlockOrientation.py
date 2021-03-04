# Ejercicio 025_Intro2_BlockOrientation
# Se muestran varios bloques y su orientacion

# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Estos son los IDs de los bloques que vamos a usar
#blockType = 23 # Dispencer
#blockType = 29 # Sticky Piston
#blockType = 33 # Piston
#blockType = 53 # Oak Wood Stairs
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
x = 10
y = 4
z = 15


# Se determina cual block ID se usara
blockType = 53
# En x +2
x = x + 2
# Se crean los bloques con data
mc.setBlock(x, y, z+2, blockType,0) 
mc.setBlock(x, y, z+4, blockType,1) 
mc.setBlock(x, y, z+6, blockType,2)
mc.setBlock(x, y, z+8, blockType,3) 
mc.setBlock(x, y, z+10, blockType,4) 
mc.setBlock(x, y, z+12, blockType,5)
mc.setBlock(x, y, z+14, blockType,6) 
mc.setBlock(x, y, z+16, blockType,7) 
mc.setBlock(x, y, z+18, blockType,8)
mc.setBlock(x, y, z+20, blockType,9) 
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15)


# Se determina cual block ID se usara
blockType = 63
# En x +2
x = x + 2
# Se crean los bloques con data
mc.setBlock(x, y, z+2, blockType,0) 
mc.setBlock(x, y, z+4, blockType,1) 
mc.setBlock(x, y, z+6, blockType,2)
mc.setBlock(x, y, z+8, blockType,3) 
mc.setBlock(x, y, z+10, blockType,4) 
mc.setBlock(x, y, z+12, blockType,5)
mc.setBlock(x, y, z+14, blockType,6) 
mc.setBlock(x, y, z+16, blockType,7) 
mc.setBlock(x, y, z+18, blockType,8)
mc.setBlock(x, y, z+20, blockType,9) 
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15)
