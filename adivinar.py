import time 
nombre=input("¿cómo te llamas? ")
print ("hola, "+nombre, "que comience la adivinanza")
print (" ")
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

	tuletra=imput("introduce una letra: ")
	tupalabra+=tuletra

	if tuletra not in palabra:
		vidas-=1
		print("equivocado mi pana")
		print("te quedan ",+vidas," vidas")
	if vidas==0:
		print ("perdiste")
else: 
	print ("gracias por participar")
	