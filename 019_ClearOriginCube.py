# Ejercicio 019
# Teletransportarse al origen 
# y se limpia un cubo gigante con la función setblocks()
# Este ejercicio es para un mapa DEFAULT no FLAT


# Estas 2 lineas conectan a Minecraft con Python
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# Necesitamos importar time
import time

# Pausa inicial de 5 segundos
time.sleep(5)

# Con esta funcion se cambia la posicion del jugador en x y z
# X y Z son 0
# Y es 110 para no quedar atorado en el suelo. 
mc.player.setTilePos(0, 110, 0)


# Hacemos otra pause de 5 segundos
time.sleep(5)


##########################################
# Limpiar un cubo gigante con aire
##########################################
# Coordenada incial
# y = 20, hasta 20 de altura o profundidad.
x = -50
y = 20
z = -50

# Coordenada final
# y = 100, borrar hasta 100 de altura.
x2 = 50
y2 = 100
z2 = 50

# Tipo de Bloque 0 es el ID de aire
blockType = 0

# Construir el bloque usando 2 coordenadas.
mc.setBlocks(x, y, z, x2, y2, z2, blockType)
