# Ejercicio 023_Intro_BlockData_2
# Donde se muestra como cambiar primero el color de wool
# ejercicio previo a mostrar cambio de orientacion
# Usamos de forma mas eficiente la variable blockType

# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# 35 es White Wool
blockType = 35

# Coordenadas iniciales
x = 10
y = 4
z = 5

# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(x, y, z, 35) # Direccion -X o WEST

# El bloque con [data] despues de la coma
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
mc.setBlock(x, y, z+30, blockType,14)
