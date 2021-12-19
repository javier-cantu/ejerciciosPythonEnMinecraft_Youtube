# Ejercicio 042_alturaRandomLoop.py
# Experimento con random y nested loop
# Crear un terreno con "ruido"
# en cada voxel de un area determinada por los loops 
# Se construirá una torre de bloques con alturas aleatorias
# Video: 

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random

# Necesitamos un bloque
# 2 grass block
# 251,5 Concreto Lime
# 251,6 Concreto Pink
# 251 Concreto blanco
# blockType = 2 grass
blockType = 2

# Se obtiene la posicion del jugador con "getTilePos()" y se asigna a la variable "player_pos"
player_pos = mc.player.getTilePos()
time.sleep(1)

# Se asignan a xi, yi, zi, los componentes de la posicion en cada eje. 
xi = player_pos.x
yi = player_pos.y
zi = player_pos.z

# Necesitamos otra variable que almacene la altura final de cada posicion
yf = 0

# Con una nested loop se pasa por los rangos que se dan
# Se genera una altura aleatoria con randomint()
for i in range(16):
    for j in range (16):
        yf = random.randint(1, 4)
        mc.setBlocks(xi,yi,zi, xi,yf,zi, blockType)
        xi = xi + 1
        time.sleep(0.001)
    # Se reinicia xi, se actualiza zi y zf
    xi = player_pos.x
    zi = zi + 1
