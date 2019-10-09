# Ejercicio 011: Teletransportarse a 3 lugares diferentes

# Conectarse con Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#Necesitamos importar el modluo de time
import time


# Esperar 5 segundos
time.sleep(5)
# Declarar variables, nombrarlas y darles valor para las coordenadas. 
x = -74
y = 68
z = -88
# Cambiar la posición del jugador
mc.player.setTilePos(x, y, z)
# Mandar un mensaje al chat
mc.postToChat("Estamos en la posición 1")


# Esperar 7 segundos
time.sleep(7)
# Darle nuevos valores a x, y, z para regresar al origen
x = -83
y = 77
z = -175
# Cambiar la posición del jugador
mc.player.setTilePos(x, y, z)
# Mandar un mensaje al chat
mc.postToChat("Estamos en la posición 2")


# Esperar 7 segundos
time.sleep(7)
# Darle nuevos valores a x, y, z para regresar al origen
x = 0
y = 200
z = 0
# Cambiar la posición del jugador
mc.player.setTilePos(x, y, z)
# Mandar un mensaje al chat
mc.postToChat("Estamos en las alturas en el origen")
