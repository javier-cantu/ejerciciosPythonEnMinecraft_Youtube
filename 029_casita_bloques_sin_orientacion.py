# Ejercicio 027_casita_bloques_sin_orientacion
# Casa voltenado hacia el S en el mapa o sea hacia +z
# Usando todos los bloques pero sin orientacion correcta 
# Construiremos esta casa https://minecraft.gamepedia.com/Village/Structure/Blueprints/Plains_small_house_1_blueprint

#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#Necesitamos importar time
import time


# Materiales para usar
# A todos se les dio un nombre
# Para no tener que usar solo numeros
cobblestone = 4
oakwoodlog = 17
oakwoodplank = 5
oakwoodstairs = 53
puerta_baja = 64
puerta_alta = 64
bed1 = 26
bed2 = 26
torch = 50 
glasspane = 102
aire = 0

##########################################
# Primero  determinamos la coordenada incial
# Este sera nuestro punto de referencia
x = -10
y = 4
z = -10


time.sleep(1)
##########################################
# Construccion bloque por bloque
# Tenemos que tener y ver un plano 
# con solo la imaginacion es dificil pero posible

# Capa o Nivel 1
time.sleep(1)
mc.setBlock(x+0, y, z, oakwoodlog)
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
time.sleep(1)
mc.setBlock(x+0, y+1, z, oakwoodlog)
mc.setBlock(x+1, y+1, z, cobblestone)
mc.setBlock(x+2, y+1, z, puerta_baja) #Aqui va puerta baja
mc.setBlock(x+3, y+1, z, cobblestone)
mc.setBlock(x+4, y+1, z, oakwoodlog)

mc.setBlock(x+0, y+1, z-1, cobblestone)
mc.setBlock(x+1, y+1, z-1, aire)
mc.setBlock(x+2, y+1, z-1, aire)
mc.setBlock(x+3, y+1, z-1, aire)
mc.setBlock(x+4, y+1, z-1, cobblestone)

mc.setBlock(x+0, y+1, z-2, cobblestone)
mc.setBlock(x+1, y+1, z-2, bed1) # Aqui va un pedazo de la cama
mc.setBlock(x+2, y+1, z-2, aire)
mc.setBlock(x+3, y+1, z-2, aire)
mc.setBlock(x+4, y+1, z-2, cobblestone)

mc.setBlock(x+0, y+1, z-3, cobblestone)
mc.setBlock(x+1, y+1, z-3, bed2) # Aqui va un pedazo de la cama
mc.setBlock(x+2, y+1, z-3, aire)
mc.setBlock(x+3, y+1, z-3, oakwoodstairs) # Aqui va oak wood stairs como mesa
mc.setBlock(x+4, y+1, z-3, cobblestone)

mc.setBlock(x+0, y+1, z-4, oakwoodlog)
mc.setBlock(x+1, y+1, z-4, cobblestone)
mc.setBlock(x+2, y+1, z-4, cobblestone)
mc.setBlock(x+3, y+1, z-4, cobblestone)
mc.setBlock(x+4, y+1, z-4, oakwoodlog)



# Capa o Nivel 3
time.sleep(1)
mc.setBlock(x+1, y+2, z+1, torch) # Aqui va antorcha
mc.setBlock(x+3, y+2, z+1, torch) # Aqui va antorcha

mc.setBlock(x+0, y+2, z, oakwoodlog)
mc.setBlock(x+1, y+2, z, cobblestone)
mc.setBlock(x+2, y+2, z, puerta_alta) # Aqui va la parte alta de la puerta
mc.setBlock(x+3, y+2, z, cobblestone)
mc.setBlock(x+4, y+2, z, oakwoodlog)

mc.setBlock(x+0, y+2, z-1, cobblestone)
mc.setBlock(x+1, y+2, z-1, aire)
mc.setBlock(x+2, y+2, z-1, aire)
mc.setBlock(x+3, y+2, z-1, aire)
mc.setBlock(x+4, y+2, z-1, cobblestone)

mc.setBlock(x+0, y+2, z-2, glasspane) # Aqui va glass pane 
mc.setBlock(x+1, y+2, z-2, aire)
mc.setBlock(x+2, y+2, z-2, aire)
mc.setBlock(x+3, y+2, z-2, aire)
mc.setBlock(x+4, y+2, z-2, glasspane) # Aqui va glass pane

mc.setBlock(x+0, y+2, z-3, cobblestone)
mc.setBlock(x+1, y+2, z-3, aire)
mc.setBlock(x+2, y+2, z-3, aire)
mc.setBlock(x+3, y+2, z-3, aire)
mc.setBlock(x+4, y+2, z-3, cobblestone)

