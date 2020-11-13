# Ejercicio 025_Intro3_BlockOrientation_repeticiones
# Se muestran varios bloques y su orientacion
# Usamos de forma mas eficiente la variable blockType
# Repetimos lo mismo varias veces pero con diferentes bloques

# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Estos son los IDs de los bloques que vamos a usar
# Cada uno con su nombre de variable unico
blockType1 = 67 # Cobblestone Stairs
blockType2 = 29 # Sticky Piston
blockType3 = 33 # Piston
blockType4 = 61 # Furnace
blockType5 = 63 # Standing sign
blockType6 = 64 # Oak Door Block
blockType7 = 65 # Ladder
blockType8 = 66 # Rail
blockType9 = 68 # Wall-mounted Sign Block
blockType10 = 69 # Lever
blockType11 = 107 # Oak Fence Gate
blockType12 = 131 # Tripwire hook


# Coordenadas iniciales
x = -20
# Poner atención en la altura 63 es el nivel del agua
y = 63
z = -17

#####################################
# Se comienza con el primer bloque
# Uso eficiente de la variable blockType
blockType = blockType1

# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(x, y, z, blockType) # Direccion -X o OESTE
# El bloque con [data] despues de la coma
mc.setBlock(x, y, z+2, blockType,0) # Direccion -X o OESTE hacia donde se pone el Sol
mc.setBlock(x, y, z+4, blockType,1) # Direccion +X o ESTE donde sale el Sol
mc.setBlock(x, y, z+6, blockType,2) # Direccion -Z o NORTE
mc.setBlock(x, y, z+8, blockType,3) # Direccion +Z o SUR
mc.setBlock(x, y, z+10, blockType,4) # Direccion -X o OESTE Invetido
mc.setBlock(x, y, z+12, blockType,5) # Direccion +X o ESTE Invertido
mc.setBlock(x, y, z+14, blockType,6) # Direccion -Z o NORTE Invertido
mc.setBlock(x, y, z+16, blockType,7) # Direccion +Z o SUR Invertido
mc.setBlock(x, y, z+18, blockType,8) # Cualquier valor de [data] que no existe se convierte en 0
mc.setBlock(x, y, z+20, blockType,9) # y se pone el bloque hacia -X
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15)

# Se mueve hacia X negativa para repetir lo mismo perocon otro bloque
x = x-2



#####################################
# Se repite
# Uso eficiente de la variable blockType
# al cambiarle el valor por otra variable ahora blockType es igual a blockType2
blockType = blockType2

# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(x, y, z, blockType) # Direccion -X o OESTE
# El bloque con [data] despues de la coma
mc.setBlock(x, y, z+2, blockType,0) # Direccion -X o OESTE hacia donde se pone el Sol
mc.setBlock(x, y, z+4, blockType,1) # Direccion +X o ESTE donde sale el Sol
mc.setBlock(x, y, z+6, blockType,2) # Direccion -Z o NORTE
mc.setBlock(x, y, z+8, blockType,3) # Direccion +Z o SUR
mc.setBlock(x, y, z+10, blockType,4) # Direccion -X o OESTE Invetido
mc.setBlock(x, y, z+12, blockType,5) # Direccion +X o ESTE Invertido
mc.setBlock(x, y, z+14, blockType,6) # Direccion -Z o NORTE Invertido
mc.setBlock(x, y, z+16, blockType,7) # Direccion +Z o SUR Invertido
mc.setBlock(x, y, z+18, blockType,8) # Cualquier valor de [data] que no existe se convierte en 0
mc.setBlock(x, y, z+20, blockType,9) # y se pone el bloque hacia -X
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15)

# Se mueve hacia X negativa para repetir lo mismo perocon otro bloque
x = x-2



#####################################
# Se repite
# Uso eficiente de la variable blockType
# al cambiarle el valor por otra variable ahora blockType es igual a blockType3
blockType = blockType3

# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(x, y, z, blockType) # Direccion -X o OESTE
# El bloque con [data] despues de la coma
mc.setBlock(x, y, z+2, blockType,0) # Direccion -X o OESTE hacia donde se pone el Sol
mc.setBlock(x, y, z+4, blockType,1) # Direccion +X o ESTE donde sale el Sol
mc.setBlock(x, y, z+6, blockType,2) # Direccion -Z o NORTE
mc.setBlock(x, y, z+8, blockType,3) # Direccion +Z o SUR
mc.setBlock(x, y, z+10, blockType,4) # Direccion -X o OESTE Invetido
mc.setBlock(x, y, z+12, blockType,5) # Direccion +X o ESTE Invertido
mc.setBlock(x, y, z+14, blockType,6) # Direccion -Z o NORTE Invertido
mc.setBlock(x, y, z+16, blockType,7) # Direccion +Z o SUR Invertido
mc.setBlock(x, y, z+18, blockType,8) # Cualquier valor de [data] que no existe se convierte en 0
mc.setBlock(x, y, z+20, blockType,9) # y se pone el bloque hacia -X
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15)

