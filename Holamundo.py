#comentario de una sola linea 
'''
comentario de multilineas 
lenguaj c es un lenguaje compilado y una vez compilado no depende del compilador 
python es un lenguaje interpretado, no genera ejecutable, es decir siempre que se quiera ejecutar se tiene que llamar al 
interprete de python
''' 
print ("hola mundo") 
x=10
print(type(x))
print(x)
x = y = z = 2.3
print(x,y,z)
print(type(x))
x="cadena"
print(type(x))

c1 = "hola"
c2 = "Alejandro"
saludo = c1+" "+c2
print(saludo)

saludo2 = "{} {} {}".format(c1, c2, 3)
print(saludo2)

saludo3 = "Cambio de orden {1} {2} {0}".format(c1, c2, 3)
print(saludo3)
