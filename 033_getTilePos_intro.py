# Ejercicio 033_getTilePos_intro getTilePos obtiene la posicion del jugador y la manda al chat
# Video en Youtube: 


# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Con "mc.player.getTilePos()" se obtienen los 3 valores de x y z de la posición del jugador. 
# Esos 3 valores se asignan a la variable "pos"


Gets the position of the “tile” that the player is currently on.

This function returns the position as a vector. The tile position is stored as an integer as it represents the blocks exact position within the game world.

Like the .getPos() function, you can also use Python’s unpack ability to unpack this vector back to the individual x, y, and z values.

pos = mc.player.getTilePos()

# Luego asignamos cada valor a una variable diferente
x = pos.x
y = pos.y
z = pos.z


# Convertir en RANDOM el bloque abajo
mc.postToChat("Player Tile Position = " + " X = " + str(x) + "  Y = " +str(y) + "  Z = " + str(z))
