import os
import msvcrt
import random

def dibujarLinea():
    print("----------------------------------------------------------------------------------------------------------------")

def mostrarTitulo(titulo):
    print("----------------------------------------------------------------------------------------------------------------")
    print(titulo.upper())
    print("----------------------------------------------------------------------------------------------------------------")

def limpiarTerminal():
    os.system("cls")

def convertToCell(text):
    num = 9 - len(text)
    spaces = ""
    for j in range(int(num / 2)):
        spaces += " "
    
    text = spaces + text + spaces
    if len(text) == 8:
        text = text + "-"
    return text    

# Inicializa las matrices con cadenas vacías
matriz = [["[ ]" for _ in range(12)] for _ in range(12)]
matrizNav = [["[ ]" for _ in range(12)] for _ in range(12)]


    
    


def LlenarMatriz(matriz, width, height, num_minas):
    for i in range(height):
        matriz.append(["W"] * width)

    minas_colocadas = 0
    while minas_colocadas < num_minas:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        if matriz[y][x] != "(M)":
            matriz[y][x] = "(M)"
            minas_colocadas += 1

def CalcularValores(matriz):
    direcciones = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for y in range(len(matriz)):
        for x in range(len(matriz[y])):
            if matriz[y][x] == "(M)":
                continue

            minas_cercanas = 0
            for dx, dy in direcciones:
                nx, ny = x + dx, y + dy

                if 0 <= nx < len(matriz[0]) and 0 <= ny < len(matriz):
                    if matriz[ny][nx] == "(M)":
                        minas_cercanas += 1

            matriz[y][x] = str(minas_cercanas) if minas_cercanas > 0 else "-"

def SetGameOver():
    for i, fila in enumerate(matrizNav):
        if i <= 11:
            for j in range(len(fila)):
                if matriz[i][j] == "(M)":
                    fila[j] = "(M)"
                else:
                    fila[j] = "."  

    matrizNav[5][1] = "[G]"
    matrizNav[5][2] = "[A]"
    matrizNav[5][3] = "[M]"
    matrizNav[5][4] = "[E]"
    matrizNav[5][7] = "[O]"
    matrizNav[5][8] = "[V]"
    matrizNav[5][9] = "[E]"
    matrizNav[5][10] = "[R]"

    
    
def SetWin():
    for i, fila in enumerate(matrizNav):
        if i <= 11:
            for j in range(len(fila)):
                if matriz[i][j] == "(M)":
                    fila[j] = "(M)"
                else:
                    fila[j] = "."  

    matrizNav[5][1] = "[Y]"
    matrizNav[5][2] = "[O]"
    matrizNav[5][3] = "[U]"
    matrizNav[5][7] = "[W]"
    matrizNav[5][8] = "[I]"
    matrizNav[5][9] = "[N]"






def obtenerCampos(x, y):
    direcciones = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    campos_limpios = []
    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(matrizNav) and 0 <= nx < len(matrizNav[0]):
            if matriz[ny][nx] == "-":  
                matrizNav[ny][nx] = "C" 
                campos_limpios.append((nx, ny))
            elif matriz[ny][nx] != "-" and matriz[ny][nx] != "(M)": 
                matrizNav[ny][nx] = "C"  
    return campos_limpios


def EmpezarLimpieza(x, y):
    celdas_a_limpiar = [(x, y)]
    procesadas = set(celdas_a_limpiar)

   
    while celdas_a_limpiar:
        x, y = celdas_a_limpiar.pop(0)  
        vecinos = obtenerCampos(x, y)
        for vecino in vecinos:
            if vecino not in procesadas:
                celdas_a_limpiar.append(vecino)
                procesadas.add(vecino)

    
    return list(procesadas)


def verificarVictoria():
    for y in range(12):
        for x in range(12):
            if matriz[y][x] == "M":
                if matrizNav[y][x] != "[X]":
                    return False
            elif matriz[y][x] == "-" and matrizNav[y][x] != "C":
                return False
    return True


def Dibujar():
    limpiarTerminal()
    mostrarTitulo("Buscaminas By Kendall Guido U San Marcos")
    for j, fila in enumerate(matrizNav):
        txt = ""
        for i in range(len(fila)):
            if i == 0 and fila[i] == "x":
                dibujarLinea()
            
            if i == px and j == py:  # Celda seleccionada
                if fila[i] == "C":
                    txt += convertToCell("< " + matriz[j][i] + " >")
                else:
                    txt += convertToCell("< " + fila[i] + " >")
            else:
                if fila[i] == "C":
                    txt += convertToCell(""+matriz[j][i]+"")
                else:
                    txt += convertToCell(fila[i])
        
        print("| " + txt + " |")
    dibujarLinea()

gameOver = False
win = False
salir = False
while not salir:
    limpiarTerminal()
    matriz = [["[ ]" for _ in range(12)] for _ in range(12)]
    matrizNav = [["[ ]" for _ in range(12)] for _ in range(12)]
    LlenarMatriz(matriz, 12, 12, random.randint(10, 25))
    CalcularValores(matriz)
    
    gameOver = False
    win = False 
    px = 0
    py = 0
    tecla2 = "S"
    tecla = "x"
    mov = 0

    while not gameOver and not win:
        limpiarTerminal()
        mostrarTitulo("  Buscaminas By Kendall Guido U San Marcos")
        Dibujar()
        
        print(str(tecla))
        print(str(tecla2))
        print("Enter para reiniciar, Escape para salir...")
        print("Presiona una tecla (Arriba, Abajo, Izquierda, Derecha) para navegar...")
        print("Presiona 'C' para cavar o 'X' para marcar como mina...")
        
        tecla = msvcrt.getch()
        
        if tecla == b"c" or tecla == b"C":
            if mov == 0:
                matriz[py][px] = "-"
            mov += 1
         
            matrizNav[py][px] = "C"
            if matriz[py][px] == "(M)":
                SetGameOver()
          
               
            else:
                if matriz[py][px] == "-":
                    EmpezarLimpieza(px, py)
            
            if verificarVictoria():
                SetWin()
               # win= True
               
                
                    
        elif tecla == b"x" or tecla == b"X":
           # print("Tecla C presionada")
        
            if verificarVictoria():
                SetWin()
                win= True
                tsc= msvcrt.getch()
            else:
                if matrizNav[py][px] =="[X]":
                    matrizNav[py][px]= "[ ]"
                else:
                    matrizNav[py][px] = "[X]"
            
        elif tecla == b"\r":
            gameOver = True    
            
        else:
            tecla2 = msvcrt.getch()

            width = 12
            height = 13

            if tecla2 == b"H":  # Flecha Arriba
                if py > 0:
                    py -= 1
                else:
                    if px < 2:
                        py = height - 2
                    else:
                        py = height - 1
            elif tecla2 == b"K":  # Flecha Izquierda
                if px == 0:
                    px = width - 1
                else:
                    if py == height - 1 and px == 2:
                        py = height - 2
                    px -= 1
            elif tecla2 == b"P":  # Flecha Abajo
                if px < 2:
                    if py == height - 2:
                        py = 0
                    else:
                        py += 1
                else:
                    if py == height - 1:
                        py = 0
                    else: 
                        py += 1
            elif tecla2 == b"M":  # Flecha Derecha
                if px == width - 1:
                    px = 0
                    if py == height - 1:
                        py = height - 2
                else:
                    px += 1
                    
            elif tecla2 == b'\x1b':
                salir = True
                gameOver= True


mostrarTitulo("Universidad San Marcos -  Kendall Guido")
os.system('exit')


