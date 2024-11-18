#Una casa de cambio le solicita que haga un programa que calcule la cantidad de dinero a entregar a un cliente. 
#La casa de cambio realiza cambio de dólares a colones, de euros a colones, de colones a dólares y de colones a 
#euros. El programa debe funcionar N veces, y realiza una sola conversión a la vez. 
#Establezca el tipo de cambio del dólar o del euro en un monto fijo o puede pedirlo al usuario al inicio, esa decisión la 
#toma usted como programador.


import os


#Funciones
def dibujarLinea():
    print("----------------------------------------------------------------------")
    
def mostrarTitulo(titulo):
    print("----------------------------------------------------------------------")
    print(titulo.upper())
    print("----------------------------------------------------------------------")

def limpiarTerminal():
    os.system('cls')



monedas = ["Colón","Dolar","Euro"]
montosColones=[1,512,557] 
transacciones= ["Dolar a Colon","Colon a Dolar", "Euro a Colon","Colón a Euro"]
colon =0
euro=0
dolar=0

resultado = 0



transaccion= -1
salir =False

while salir==False:
    
    limpiarTerminal()
    mostrarTitulo("CASA DE CAMBIO")
 

    if transaccion ==-1:
        print("Transacciones disponibles: ")
        for i in range(4):
            print( str(i) +") "+ transacciones[i])
        transaccion = int(input("Ingrese un valor: "))
        
    #transacciones= ["Dolar a Colon","Colon a Dolar", "Euro a Colon","Colón a Euro"]  
    
    elif transaccion != -1 :
        if transaccion == 0:
            dolar= float(input("Ingrese la cantidad de Dólares que desea Convertir a Colones: "))
            resultado= dolar* montosColones[1] 
            mostrarTitulo( str(dolar) +" dólares son:  "+ str(resultado)  + " colones")
            
        elif transaccion==1:
            colon= float(input("Ingrese la cantidad de Colónes que desea Convertir a Dólares: "))
            resultado= colon / montosColones[1] 
            mostrarTitulo( str(colon) +" colónes son:  "+ str(resultado)  + " dólares")
        elif transaccion==2:
            euro= float(input("Ingrese la cantidad de Euros que desea Convertir a Colones: "))
            resultado= euro* montosColones[2] 
            mostrarTitulo( str(euro) +" euros son:  "+ str(resultado)  + " colones")
        elif transaccion==3:
            colon= float(input("Ingrese la cantidad de Colones que desea Convertir a Euros: "))
            resultado= colon* montosColones[2] 
            mostrarTitulo( str(colon) +" euros son:  "+ str(resultado)  + " colones")
        else:
            mostrarTitulo("x     ERROR: Debe ingresar un número válido     x")    
            transaccion=-1
            resultado=0
       
            
            
        
    if resultado != 0:    
        textoSalida = input("¿Desea realizar otra transacción? (s/n):  ")
        if 'n' in textoSalida :
            salir=True
        else:
            resultado=0
            colon=0
            euro=0
            dolar=0
            transaccion=-1
            salir= False








mostrarTitulo("\nUniversidad de San Marcos\nKendall Jefferson Guido Cruz \nEjercicio 2\nCása de Cambio\n2024\n ")
os.system('exit')
    



