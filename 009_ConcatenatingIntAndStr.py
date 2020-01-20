# Ejercicio 009: Concatenar numeros enteros inegers con strings

# Conectarse a Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Declarar Integers y floats
numDragonBalls = 7
buscarQue = "Esferas del Dragon"

# Unir o concatenar las variables
# Se usa str() para convertir el integer en string y poderlo concatenar
mc.postToChat("Vamos a buscar las " + str(numDragonBalls) + " " + buscarQue)
