#Ejercicio 012: Convertir en DIAMANTE el cubo origen 0, 0 

# Introducción a la función mc.setBlock()

# Conectarse a Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# Necesitamos importar el modulo time
import time

# Declarar las variables para los valores de x y z
# Para un mundo super flat
x = 0
y = 3
z = 0

# Esto nos acerca al origen por si estamos lejos
mc.player.setTilePos(x, 5, z)

# Esperar 3 segundos
time.sleep(3)

# Convertir en DIAMANTE el bloque del origen
# Block ID del diamante es 57
mc.setBlock(x, y, z, 57)
mc.postToChat("El Cubo en 0, 3, 0 es DIAMANTE")
