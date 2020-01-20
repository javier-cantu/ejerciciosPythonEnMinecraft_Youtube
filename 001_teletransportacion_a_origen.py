# Ejercicio 001 Teletransportarse al origen del mundo

#Estas 2 lineas conectan a Minecraft con Python
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#Con esta funcion se cambia la posicon del jugador en x y z
# X y Z son 0
# Y es 110 para no quedar atorado en el suelo. 
mc.player.setTilePos(0, 110, 0)