# Se mueve hacia X negativa para repetir lo mismo perocon otro bloque
x = x-2



#####################################
# Se repite
# Uso eficiente de la variable blockType
# al cambiarle el valor por otra variable ahora blockType es igual a blockType4
blockType = blockType4

# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(x, y, z, blockType) # Direccion -X o OESTE
# El bloque con [data] despues de la coma
mc.setBlock(x, y, z+2, blockType,0) # Direccion -X o OESTE hacia donde se pone el Sol
mc.setBlock(x, y, z+4, blockType,1) # Direccion +X o ESTE donde sale el Sol
mc.setBlock(x, y, z+6, blockType,2) # Direccion -Z o NORTE
mc.setBlock(x, y, z+8, blockType,3) # Direccion +Z o SUR
mc.setBlock(x, y, z+10, blockType,4) # Direccion -X o OESTE Invetido
mc.setBlock(x, y, z+12, blockType,5) # Direccion +X o ESTE Invertido
mc.setBlock(x, y, z+14, blockType,6) # Direccion -Z o NORTE Invertido
mc.setBlock(x, y, z+16, blockType,7) # Direccion +Z o SUR Invertido
mc.setBlock(x, y, z+18, blockType,8) # Cualquier valor de [data] que no existe se convierte en 0
mc.setBlock(x, y, z+20, blockType,9) # y se pone el bloque hacia -X
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15)

# Se mueve hacia X negativa para repetir lo mismo perocon otro bloque
x = x-2



#####################################
# Se repite
# Uso eficiente de la variable blockType
# al cambiarle el valor por otra variable ahora blockType es igual a blockType5
blockType = blockType5

# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(x, y, z, blockType) # Direccion -X o OESTE
# El bloque con [data] despues de la coma
mc.setBlock(x, y, z+2, blockType,0) # Direccion -X o OESTE hacia donde se pone el Sol
mc.setBlock(x, y, z+4, blockType,1) # Direccion +X o ESTE donde sale el Sol
mc.setBlock(x, y, z+6, blockType,2) # Direccion -Z o NORTE
mc.setBlock(x, y, z+8, blockType,3) # Direccion +Z o SUR
mc.setBlock(x, y, z+10, blockType,4) # Direccion -X o OESTE Invetido
mc.setBlock(x, y, z+12, blockType,5) # Direccion +X o ESTE Invertido
mc.setBlock(x, y, z+14, blockType,6) # Direccion -Z o NORTE Invertido
mc.setBlock(x, y, z+16, blockType,7) # Direccion +Z o SUR Invertido
mc.setBlock(x, y, z+18, blockType,8) # Cualquier valor de [data] que no existe se convierte en 0
mc.setBlock(x, y, z+20, blockType,9) # y se pone el bloque hacia -X
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15)

# Se mueve hacia X negativa para repetir lo mismo perocon otro bloque
x = x-2



#####################################
# Se repite
# Uso eficiente de la variable blockType
# al cambiarle el valor por otra variable ahora blockType es igual a blockType6
blockType = blockType6

# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(x, y, z, blockType) # Direccion -X o OESTE
# El bloque con [data] despues de la coma
mc.setBlock(x, y, z+2, blockType,0) # Direccion -X o OESTE hacia donde se pone el Sol
mc.setBlock(x, y, z+4, blockType,1) # Direccion +X o ESTE donde sale el Sol
mc.setBlock(x, y, z+6, blockType,2) # Direccion -Z o NORTE
mc.setBlock(x, y, z+8, blockType,3) # Direccion +Z o SUR
mc.setBlock(x, y, z+10, blockType,4) # Direccion -X o OESTE Invetido
mc.setBlock(x, y, z+12, blockType,5) # Direccion +X o ESTE Invertido
mc.setBlock(x, y, z+14, blockType,6) # Direccion -Z o NORTE Invertido
mc.setBlock(x, y, z+16, blockType,7) # Direccion +Z o SUR Invertido
mc.setBlock(x, y, z+18, blockType,8) # Cualquier valor de [data] que no existe se convierte en 0
mc.setBlock(x, y, z+20, blockType,9) # y se pone el bloque hacia -X
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15) # El standing sign es el unico que llega hasta el 15

