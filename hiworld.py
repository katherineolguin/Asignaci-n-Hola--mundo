# 1. TAREA: imprime "Hola, mundo"
msge= "Hola, mundo"
print( msge )

# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Kathy"
print( "Hola,",name )	# con una coma
print( "Hola, "+name)	# con un +


# 3. imprimir "Hola 42!" con el número en una variable
name = 6
print( "Hola",name)	# con una coma
#print("Hola "+name)	# con una +	-- este debería arrojar un error!
print("Hola "+str(name))

# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables

fave_food1 = "sushi"
fave_food2 = "rissoto"
print( "Amo comer {fave_food1} y {fave_food2}".format( fave_food1 = "sushi", fave_food2 = "pizza"))     #con .format()
print(f"Amo comer {fave_food1} y {fave_food2}" ) # con una cadena f

