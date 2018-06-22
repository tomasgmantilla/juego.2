'''
Muy buen trabajo Tomas, el juego esta funcionando y pudiste practicar con varias herramientas de python.

El código funciona perfecto.

Recomendaciones:
1. Agrega comentarios en la mitad del código sobre lo que estas haciendo en el código, puedes usar # para ello.
2. Es preferible que utilices la convención snake_case para nombrar las variables:
Por ejemplo: en vez de nombrar tupalabra => utiliza tu_palabra

RETOS:
Ya que lograste muy bien este primer reto, te propongo lo siguiente:
1. En la versión del juego actual palabra siempre es 'hermano'. Modifica el juego para que palabra pueda ser cualquier palabra
de esta lista de palabras:
'hermano', 'pajaro', 'futbol', 'cuadrilatero', 'emprendimiento', 'eficiencia', 'chocolatier', 'referencia'

2. Continua con los retos de la academia Hack.

MUY BUEN TRABAJO!

'''

import time 
nombre=input("¿cómo te llamas? ")
print ("hola, "+nombre, "que comience la adivinanza")
print (" ")
# Ejemplo de comentario:
# Esperamos un segundo para ejecucion de la line de abajo
time.sleep(1)
print ("comienza a adivinar")
time.sleep(0.5)
palabra='hermano'
tupalabra=''
vidas=5

while vidas > 0:
	fallas=0
	for letra in palabra:
		if letra in tupalabra:
			print(letra,end="")
		else:
			print("*",end="")
			fallas+=1
	if fallas==0:
		print("")
		print("asi mismo bro!")
		break

	tuletra=input("introduce una letra: ")
	tupalabra+=tuletra

	if tuletra not in palabra:
		vidas-=1
		print("equivocado mi pana")
		print("te quedan ",+vidas," vidas")
	if vidas==0:
		print ("perdiste")
else: 
	print ("gracias por participar")
	