# Se mueve hacia X negativa para repetir lo mismo perocon otro bloque
x = x-2



#####################################
# Se repite
# Uso eficiente de la variable blockType
# al cambiarle el valor por otra variable ahora blockType es igual a blockType7
blockType = blockType7

# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(x, y, z, blockType) # Direccion -X o OESTE
# El bloque con [data] despues de la coma
mc.setBlock(x, y, z+2, blockType,0) # Direccion -X o OESTE hacia donde se pone el Sol
mc.setBlock(x, y, z+4, blockType,1) # Direccion +X o ESTE donde sale el Sol
mc.setBlock(x, y, z+6, blockType,2) # Direccion -Z o NORTE
mc.setBlock(x, y, z+8, blockType,3) # Direccion +Z o SUR
mc.setBlock(x, y, z+10, blockType,4) # Direccion -X o OESTE Invetido
mc.setBlock(x, y, z+12, blockType,5) # Direccion +X o ESTE Invertido
mc.setBlock(x, y, z+14, blockType,6) # Direccion -Z o NORTE Invertido
mc.setBlock(x, y, z+16, blockType,7) # Direccion +Z o SUR Invertido
mc.setBlock(x, y, z+18, blockType,8) # Cualquier valor de [data] que no existe se convierte en 0
mc.setBlock(x, y, z+20, blockType,9) # y se pone el bloque hacia -X
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15)

# Se mueve hacia X negativa para repetir lo mismo perocon otro bloque
x = x-2



#####################################
# Se repite
# Uso eficiente de la variable blockType
# al cambiarle el valor por otra variable ahora blockType es igual a blockType8
blockType = blockType8

# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(x, y, z, blockType) # Direccion -X o OESTE
# El bloque con [data] despues de la coma
mc.setBlock(x, y, z+2, blockType,0) # Direccion -X o OESTE hacia donde se pone el Sol
mc.setBlock(x, y, z+4, blockType,1) # Direccion +X o ESTE donde sale el Sol
mc.setBlock(x, y, z+6, blockType,2) # Direccion -Z o NORTE
mc.setBlock(x, y, z+8, blockType,3) # Direccion +Z o SUR
mc.setBlock(x, y, z+10, blockType,4) # Direccion -X o OESTE Invetido
mc.setBlock(x, y, z+12, blockType,5) # Direccion +X o ESTE Invertido
mc.setBlock(x, y, z+14, blockType,6) # Direccion -Z o NORTE Invertido
mc.setBlock(x, y, z+16, blockType,7) # Direccion +Z o SUR Invertido
mc.setBlock(x, y, z+18, blockType,8) # Cualquier valor de [data] que no existe se convierte en 0
mc.setBlock(x, y, z+20, blockType,9) # y se pone el bloque hacia -X
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15)

# Se mueve hacia X negativa para repetir lo mismo perocon otro bloque
x = x-2



#####################################
# Se repite
# Uso eficiente de la variable blockType
# al cambiarle el valor por otra variable ahora blockType es igual a blockType9
blockType = blockType9

# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(x, y, z, blockType) # Direccion -X o OESTE
# El bloque con [data] despues de la coma
mc.setBlock(x, y, z+2, blockType,0) # Direccion -X o OESTE hacia donde se pone el Sol
mc.setBlock(x, y, z+4, blockType,1) # Direccion +X o ESTE donde sale el Sol
mc.setBlock(x, y, z+6, blockType,2) # Direccion -Z o NORTE
mc.setBlock(x, y, z+8, blockType,3) # Direccion +Z o SUR
mc.setBlock(x, y, z+10, blockType,4) # Direccion -X o OESTE Invetido
mc.setBlock(x, y, z+12, blockType,5) # Direccion +X o ESTE Invertido
mc.setBlock(x, y, z+14, blockType,6) # Direccion -Z o NORTE Invertido
mc.setBlock(x, y, z+16, blockType,7) # Direccion +Z o SUR Invertido
mc.setBlock(x, y, z+18, blockType,8) # Cualquier valor de [data] que no existe se convierte en 0
mc.setBlock(x, y, z+20, blockType,9) # y se pone el bloque hacia -X
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15)

# Se mueve hacia X negativa para repetir lo mismo perocon otro bloque
x = x-2



