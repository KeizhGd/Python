

import os
import msvcrt

def dibujarLinea():
    print("--------------------------------------------------------------------------------------------------------")
    
def mostrarTitulo(titulo):
    print("--------------------------------------------------------------------------------------------------------")
    print(titulo.upper())
    print("--------------------------------------------------------------------------------------------------------")

def limpiarTerminal():
    os.system('cls')
    
def convertToCell(text):
    num = 25 - len(text)
    spaces= ""
    for j in range( int(num/2)):
        spaces+=" "
    

    
    text  =  spaces + text +spaces 
    if len(text) == 24:
        text=text+" "
    return text     
    
#La empresa Aero Lux se dedica a transporte aéreo en el territorio nacional. Prestan un
#servicio de lujo por lo cual las aeronaves tienen pocos asientos, confortables y espaciosos.
#Cada aeronave cuenta con 5 filas de 4 asientos.
#Se le pide crear un programa para registrar los nombres de los pasajeros asignados a los
#asientos de una aeronave. Cuando se solicite debe imprimir para cada asiento, el nombre
#de quien lo compró y si no ha sido asignado debe decir “Vacío”. También debe ofrecer la
#opción de consultar quién está sentado en un asiento específico. 

matriz = [['Vacío' for _ in range(4)] for _ in range(6)]
matrizNav = [['Vacío' for _ in range(4)] for _ in range(6)]

matrizNav[5][0]="x"
matrizNav[5][1]="x"
matrizNav[5][2]="Portada"
matrizNav[5][3]="Salir"
px=0
py=0
tecla2=None




def Dibujar():
 
    limpiarTerminal()
    mostrarTitulo("                                            AERO LUX")
    for j,fila in enumerate(matrizNav):
        txt =""
        for i in range(len(fila)):
            if i ==0 and fila[i]=="x":
                dibujarLinea()
            if i == px and j == py:
                txt+= convertToCell("[  "+fila[i]+"  ]")
            else:
                txt+= convertToCell(fila[i])
                
            
            
        print("| " + txt +" |")
    dibujarLinea()



salir =False
tecla=''
digitar = False
txts=""
psx=0
psy=0
while salir ==False:
   
    Dibujar()
    print("Px :" + str(px) + " Py: " + str(py))

    print("Teclas: "+ str(tecla2))
    print("Presiona una tecla (Arriba, Abajo, Izquierda, Derecha) para navegar o Enter para Usar...")

    tecla = msvcrt.getch()  

   

 

    if tecla == b'\r':  #enter
        
        if(py < 5):
            
            txt = input("Digite el nombre del Cliente para este asiento: ")
            value= "Vacío"
            if txt:
                value=txt
                
            matrizNav[py][px]= value
         
            txts=""
        
        elif px == 2:
            mostrarTitulo("\nUniversidad de San Marcos\nKendall Jefferson Guido Cruz \nEjercicio 1\nGanancias Semanales\n2024\n ")
            vals = msvcrt.getch() 
        else:
            dibujarLinea()
            print("Gracias por utilizar este Sistema...")
            salir=True
    else:
     
     
        tecla2 = msvcrt.getch()

        if tecla2 == b'H':   #Flecha Arriba
        
            if py > 0:
                py-=1
            else:
                if px < 2:
                    py=4
                else:
                    py = 5
            
        elif tecla2 == b'K':    #Flecha Izquerda
        
            if px ==0:
                px=3
            else:
                
                if py == 5 and px == 2:
                    py=4 
                px-=1
        elif tecla2 == b'P':   #Flecha Flecha Abajo
            if px < 2:
                if py == 4:
                    py=0
                else:
                    py+=1
            else:
                if py ==5:
                    py = 0
                else: 
                    py+=1
        
        elif tecla2 == b'M':   #Flecha Derecha
            if px ==3:
                px=0
                if py == 5:
                    py=4
            else:
                px+=1
        


os.system('exit')

        
        
        

        
           

    
