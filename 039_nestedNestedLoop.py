# Ejercicio 039_nestedNestedLoop
# Un loop dentro de un loop dentro de otro loop
# Video en Youtube: 

# Conectar a MC e importar el modulo de tiempo. 
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

# Necesitamos un bloque
# 251:14 es concreto rojo, lo que uso en eje x
# 251 es concreto blanco
blockType = 251

# Se obtiene la posicion del jugador con "getTilePos()"
# Y se asigna a una variable que almacenara sus 3 componentes x y z
pos_inicial = mc.player.getTilePos()

# Se separa la posicion original en cada eje
# y se asigna a estas 3 variables. 
# Estas variables se utilizaran para construir. 
xi = pos_inicial.x
yi = pos_inicial.y
zi = pos_inicial.z


# Con esto se va a construir bloque por bloque un volumen 3D. 
# Aqui camos a poner un nested loop triple
# Un loop dentro de otro loop dentro de otro loop
for i in range(16):
    for j in range (16):
        for K in range (16):
          mc.setBlock(xi,yi-1,zi, blockType)
          mc.postToChat("Z +1")
          zi = zi + 1
          time.sleep(0.05)
    mc.postToChat("X +1")
    xi = xi + 1
    zi = pos_inicial.z # Con esto se reinicia el valor de Z
 mc.postToChat("Y +1")
 yi = yi + 1
 xi = pos_inicial.x # Se reinicia el valor de X
 zi = pos_inicial.z # Con esto se reinicia el valor de Z
