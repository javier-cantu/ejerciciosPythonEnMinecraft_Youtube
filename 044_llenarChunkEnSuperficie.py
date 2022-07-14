# Ejercicio 044_llenarChunkEnSuperficie.py
# Experimento con random, nested loop, math
# Dependiendo de la posicion del jugador
# Se detectara la coordenada inicial del chucnk en donde este
# Se va a cambiar el material de ese chunck
# Se construirá en la superficie no importa y del jugador
# Video: 

# Conectar
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random
# Math para usar floor
import math

# Pausa antes de empezar
time.sleep(3)

# Se detecta posicion del jugador
# Se asignan a las variables xi,yi,zi
pos_jugador = mc.player.getTilePos()
xi = pos_jugador.x
yi = pos_jugador.y
zi = pos_jugador.z


# Se divide la posicion dej jugador en x entre 16
# Se redondea para abajo para perder el decimal
# Ahora tenemos el numero del chunk
# El numero del chunk se multiplica por 16 para llegar a su X inicial
xi = (xi/16)
xi = math.floor(xi)
xi = xi*16
mc.postToChat(xi)
# Necesito guardar el valor original de xi para el nested loop
xo = xi

# Lo mismo con Z pero junte todas las operaciones
zi = math.floor((zi/16))*16
mc.postToChat(zi)

# Esto es lo diferente
# Altura
# Con la funcion getHeight podemos detectar cual es el bloque mas alto
# en esa coordenada y asi siempre se construira en la superficie y no
# donde estemos volando
yi = mc.getHeight(xi, zi)


# Material
blockType = 41

# Loop que llenara el chunk
for z in range(16):
    for x in range (16):
        # No le tenemos que restar -1 a y porque si queremos que se construya en la superficie. 
        mc.setBlock(xi,yi,zi, blockType)
        xi = xi + 1
        time.sleep(0.01)
    zi = zi + 1
    xi = xo
