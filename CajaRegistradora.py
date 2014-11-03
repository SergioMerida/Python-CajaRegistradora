#coding: utf-8
import time
print ""
print "Bienvenido a MOS S.A"
print "Seleccione la opcion que desea con el número que le representa."
precios = {}
inventario = {}
total_lista = []
#Opcion inventario
def limpiar():
	del total_lista[:]
	print "Puede ingresar nueva factura."
		
def funcion1():
	while True:
		producto = raw_input("Ingrese el nuevo producto: ")
		if producto.isalpha():
			producto.lower()
			break
		else:
			print "Solo puedes ingresar letras"
	while True:
		try:
			precio = float(raw_input("Ingrese precio: "))
			cantidad = int(raw_input("Ingrese cantidad existente: "))	
			break
		except ValueError:
			print "Solo puede ingresar numeros"
#Aca ingresara al dic. precios el producto y precio  
	precios[producto] = precio
	inventario[producto]= cantidad #producto y cantidad
	for i in precios:
		print ""
		print "Usted ingreso", i, "al inventario" 
		print "Con un precio de", precios[i]
		print "Y una cantidad de", inventario[i]
		print ""
#Opcion caja
def calcularFactura():
	cliente = {} #Dic. local	
	while True:
		try: 
			a = raw_input("Ingrese producto: ")
			b = int(input("Ingrese la cantidad: "))
			cliente[a] = b #Al dic. se le ingresara el producto que coloque y cantidad
			calc = inventario[a] - cliente[a] #a inventario le resta el nuevo dic. cliente
			inventario[a] = calc 
			total = precios[a] * cliente[a] #precio por la cantidad que ingreso
			total_lista.append(total) #ingresa un valor a total_lista
			break
		except KeyError:
			print "Esta opcion no se encuentra en el inventario, intente nuevamente"
#Opcion facturar
def factura():
	print """
Elija una opción: 
1 No cuenta con tarjeta de cliente preferencial
2 Cuenta con tarjeta Gold
3 Cuenta con tarjeta Silver
""" #Menu	
	while True: 	
		try: 
			opcion = input("> ") #Aca ingresa el cliente la opcion 1 2 o 3
			break
		except (ValueError, NameError):
			print "Solo puede ingresar numeros, intenta nuevamente" 
	
	while (opcion >= 4): #Si la opcion es mayor o igual a 4 desplegara
		print "Opcion no valida elija nuevamente, recuerda que es del 1 al 3"		
		opcion = input("> ") #Y volvera a solicitar que de una opcion correcta
	total2 = sum(total_lista) #llama el valor de total_lista
	iva = 0.12
	gold = 0.05
	silver = 0.02
	calc_iva = total2 * iva #Calcula el iva
	iva_agregado = calc_iva + total2 #Agrega el iva a la cantidad
	if opcion == 1: # no se le hace ningun descuento
		print "Calculando los datos...."
		time.sleep(2)
		print "El total de su cuenta es %s mas el iva %s" % (total2, calc_iva)
		print "El total a pagar es %s" % iva_agregado
		respuesta = 0 
		while (respuesta==0):
			a =	raw_input  ("Desea salir de facturación Si o No: ")
			b = a.lower()
			if b == "si":
				limpiar()
				respuesta = 1
			elif b == "no":
				break
				respuesta = 1
			else:
				print "Debe ingresar una opción valida"
	elif opcion == 2: #Descuento Gold
		print "Calculando los datos...."
		time.sleep(2)		
		calc_gold = iva_agregado * gold
		desc_gold = iva_agregado - calc_gold
		print "El total de su cuenta es %s mas el iva %s y su descuento de tarjeta Gold que es %s" % (total2, calc_iva, calc_gold)
		print "El total a pagar es %s " % desc_gold
		respuesta = 0
		while (respuesta==0):
			a =	raw_input  ("Desea salir de facturación Si o No: ")
			b = a.lower()
			if b == "si":
				limpiar()
				respuesta = 1
			elif b == "no":
				break
				respuesta = 1
			else:
				print "Debe ingresar una opción valida"
	elif opcion == 3: #Descuento Silver
		print "Calculando los datos...."
		time.sleep(2)		
		calc_silver = iva_agregado * silver
		desc_silver = iva_agregado - calc_silver
		print "El total de su cuenta es %s mas el iva %s y su descuento de tarjeta Silver que es %s" % (total2, calc_iva, calc_silver)
		print "El total a pagar es %s " % desc_silver
		respuesta = 0
		while (respuesta==0):
			a =	raw_input  ("Desea salir de facturación Si o No: ")
			b = a.lower()
			if b == "si":
				limpiar()
				respuesta = 1
			elif b == "no":
				break
				respuesta = 1
			else:
				print "Debe ingresar una opción valida"

#Menu principal
respuesta = 0
while (respuesta==0):
	opcion = raw_input("1 Inventario \n2 Caja \n3 Facturar \n4 Salir \n> ")
	if opcion == "1": #dirige hacia funcion1
		funcion1()
		respuesta = 0
	elif opcion == "2": #calcularFactura()
		calcularFactura()
		respuesta = 0
	elif opcion == "3": #factura()
		factura()
		respuesta = 0
	elif opcion == "4":
		print "Gracias por utilizar nuestro servicio, que tenga un buen dia"
		respuesta = 1		
	else:
		print "Debe ingresar un numero del 1 al 4 dependiendo de lo que quiera realizar no se aceptan letras \n"
