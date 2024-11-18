import os
import msvcrt

def dibujarLinea():
    print("-------------------------------------------------------------------------------------------------------------------------")
    
def mostrarTitulo(titulo):
    print("-------------------------------------------------------------------------------------------------------------------------")
    print(titulo.upper())
    print("-------------------------------------------------------------------------------------------------------------------------")

def limpiarTerminal():
    os.system('cls')
    
#La profesora necesita un programa que calcule la nota final para el curso Lógica de
#Programación. Las calificaciones deben almacenarse. Suponga que tiene 5 estudiantes
#que realizan 4 actividades evaluativas. El programa debe diseñarse de forma que con
#pequeños cambios funcione para n estudiantes. Además de la nota final del curso también
#debe indicar cuál estudiante tiene la nota más alta.


estudiantes = [['Juan', 5, 7, 3, 9, 6.0, 'No'],
['Ana', 8, 9, 4, 7, 7.0, 'No'],
['Carlos', 3, 5, 8, 6, 5.5, 'No'],
['Luisa', 7, 7, 7, 6, 6.75, 'No'],
['José', 8, 10, 9, 9, 9.0, 'Sí']
]

casillas = ["Nombre","Actividad 1" ,"Actividad 2", "Actividad 3 ", "Actividad 4 ", "Nota Final","Mejor Promedio" ]
estudianteMejor = ["",0,0,0,0,0,"No"]
estudiante = ["",0,0,0,0,0,"No"]


def convertToCell(text):
    num = 16 - len(text)
    spaces= ""
    for j in range( int(num/2)):
        spaces+=" "
    
    text  =  spaces + text +spaces 
    if len(text) == 15:
        text=text+" "
    return text+"|"     
    
    
    
def Dibujar():


    for j,fila in enumerate(estudiantes):
        txt =""
        if j ==0:
            for c in range(len(casillas)):
                txt+=convertToCell( str(casillas[c])) 
            print("| " + txt +" ")
        dibujarLinea()
        txt =""
        for i in range(len(fila)):
            txt+=convertToCell( str(fila[i])) 
        print("| " + txt +" ")
    dibujarLinea()
     


def calcularNota():
    for fila in estudiantes:
        fila[-2] = (fila[1] + fila[2]+fila[3]+fila[4])/4
        CalcularMayor()
        


def CalcularMayor():
    global estudianteMejor
    mayorNota =0
    idE =-1
    for id,fila in  enumerate(estudiantes):
       nota = fila[-2]
       if nota > mayorNota:
           mayorNota=nota
           idE=id
    
    for fila in estudiantes:
        fila[-1] = "No"
    
    estudiantes[idE][-1]="Si"
    estudianteMejor=  estudiantes[idE].copy()            




menu = ["Agregar Estudiante","Ver Estudiantes","Portada","Salir"]



salir = False

while salir == False:
    limpiarTerminal()
    mostrarTitulo("                                            Estudiantes")    
    for i in range(4):
        print(str(i+1) + ") " + menu[i])
    val =  input("Digite un Valor: ").strip()
    value =0
    if val:
        value= int(val)
    if value == 1:
        estudiante[0] = input("Digite el nombre de estudiante: ")
        estudiante[1] = float(input("Digite la nota de la Actividad 1: "))
        estudiante[2] = float(input("Digite la nota de la Actividad 2: "))
        estudiante[3] = float(input("Digite la nota de la Actividad 3: "))
        estudiante[4] = float(input("Digite la nota de la Actividad 4: "))
        
        estudiantes.append(estudiante)
        calcularNota()
        mostrarTitulo("                                            RESULTADOS")  
        Dibujar()
        tecla = msvcrt.getch()
        
    elif value ==2:
        mostrarTitulo("                                            RESULTADOS")  
        Dibujar()
        
        tecla = msvcrt.getch()
    elif value == 3:
      
        mostrarTitulo("\nUniversidad de San Marcos\nKendall Jefferson Guido Cruz \nEjercicio 1\nGanancias Semanales\n2024\n ")
        tecla = msvcrt.getch()
    else:
        dibujarLinea()
        print("Gracias por utilizar este Sistema...")
        salir=True
        
    
    
    
    
    
    







