# Practica-9
def suma(a, b):
     c=a+b
     return c

def restar(a,b):
    return a-b

def multiplicar (a,b):
    return a*b

def div_entera(a,b):
    if  b == 0:
        print("error division sobre 0")
        return  
    return a//b

def division(a,b):
    if b == 0:
        print("error division sobre 0")
        return  
    return a//b

def modulo(a,b):
    if b==0:
        print("error division sobre 0")
        return
    return a%b

def potencia(a,b):
    return a**b

def main():
    print ("ingrese los valores")
    x = int(input())
    y = int(input())
    print("seleccione la operacion a realizar")
    print(" 1.Sumar\n 2.Restar\n 3.Multiplicar\n 4.Division entera")
    print(" 5.Division\n 6.Modulo\n 7.Potencia\n 10.Salir")
    
    op = int(input())
    

    if  op == 1:
        print(suma(x,y))
    elif op == 2:
        print(restar(x,y))
    elif op ==3: 
        print(multiplicar(x,y))
    elif op == 4:
        print(div_entera(x,y))
    elif op == 5:
        print(division(x,y))
    elif op == 6:
        print(modulo(x,y))
    elif op == 7:
        print(potencia(x,y))
    else:
        print("opcion no valida")
       

if __name__ == "__main__" :
     main()

