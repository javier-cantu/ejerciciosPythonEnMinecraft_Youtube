# 029_Puertas
# Como construir puertas con Python

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# Coordenadas iniciales y finales del cubo
x1 = 75
y1 = 4
z1 = 10

x2 = x1 + 10
y2 = y1 + 10
z2 = z1 + 10

mat1 = 1
mat2 = 0

# Crear cubo
time.sleep(.1)
mc.setBlocks(x1, y1, z1, x2, y2, z2, mat1)
# Hacerlo hueco con aire
time.sleep(.1)
mc.setBlocks(x1+1, y1, z1+1, x2-1, y2, z2-1, mat2)
# Espacios para las ventanas
time.sleep(.1)
mc.setBlocks(x1+2, y1+2, z1, x2-2, y2-2, z2, mat2)
# Espacios para las ventanas
time.sleep(.1)
mc.setBlocks(x1, y1+2, z1+2, x2, y2-2, z2-2, mat2)


# Camas con su data argument
time.sleep(1)
mc.setBlock(76, 4, 26, 26,0)
mc.setBlock(76, 4, 28, 26,1)
mc.setBlock(76, 4, 30, 26,2)
mc.setBlock(76, 4, 32, 26,3)
mc.setBlock(76, 4, 34, 26,4)
mc.setBlock(76, 4, 36, 26,5)
mc.setBlock(76, 4, 38, 26,6)
mc.setBlock(76, 4, 40, 26,7)
mc.setBlock(76, 4, 42, 26,8)
mc.setBlock(76, 4, 44, 26,9)
mc.setBlock(76, 4, 46, 26,10)
mc.setBlock(76, 4, 48, 26,11)
mc.setBlock(76, 4, 50, 26,12)
mc.setBlock(76, 4, 52, 26,13)
mc.setBlock(76, 4, 54, 26,14)
mc.setBlock(76, 4, 56, 26,15)


# Camas dentro
# Cama hacia +Z
time.sleep(1)
mc.setBlock(76, 4, 11, 26,10)
mc.setBlock(76, 4, 12, 26,2)

# Cama hacia -Z
time.sleep(1)
mc.setBlock(76, 4, 19, 26,8)
mc.setBlock(76, 4, 18, 26,0)

# Cama hacia +X
time.sleep(1)
mc.setBlock(84, 4, 11, 26,11)
mc.setBlock(83, 4, 11, 26,3)

# Cama hacia -X
time.sleep(1)
mc.setBlock(83, 4, 19, 26,9)
mc.setBlock(84, 4, 19, 26,1)
