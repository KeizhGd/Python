

import os

def dibujarLinea():
    print("------------------------------------------------------------------------------------------------------------------------")
    
def mostrarTitulo(titulo):
    print("------------------------------------------------------------------------------------------------------------------------")
    print(titulo.upper())
    print("------------------------------------------------------------------------------------------------------------------------")


def limpiarTerminal():
    os.system('cls')
    
    
#Juan Pablo trabaja en su tiempo libre, para una plataforma de transporte. Haga un
#programa en Python que le permita a Juan Pablo registrar el monto ganado por día,
#suponiendo que trabaja 7 días a la semana. Al finalizar la semana le mostrará el total y le
#indicará el día que ganó más dinero.


salir = False

monto= [0,0,0,0,0,0,0]
dias= ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]

suma = 0
maximo= -1
valueMax= 0;


limpiarTerminal()
mostrarTitulo("GANANCIAS SEMANALES")
print("En este apartado se calcularán los ingresos obtenidos la ultima semana.\nFavor brindar los datos solicitados.")
dibujarLinea()
for i  in range(7):
    value=0
    entrada = input("Digite el monto obtenido el día "+ dias[i] +": ").strip()
    
    
    if not entrada:
        value=0
    else:
        value= float(entrada)
    monto[i]= value
    suma = suma + float(monto[i])   
    if monto[i] > valueMax :
        maximo = i
        valueMax= float(monto[i]) 
    
    print(str(valueMax))


limpiarTerminal()
mostrarTitulo("RESULTADOS")
rows = [""]*7 
cols = [""]*7

for i in range(7):
    numCols = 10 - len(dias[i])
    spaces= ""
    for j in range(numCols):
        spaces+=" "
    spaces+="|"
    cols[i] = dias[i] +spaces
    
    numRows = 10 - len(str(monto[i]))
    spaces= ""
    for j in range(numRows):
        spaces+=" "
    spaces+="|"
    rows[i] = str(monto[i]) +spaces
    
    
print(cols)   
print(rows)   
    
dibujarLinea()
print("El total de ganancias semanales es: "+ str(suma) +" colones.")

print("El día con mayores ingresos fue el "+ dias[maximo]  + " por un total de " + str(max(monto)) +" colones generados."   )  
dibujarLinea()
val = input("Presione cualquier tecla para continuar...")
mostrarTitulo("\nUniversidad de San Marcos\nKendall Jefferson Guido Cruz \nEjercicio 1\nGanancias Semanales\n2024\n ")
os.system('exit')