mc.setBlock(x+0, y+2, z-4, oakwoodlog)
mc.setBlock(x+1, y+2, z-4, cobblestone)
mc.setBlock(x+2, y+2, z-4, glasspane) # Aqui va glass pane
mc.setBlock(x+3, y+2, z-4, cobblestone)
mc.setBlock(x+4, y+2, z-4, oakwoodlog)



# Capa o Nivel 4
time.sleep(1)
mc.setBlock(x+0, y+3, z, oakwoodlog)
mc.setBlock(x+1, y+3, z, cobblestone)
mc.setBlock(x+2, y+3, z, cobblestone)
mc.setBlock(x+3, y+3, z, cobblestone)
mc.setBlock(x+4, y+3, z, oakwoodlog)

mc.setBlock(x+0, y+3, z-1, cobblestone)
mc.setBlock(x+1, y+3, z-1, aire)
mc.setBlock(x+2, y+3, z-1, aire)
mc.setBlock(x+3, y+3, z-1, aire)
mc.setBlock(x+4, y+3, z-1, cobblestone)

mc.setBlock(x+0, y+3, z-2, cobblestone)
mc.setBlock(x+1, y+3, z-2, aire)
mc.setBlock(x+2, y+3, z-2, aire)
mc.setBlock(x+3, y+3, z-2, aire)
mc.setBlock(x+4, y+3, z-2, cobblestone)

mc.setBlock(x+0, y+3, z-3, cobblestone)
mc.setBlock(x+1, y+3, z-3, aire)
mc.setBlock(x+2, y+3, z-3, torch) # Aqui va antorcha
mc.setBlock(x+3, y+3, z-3, aire)
mc.setBlock(x+4, y+3, z-3, cobblestone)

mc.setBlock(x+0, y+3, z-4, oakwoodlog)
mc.setBlock(x+1, y+3, z-4, cobblestone)
mc.setBlock(x+2, y+3, z-4, cobblestone)
mc.setBlock(x+3, y+3, z-4, cobblestone)
mc.setBlock(x+4, y+3, z-4, oakwoodlog)



# Capa o Nivel 5
time.sleep(1)

# Stairs para techo
mc.setBlock(x-1, y+4, z+1, oakwoodstairs)
mc.setBlock(x+0, y+4, z+1, oakwoodstairs)
mc.setBlock(x+1, y+4, z+1, oakwoodstairs)
mc.setBlock(x+2, y+4, z+1, oakwoodstairs)
mc.setBlock(x+3, y+4, z+1, oakwoodstairs)
mc.setBlock(x+4, y+4, z+1, oakwoodstairs)
mc.setBlock(x+5, y+4, z+1, oakwoodstairs)

mc.setBlock(x-1, y+4, z-5, oakwoodstairs)
mc.setBlock(x+0, y+4, z-5, oakwoodstairs)
mc.setBlock(x+1, y+4, z-5, oakwoodstairs)
mc.setBlock(x+2, y+4, z-5, oakwoodstairs)
mc.setBlock(x+3, y+4, z-5, oakwoodstairs)
mc.setBlock(x+4, y+4, z-5, oakwoodstairs)
mc.setBlock(x+5, y+4, z-5, oakwoodstairs)

mc.setBlock(x-1, y+4, z-0, oakwoodstairs)
mc.setBlock(x-1, y+4, z-1, oakwoodstairs)
mc.setBlock(x-1, y+4, z-2, oakwoodstairs)
mc.setBlock(x-1, y+4, z-3, oakwoodstairs)
mc.setBlock(x-1, y+4, z-4, oakwoodstairs)

mc.setBlock(x+5, y+4, z-0, oakwoodstairs)
mc.setBlock(x+5, y+4, z-1, oakwoodstairs)
mc.setBlock(x+5, y+4, z-2, oakwoodstairs)
mc.setBlock(x+5, y+4, z-3, oakwoodstairs)
mc.setBlock(x+5, y+4, z-4, oakwoodstairs)

# Resto
mc.setBlock(x+0, y+4, z, oakwoodplank)
mc.setBlock(x+1, y+4, z, oakwoodplank)
mc.setBlock(x+2, y+4, z, oakwoodplank)
mc.setBlock(x+3, y+4, z, oakwoodplank)
mc.setBlock(x+4, y+4, z, oakwoodplank)

mc.setBlock(x+0, y+4, z-1, oakwoodplank)
mc.setBlock(x+1, y+4, z-1, aire)
mc.setBlock(x+2, y+4, z-1, aire)
mc.setBlock(x+3, y+4, z-1, aire)
mc.setBlock(x+4, y+4, z-1, oakwoodplank)

