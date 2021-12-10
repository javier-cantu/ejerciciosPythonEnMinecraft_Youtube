# Ejercicio 037_casitaLoop
# Ejemplo de como se puede usar un loop
# Video en Youtube: 

# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# importar modulo time
import time


# Variables para los materiales
cobblestone = 4
oakwoodlog = 17
oakwoodplank = 5
glass = 20
aire = 0
oakwoodstairs = 53
glasspane = 102
torch = 50

# Pausa
time.sleep(2)


# "for loop" que se ejecutara 20 veces
# Cada vez que se de una loop se construira una casita
# Y se actualiza la posicion del jugador
for i in range(20):
  ##########################################
  # Primero  obtiene la posicion del jugador
  # Y se almacena en las variables x y z
  x, y, z = mc.player.getTilePos()
  ##########################################
  # Construccion bloque por bloque
  # Capa o Nivel 1
  mc.setBlock(x+0, y, z, 41)
  mc.setBlock(x+1, y, z, cobblestone)
  mc.setBlock(x+2, y, z, cobblestone)
  mc.setBlock(x+3, y, z, cobblestone)
  mc.setBlock(x+4, y, z, oakwoodlog)
  mc.setBlock(x+0, y, z-1, cobblestone)
  mc.setBlock(x+1, y, z-1, oakwoodplank)
  mc.setBlock(x+2, y, z-1, oakwoodplank)
  mc.setBlock(x+3, y, z-1, oakwoodplank)
  mc.setBlock(x+4, y, z-1, cobblestone)
  mc.setBlock(x+0, y, z-2, cobblestone)
  mc.setBlock(x+1, y, z-2, oakwoodplank)
  mc.setBlock(x+2, y, z-2, oakwoodplank)
  mc.setBlock(x+3, y, z-2, oakwoodplank)
  mc.setBlock(x+4, y, z-2, cobblestone)
  mc.setBlock(x+0, y, z-3, cobblestone)
  mc.setBlock(x+1, y, z-3, oakwoodplank)
  mc.setBlock(x+2, y, z-3, oakwoodplank)
  mc.setBlock(x+3, y, z-3, oakwoodplank)
  mc.setBlock(x+4, y, z-3, cobblestone)
  mc.setBlock(x+0, y, z-4, oakwoodlog)
  mc.setBlock(x+1, y, z-4, cobblestone)
  mc.setBlock(x+2, y, z-4, cobblestone)
  mc.setBlock(x+3, y, z-4, cobblestone)
  mc.setBlock(x+4, y, z-4, oakwoodlog)
  # Capa o Nivel 2
  mc.setBlock(x+0, y+1, z, oakwoodlog)
  mc.setBlock(x+1, y+1, z, cobblestone)
  mc.setBlock(x+3, y+1, z, cobblestone)
  mc.setBlock(x+4, y+1, z, oakwoodlog)
  mc.setBlock(x+0, y+1, z-1, cobblestone)
  mc.setBlock(x+4, y+1, z-1, cobblestone)
  mc.setBlock(x+0, y+1, z-2, cobblestone)
  mc.setBlock(x+4, y+1, z-2, cobblestone)
  mc.setBlock(x+0, y+1, z-3, cobblestone)
  mc.setBlock(x+4, y+1, z-3, cobblestone)
  mc.setBlock(x+0, y+1, z-4, oakwoodlog)
  mc.setBlock(x+1, y+1, z-4, cobblestone)
  mc.setBlock(x+2, y+1, z-4, cobblestone)
  mc.setBlock(x+3, y+1, z-4, cobblestone)
  mc.setBlock(x+4, y+1, z-4, oakwoodlog)
  # Capa o Nivel 3
  mc.setBlock(x+0, y+2, z, oakwoodlog)
  mc.setBlock(x+1, y+2, z, cobblestone)
  mc.setBlock(x+3, y+2, z, cobblestone)
  mc.setBlock(x+4, y+2, z, oakwoodlog)
  mc.setBlock(x+0, y+2, z-1, cobblestone)
  mc.setBlock(x+4, y+2, z-1, cobblestone)
  mc.setBlock(x+0, y+2, z-2, glass)
  mc.setBlock(x+4, y+2, z-2, glass)
  mc.setBlock(x+0, y+2, z-3, cobblestone)
  mc.setBlock(x+4, y+2, z-3, cobblestone)
  mc.setBlock(x+0, y+2, z-4, oakwoodlog)
  mc.setBlock(x+1, y+2, z-4, cobblestone)
  mc.setBlock(x+2, y+2, z-4, glass)
  mc.setBlock(x+3, y+2, z-4, cobblestone)
  mc.setBlock(x+4, y+2, z-4, oakwoodlog)
  # Capa o Nivel 4
  mc.setBlock(x+0, y+3, z, oakwoodlog)
  mc.setBlock(x+1, y+3, z, cobblestone)
  mc.setBlock(x+2, y+3, z, cobblestone)
  mc.setBlock(x+3, y+3, z, cobblestone)
  mc.setBlock(x+4, y+3, z, oakwoodlog)
  mc.setBlock(x+0, y+3, z-1, cobblestone)
  mc.setBlock(x+4, y+3, z-1, cobblestone)
  mc.setBlock(x+0, y+3, z-2, cobblestone)
  mc.setBlock(x+4, y+3, z-2, cobblestone)
  mc.setBlock(x+0, y+3, z-3, cobblestone)
  mc.setBlock(x+4, y+3, z-3, cobblestone)
  mc.setBlock(x+0, y+3, z-4, oakwoodlog)
  mc.setBlock(x+1, y+3, z-4, cobblestone)
  mc.setBlock(x+2, y+3, z-4, cobblestone)
  mc.setBlock(x+3, y+3, z-4, cobblestone)
  mc.setBlock(x+4, y+3, z-4, oakwoodlog)
  # Capa o Nivel 5
  # Stairs para techo
  mc.setBlock(x-1, y+4, z+1, oakwoodstairs,3)
  mc.setBlock(x+0, y+4, z+1, oakwoodstairs,3)
  mc.setBlock(x+1, y+4, z+1, oakwoodstairs,3)
  mc.setBlock(x+2, y+4, z+1, oakwoodstairs,3)
  mc.setBlock(x+3, y+4, z+1, oakwoodstairs,3)
  mc.setBlock(x+4, y+4, z+1, oakwoodstairs,3)
  mc.setBlock(x+5, y+4, z+1, oakwoodstairs,3)
  mc.setBlock(x-1, y+4, z-5, oakwoodstairs,2)
  mc.setBlock(x+0, y+4, z-5, oakwoodstairs,2)
  mc.setBlock(x+1, y+4, z-5, oakwoodstairs,2)
  mc.setBlock(x+2, y+4, z-5, oakwoodstairs,2)
  mc.setBlock(x+3, y+4, z-5, oakwoodstairs,2)
  mc.setBlock(x+4, y+4, z-5, oakwoodstairs,2)
  mc.setBlock(x+5, y+4, z-5, oakwoodstairs,2)
  mc.setBlock(x-1, y+4, z-0, oakwoodstairs,0)
  mc.setBlock(x-1, y+4, z-1, oakwoodstairs,0)
  mc.setBlock(x-1, y+4, z-2, oakwoodstairs,0)
  mc.setBlock(x-1, y+4, z-3, oakwoodstairs,0)
  mc.setBlock(x-1, y+4, z-4, oakwoodstairs,0)
  mc.setBlock(x+5, y+4, z-0, oakwoodstairs,1)
  mc.setBlock(x+5, y+4, z-1, oakwoodstairs,1)
  mc.setBlock(x+5, y+4, z-2, oakwoodstairs,1)
  mc.setBlock(x+5, y+4, z-3, oakwoodstairs,1)
  mc.setBlock(x+5, y+4, z-4, oakwoodstairs,1)
  # Planks
  mc.setBlock(x+0, y+4, z, oakwoodplank)
  mc.setBlock(x+1, y+4, z, oakwoodplank)
  mc.setBlock(x+2, y+4, z, oakwoodplank)
  mc.setBlock(x+3, y+4, z, oakwoodplank)
  mc.setBlock(x+4, y+4, z, oakwoodplank)
  mc.setBlock(x+0, y+4, z-1, oakwoodplank)
  mc.setBlock(x+4, y+4, z-1, oakwoodplank)
  mc.setBlock(x+0, y+4, z-2, oakwoodplank)
  mc.setBlock(x+4, y+4, z-2, oakwoodplank)
  mc.setBlock(x+0, y+4, z-3, oakwoodplank)
  mc.setBlock(x+4, y+4, z-3, oakwoodplank)
  mc.setBlock(x+0, y+4, z-4, oakwoodplank)
  mc.setBlock(x+1, y+4, z-4, oakwoodplank)
  mc.setBlock(x+2, y+4, z-4, oakwoodplank)
  mc.setBlock(x+3, y+4, z-4, oakwoodplank)
  mc.setBlock(x+4, y+4, z-4, oakwoodplank)
  # Capa o Nivel 6
  # Stairs
  mc.setBlock(x+0, y+5, z, oakwoodstairs,3)
  mc.setBlock(x+1, y+5, z, oakwoodstairs,3)
  mc.setBlock(x+2, y+5, z, oakwoodstairs,3)
  mc.setBlock(x+3, y+5, z, oakwoodstairs,3)
  mc.setBlock(x+4, y+5, z, oakwoodstairs,3)
  mc.setBlock(x+0, y+5, z-1, oakwoodstairs,0)
  mc.setBlock(x+0, y+5, z-2, oakwoodstairs,0)
  mc.setBlock(x+0, y+5, z-3, oakwoodstairs,0)
  mc.setBlock(x+0, y+5, z-4, oakwoodstairs,0)
  mc.setBlock(x+4, y+5, z-1, oakwoodstairs,1)
  mc.setBlock(x+4, y+5, z-2, oakwoodstairs,1)
  mc.setBlock(x+4, y+5, z-3, oakwoodstairs,1)
  mc.setBlock(x+4, y+5, z-4, oakwoodstairs,1)
  mc.setBlock(x+1, y+5, z-4, oakwoodstairs,2)
  mc.setBlock(x+2, y+5, z-4, oakwoodstairs,2)
  mc.setBlock(x+3, y+5, z-4, oakwoodstairs,2)
  # Planks
  mc.setBlock(x+1, y+5, z-1, oakwoodplank)
  mc.setBlock(x+2, y+5, z-1, oakwoodplank)
  mc.setBlock(x+3, y+5, z-1, oakwoodplank)
  mc.setBlock(x+1, y+5, z-2, oakwoodplank)
  mc.setBlock(x+3, y+5, z-2, oakwoodplank)
  mc.setBlock(x+1, y+5, z-3, oakwoodplank)
  mc.setBlock(x+2, y+5, z-3, oakwoodplank)
  mc.setBlock(x+3, y+5, z-3, oakwoodplank)
  # Capa o Nivel 7
  # Stairs
  mc.setBlock(x+1, y+6, z-1, oakwoodstairs,3)
  mc.setBlock(x+2, y+6, z-1, oakwoodstairs,3)
  mc.setBlock(x+3, y+6, z-1, oakwoodstairs,3)
  mc.setBlock(x+1, y+6, z-3, oakwoodstairs,2)
  mc.setBlock(x+2, y+6, z-3, oakwoodstairs,2)
  mc.setBlock(x+3, y+6, z-3, oakwoodstairs,2)
  mc.setBlock(x+1, y+6, z-2, oakwoodstairs,0)
  mc.setBlock(x+3, y+6, z-2, oakwoodstairs,1)
  # Plank
  mc.setBlock(x+2, y+6, z-2, oakwoodplank)
  # Detalles
  # Puerta, cama, antorchas
  # Escaleras en frente de la puerta
  mc.setBlock(x+2, y, z+1, oakwoodstairs,3)
  # Puerta
  mc.setBlock(x+2, y+2, z, 64,11)
  mc.setBlock(x+2, y+1, z, 64,3)
  # Cama
  mc.setBlock(x+1, y+1, z-3, 26,10)
  mc.setBlock(x+1, y+1, z-2, 26,2)
  # Silla
  mc.setBlock(x+3, y+1, z-3, oakwoodstairs,3)
  # Antorchas
  mc.setBlock(x+1, y+3, z+1, torch,3)
  mc.setBlock(x+3, y+3, z+1, torch,3)
  mc.setBlock(x+2, y+3, z-3, torch,3)
  
  # Pausa de 3 segundos para poder movernos
  time.sleep(3)
