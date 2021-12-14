# Ejercicio 038_nestedLoop
# Introduccion a las "nested loops" o loops anidados. 
# Nested loop = un loop dentro de otro loop. 
# Video en Youtube: 

# Conectar a MC e importar el modulo de tiempo. 
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# Necesitamos un bloque
# 251:14 es concreto rojo, lo que uso en eje x
blockType = 251,14

# Se obtiene la posicion del jugador con "getTilePos()" y se asigna a la variable "pos"
# Se manda al char la posicion
# Se hace una pause de 1 segundo
pos = mc.player.getTilePos()
mc.postToChat("Posicion inicial " + str(pos))
time.sleep(1)

# Se asignan a xi, yi, zi, los componentes de la posicion en cada eje. 
xi = pos.x
yi = pos.y
zi = pos.z

# Esto es una "lested loop"
# Hay un loop, dentro del primer loop. 
# Aqui un loop pone bloque por bloque en Z
# Y el otro loop mueve al primer loop en X
for i in range(16):
    for j in range (16):
        mc.setBlock(xi,yi-1,zi, blockType)
        zi = zi + 1
        time.sleep(0.1)
    xi = xi + 1
    zi = pos.z