mc.setBlock(x+0, y+4, z-2, oakwoodplank)
mc.setBlock(x+1, y+4, z-2, aire)
mc.setBlock(x+2, y+4, z-2, aire)
mc.setBlock(x+3, y+4, z-2, aire)
mc.setBlock(x+4, y+4, z-2, oakwoodplank)

mc.setBlock(x+0, y+4, z-3, oakwoodplank)
mc.setBlock(x+1, y+4, z-3, aire)
mc.setBlock(x+2, y+4, z-3, aire)
mc.setBlock(x+3, y+4, z-3, aire)
mc.setBlock(x+4, y+4, z-3, oakwoodplank)

mc.setBlock(x+0, y+4, z-4, oakwoodplank)
mc.setBlock(x+1, y+4, z-4, oakwoodplank)
mc.setBlock(x+2, y+4, z-4, oakwoodplank)
mc.setBlock(x+3, y+4, z-4, oakwoodplank)
mc.setBlock(x+4, y+4, z-4, oakwoodplank)



# Capa o Nivel 6
time.sleep(1)

mc.setBlock(x+0, y+5, z, oakwoodstairs)
mc.setBlock(x+1, y+5, z, oakwoodstairs)
mc.setBlock(x+2, y+5, z, oakwoodstairs)
mc.setBlock(x+3, y+5, z, oakwoodstairs)
mc.setBlock(x+4, y+5, z, oakwoodstairs)

mc.setBlock(x+0, y+5, z-1, oakwoodstairs)
mc.setBlock(x+1, y+5, z-1, oakwoodplank)
mc.setBlock(x+2, y+5, z-1, oakwoodplank)
mc.setBlock(x+3, y+5, z-1, oakwoodplank)
mc.setBlock(x+4, y+5, z-1, oakwoodstairs)

mc.setBlock(x+0, y+5, z-2, oakwoodstairs)
mc.setBlock(x+1, y+5, z-2, oakwoodplank)
mc.setBlock(x+2, y+5, z-2, aire)
mc.setBlock(x+3, y+5, z-2, oakwoodplank)
mc.setBlock(x+4, y+5, z-2, oakwoodstairs)

mc.setBlock(x+0, y+5, z-3, oakwoodstairs)
mc.setBlock(x+1, y+5, z-3, oakwoodplank)
mc.setBlock(x+2, y+5, z-3, oakwoodplank)
mc.setBlock(x+3, y+5, z-3, oakwoodplank)
mc.setBlock(x+4, y+5, z-3, oakwoodstairs)

mc.setBlock(x+0, y+5, z-4, oakwoodstairs)
mc.setBlock(x+1, y+5, z-4, oakwoodstairs)
mc.setBlock(x+2, y+5, z-4, oakwoodstairs)
mc.setBlock(x+3, y+5, z-4, oakwoodstairs)
mc.setBlock(x+4, y+5, z-4, oakwoodstairs)



# Capa o Nivel 7
time.sleep(1)
mc.setBlock(x+0, y+6, z, aire)
mc.setBlock(x+1, y+6, z, aire)
mc.setBlock(x+2, y+6, z, aire)
mc.setBlock(x+3, y+6, z, aire)
mc.setBlock(x+4, y+6, z, aire)

mc.setBlock(x+0, y+6, z-1, aire)
mc.setBlock(x+1, y+6, z-1, oakwoodstairs)
mc.setBlock(x+2, y+6, z-1, oakwoodstairs)
mc.setBlock(x+3, y+6, z-1, oakwoodstairs)
mc.setBlock(x+4, y+6, z-1, aire)

mc.setBlock(x+0, y+6, z-2, aire)
mc.setBlock(x+1, y+6, z-2, oakwoodstairs)
mc.setBlock(x+2, y+6, z-2, oakwoodplank)
mc.setBlock(x+3, y+6, z-2, oakwoodstairs)
mc.setBlock(x+4, y+6, z-2, aire)

mc.setBlock(x+0, y+6, z-3, aire)
mc.setBlock(x+1, y+6, z-3, oakwoodstairs)
mc.setBlock(x+2, y+6, z-3, oakwoodstairs)
mc.setBlock(x+3, y+6, z-3, oakwoodstairs)
mc.setBlock(x+4, y+6, z-3, aire)

mc.setBlock(x+0, y+6, z-4, aire)
mc.setBlock(x+1, y+6, z-4, aire)
mc.setBlock(x+2, y+6, z-4, aire)
mc.setBlock(x+3, y+6, z-4, aire)
mc.setBlock(x+4, y+6, z-4, aire)
