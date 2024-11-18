
#La tienda Vintage necesita un programa para calcular el precio a pagar por la compra que realiza cada cliente. 
#El dueño de la tienda le pide que muestre el detalle de la compra, no tan solo el monto total. Suponga que cada cliente 
#compra un solo artículo, pero puede llevar varias unidades de ese artículo. Cada artículo de la tienda pertenece a una 
#categoría y se van a aplicar descuentos según la categoría como se muestra en la siguiente tabla: 

#Códigos:  [101,205,105,301]
#Categoría: ["Bisutería","Calzado","Lencería","Abrigos"]
#Descuento: [20,35,10,50]
 
#Aplicar descuento del 13 
  
# Entrada: codigo,cantidad,categoría
#proceso: calcularTotal(),calcularImpuesto(),calcularDescuento()
#Salida: total

import os

#Inicio del código
codigos=[101,205,105,301]
descuentos =[20,35,10,50]
categorias=["Bisutería","Calzado","Lencería","Abrigos"]
salir =False
total=0
codigo=0
cantidad=0
categoria=""
descuento =0
montoDescuento=0
montoImpuesto=0
precio=0.00
subtotal=0



#Funciones
def dibujarLinea():
    print("----------------------------------------------------------------------")
    
def mostrarTitulo(titulo):
    print("----------------------------------------------------------------------")
    print(titulo.upper())
    print("----------------------------------------------------------------------")

def limpiarTerminal():
    os.system('cls')
    
    
def limpiarDatos():
    global precio
    global cantidad 
    global descuento
    global montoDescuento
    global total
    global montoImpuesto
    global subtotal
    global codigo
    global categoria

    # Restablecer las variables a sus valores iniciales
    precio = 0
    cantidad = 0
    descuento = 0
    montoDescuento = 0
    total = 0
    montoImpuesto = 0
    subtotal = 0
    codigo = 0
    categoria = ""
    
    
    
def verificarInput(value):
    num = int(value)
    valido= True
    global codigo
    global categoria
    global codigos
    global categorias
    global descuento
    
    for i in range(4):
        if num == codigos[i]:
            codigo= codigos[i]
            categoria = categorias[i]
            descuento= descuentos[i]
            return True
        
    return False


def calcularTotal():
    global precio 
    global cantidad
    global codigo
    global descuento
    global montoDescuento
    global montoImpuesto
    global total
    global subtotal
    
    precioFinal =  precio * cantidad
    montoDescuento = (precioFinal/100)*descuento
    precioFinal -= montoDescuento
    montoImpuesto = (precioFinal/100)*13
    subtotal= precioFinal
    precioFinal= precioFinal + montoImpuesto
    total= precioFinal
        
    
def mostrarResultado():
    
    global precio 
    global cantidad
    global codigo
    global descuento
    global montoDescuento
    global montoImpuesto
    global total
    global categoria
    mostrarTitulo("CODIGO: " + str(codigo)+"\nCategoría: "+ categoria+"\nPrecio unitario: " + str(precio) + "\nCantidad: " + str(cantidad) + "\nDescuento:  "+str(descuento) +"\nMonto Descuento: "+ str(montoDescuento) +"\nSubtotal: "+str(subtotal)+ "\nImpuesto: "+ str(montoImpuesto) +"\nTotal: " + str(total)   )
    
    

while salir==False:
    limpiarTerminal()
    mostrarTitulo("VINTAGE POS                 " + " Codigo: "+str(codigo) +"  Precio: "+ str(precio)+ "  Cantidad: "+str(cantidad) )
    
    if codigo ==  0:
        print("Códigos disponibles: \n")
        
        for i in  range(4):
            print(str(codigos[i]) +" - "+ categorias[i] ) 
        
        
        codigoValido = False
        while codigoValido == False:
            codigo=  input("\nIngrese el código: ")
            if verificarInput(codigo):
                codigoValido = True
            else:
                mostrarTitulo("x     ERROR: Debe ingresar un código válido     x")    
                           
    elif codigo != 0  and precio == 0:
    
        precio= float(input("Ingrese el precio: "))
        
    elif codigo != 0  and precio != 0  and cantidad == 0:
      
        cantidad = float(input("Ingrese la Cantidad: "))
        
    elif codigo != 0  and precio != 0  and cantidad != 0:
        calcularTotal()
        mostrarResultado()
        
        
      
    if(total != 0):
        textoSalida = input("¿Desea calcular los detalles de otro Producto? (s/n):  ")
        if 'n' in textoSalida :
            salir=True
        else:
            limpiarDatos()
    

mostrarTitulo("\nUniversidad de San Marcos\nKendall Jefferson Guido Cruz \nEjercicio 1\nCálculo de precios\n2024\n ")
os.system('exit')
    
    
    











