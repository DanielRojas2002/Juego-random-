import random
import time

class adivina:
    def __init__(self,numero,nombre):
        self.__numero=numero
        self.__nombre=nombre
        
    
    def suerte(self):
        aleatorio=random.randrange(1,50)
        contador=0
        
        
        while contador in range (0,4,1):
            if aleatorio==self.__numero:
                time.sleep(3)
                print(separador)
                print(f"Felicidades {self.__nombre} el numero que me diste : {self.__numero} es el numero en que estaba pensando")
                print("Me ganaste :(")
                print(separador)
                contador=6
            
            elif aleatorio!=self.__numero:
                if aleatorio<self.__numero:
                    time.sleep(3)
                    print(separador)
                    print("El numero en el que estoy pensando es menor ")
                    print(separador)
                    numero=int(input("Dime el numero en el que estoy pensando : "))
                    self.__numero=numero
                    contador=contador+1
                    
                else:
                    time.sleep(3)
                    print(separador)
                    print("El numero en el que estoy pensando es mayor")
                    print(separador)
                    numero=int(input("Dime el numero en el que estoy pensando : "))
                    self.__numero=numero
                    contador=contador+1
                
        if contador==4:
            print(separador)
            print("Se acabaron tus vidas")
            print(separador)

separador=("*"*30)
opcion="Si"

while opcion=="Si"or opcion=="si":
    print("Bienvenido al juego")
    print(separador)
    
    print("El juego consiste en que adivines el numero en el que estoy pensando")
    print("Tienes 5 vidas ")
    print(separador)
    nombre=input("Dime tu nombre : ")
    print(separador)
    print("Escribiendo en la Base de Datos...")
    time.sleep(3)
    print(separador)
    numero=int(input("Dime el numero en el que estoy pensando : "))
    objeto1=adivina(numero,nombre)
    objeto1.suerte()
    print("*"*30)
    opcion=input("Quieres seguir jugando: ")