# Ejercicio 020_FillStone
# Continuacion al ejercicio 019_ClearOriginCube.py
# Rellenar o convertir en piedra el espacio que se creó
# Hasta en nivel del agua del mundo de Minecraft

#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#Necesitamos importar time
import time

# Pausa de 5 segundos
time.sleep(5)

##########################################
# Coordenada inicial la misma del ejercicio 019_ClearOriginCube.py
# y = 20, 20 de profundidad
x = -50
y = 20
z = -50

#Creamos la coordenada final
# y = 62, llenar hasta 62 el nivel del agua
x2 = 50
y2 = 62
z2 = 50

# Tipo de Bloque 1 es el ID de piedra
blockType = 1

# Construir el bloque usando 2 coordenadas y un blockID
# usamos todas las variables creadas.
mc.setBlocks(x, y, z, x2, y2, z2, blockType)
