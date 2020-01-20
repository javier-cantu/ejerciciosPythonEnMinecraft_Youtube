# Ejercicio 006: intro to postToChat and Strings

#Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Enviar mensaje al chat
# El tipo de variable que se manda es un "String" y va entre comillas
# Un String es una secuencia de caracteres
mc.postToChat("Mensaje 1")