#####################################
# Se repite
# Uso eficiente de la variable blockType
# al cambiarle el valor por otra variable ahora blockType es igual a blockType10
blockType = blockType10

# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(x, y, z, blockType) # Direccion -X o OESTE
# El bloque con [data] despues de la coma
mc.setBlock(x, y, z+2, blockType,0) # Direccion -X o OESTE hacia donde se pone el Sol
mc.setBlock(x, y, z+4, blockType,1) # Direccion +X o ESTE donde sale el Sol
mc.setBlock(x, y, z+6, blockType,2) # Direccion -Z o NORTE
mc.setBlock(x, y, z+8, blockType,3) # Direccion +Z o SUR
mc.setBlock(x, y, z+10, blockType,4) # Direccion -X o OESTE Invetido
mc.setBlock(x, y, z+12, blockType,5) # Direccion +X o ESTE Invertido
mc.setBlock(x, y, z+14, blockType,6) # Direccion -Z o NORTE Invertido
mc.setBlock(x, y, z+16, blockType,7) # Direccion +Z o SUR Invertido
mc.setBlock(x, y, z+18, blockType,8) # Cualquier valor de [data] que no existe se convierte en 0
mc.setBlock(x, y, z+20, blockType,9) # y se pone el bloque hacia -X
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15)

# Se mueve hacia X negativa para repetir lo mismo perocon otro bloque
x = x-2



#####################################
# Se repite
# Uso eficiente de la variable blockType
# al cambiarle el valor por otra variable ahora blockType es igual a blockType11
blockType = blockType11

# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(x, y, z, blockType) # Direccion -X o OESTE
# El bloque con [data] despues de la coma
mc.setBlock(x, y, z+2, blockType,0) # Direccion -X o OESTE hacia donde se pone el Sol
mc.setBlock(x, y, z+4, blockType,1) # Direccion +X o ESTE donde sale el Sol
mc.setBlock(x, y, z+6, blockType,2) # Direccion -Z o NORTE
mc.setBlock(x, y, z+8, blockType,3) # Direccion +Z o SUR
mc.setBlock(x, y, z+10, blockType,4) # Direccion -X o OESTE Invetido
mc.setBlock(x, y, z+12, blockType,5) # Direccion +X o ESTE Invertido
mc.setBlock(x, y, z+14, blockType,6) # Direccion -Z o NORTE Invertido
mc.setBlock(x, y, z+16, blockType,7) # Direccion +Z o SUR Invertido
mc.setBlock(x, y, z+18, blockType,8) # Cualquier valor de [data] que no existe se convierte en 0
mc.setBlock(x, y, z+20, blockType,9) # y se pone el bloque hacia -X
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15)

# Se mueve hacia X negativa para repetir lo mismo perocon otro bloque
x = x-2



#####################################
# Se repite
# Uso eficiente de la variable blockType
# al cambiarle el valor por otra variable ahora blockType es igual a blockType12
blockType = blockType12

# El bloque solo con su ID sin [data] despues de la coma
mc.setBlock(x, y, z, blockType) # Direccion -X o OESTE
# El bloque con [data] despues de la coma
mc.setBlock(x, y, z+2, blockType,0) # Direccion -X o OESTE hacia donde se pone el Sol
mc.setBlock(x, y, z+4, blockType,1) # Direccion +X o ESTE donde sale el Sol
mc.setBlock(x, y, z+6, blockType,2) # Direccion -Z o NORTE
mc.setBlock(x, y, z+8, blockType,3) # Direccion +Z o SUR
mc.setBlock(x, y, z+10, blockType,4) # Direccion -X o OESTE Invetido
mc.setBlock(x, y, z+12, blockType,5) # Direccion +X o ESTE Invertido
mc.setBlock(x, y, z+14, blockType,6) # Direccion -Z o NORTE Invertido
mc.setBlock(x, y, z+16, blockType,7) # Direccion +Z o SUR Invertido
mc.setBlock(x, y, z+18, blockType,8) # Cualquier valor de [data] que no existe se convierte en 0
mc.setBlock(x, y, z+20, blockType,9) # y se pone el bloque hacia -X
mc.setBlock(x, y, z+22, blockType,10) 
mc.setBlock(x, y, z+24, blockType,11)
mc.setBlock(x, y, z+26, blockType,12) 
mc.setBlock(x, y, z+28, blockType,13) 
mc.setBlock(x, y, z+30, blockType,14)
mc.setBlock(x, y, z+30, blockType,15)

# Se mueve hacia X negativa para repetir lo mismo perocon otro bloque
x = x-2
