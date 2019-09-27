# Ejercicio 010: Teletransportarse a varios lugares con tiempo

# Conectarse con Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#Necesitamos importar el modluo de time
import time

# Declarar variables, nombrarlas y darles valor para las coordenadas. 
x = -122
y = 5
z = 86

# Cambiar la posición del jugador
mc.player.setTilePos(x, y, z)
# Mandar un mensaje al chat
mc.postToChat("Posicion 1")

# Esperar 5 segundos
time.sleep(5)

# Darle nuevos valores a x, y, z para regresar al origen
x = 0
y = 5
z = 0

# Cambiar la posición del jugador
mc.player.setTilePos(x, y, z)
# Mandar un mensaje al chat
mc.postToChat("Posicion 2")
