# 028 Como crear puertas con mcpi python

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time


# Coordenadas iniciales y finales del cubo
x1 = 50
y1 = 4
z1 = 10

x2 = 60
y2 = 8
z2 = 20


# Crear cubo
time.sleep(.1)
mc.setBlocks(x1, y1, z1, x2, y2, z2, 1)
# Hacerlo hueco con aire
time.sleep(.1)
mc.setBlocks(x1+1, y1, z1+1, x2-1, y2, z2-1, 0)



# Se hacen los espacios para las puertas
time.sleep(.1)
# Se hace espacio para la puerta en pared hacia +X
mc.setBlocks(x2, y1, z1+5, x2, y1+1, z1+5, 0)

time.sleep(.1)
# Se hace espacio para la puerta en pared hacia +Z
mc.setBlocks(x1+5, y1, z2, x1+5, y1+1, z2, 0)

time.sleep(.1)
# Se hace espacio para la puerta en pared hacia -X
mc.setBlocks(x1, y1, z1+5, x1, y1+1, z1+5, 0)

time.sleep(.1)
# Se hace espacio para la puerta en pared hacia -Z
mc.setBlocks(x1+5, y1, z1, x1+5, y1+1, z1, 0)



# Construir las puertas wooden_door = 64
#### Primero se tiene que construir la parte de arriba
# Puerta hacia -X
time.sleep(.5)
mc.setBlock(x1, y1+1, z1+5, 64,8)
time.sleep(.5)
mc.setBlock(x1, y1, z1+5, 64,0)

# Puerta hacia -Z
time.sleep(.5)
mc.setBlock(x1+5, y1+1, z1, 64,9)
time.sleep(.5)
mc.setBlock(x1+5, y1, z1, 64,1)

# Puerta hacia +X
time.sleep(.5)
mc.setBlock(x2, y1+1, z1+5, 64,10)
time.sleep(.5)
mc.setBlock(x2, y1, z1+5, 64,2)

# Puerta hacia +Z
time.sleep(.5)
mc.setBlock(x1+5, y1+1, z2, 64,11)
time.sleep(.5)
mc.setBlock(x1+5, y1, z2, 64,3)
