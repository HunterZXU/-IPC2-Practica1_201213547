import os
import time
import informacion


def menu_Principal():
    titulo = f"Menu Principal"
    titulo = titulo.center(37)
    print("="*39)
    print (titulo)
    print("="*39)
    print("1) Registrar Producto")
    print("2) Registrar Cliente")
    print("3) Realizar Compra")
    print("4) Reporte de Compra")
    print("5) Datos del Estuadinte")
    print("6) Salir")
    print("="*39)
    print()
    while True:
        try:
            seleccion = int(input("Ingrese un valor: "))
            if seleccion == 1:
                limpiar_consola()
                print("Proceso Completado, se ha almacenado la Informacion")
                time.sleep(3)
                limpiar_consola()
                menu_Principal()
            elif seleccion == 2:
                limpiar_consola()
                print("Se han cargado las instrucciones correctamente, se procede ha realizar cada operacion")
                time.sleep(5)
                limpiar_consola()
                print("="*75)
                print("="*75)
                print("Proceso Completado")
                time.sleep(3)
                limpiar_consola()
                menu_Principal()
            elif seleccion == 3:
                limpiar_consola()
                submenu()
                time.sleep(3)
                menu_Principal()
            elif seleccion == 4:
                pass
            elif seleccion == 5:
                limpiar_consola()
                print("                             Datos:                                   ")
                print("="*65)
                print("- Adam Jose Miguel Navas Garcia")
                print("- 201213547")
                print("- Introduccion a la programacion y computacion 2 - Seccion A")
                print("- Ingenieria en Ciencias y Sistemas")
                print("- 4to Semestre")
                print("="*65)
                time.sleep(8)
                limpiar_consola()
                menu_Principal()
            elif seleccion == 6:
                limpiar_consola()
                exit()
            else:
                print("debe ingresar una opcion valida")
        except ValueError:
            print("debe ingresar una opcion valida")

#Submenu de compra
def submenu():
    subtitulo = f"Menu Compra"
    subtitulo = subtitulo.center(37)
    print("="*39)
    print(subtitulo)
    print("="*39)
    print("1) Agregar Producto")
    print("2) Terminar Compra y Facturar")
    print("="*39)
    print()
    while True:
        try:
            seleccion2 = int(input("Ingrese un valor: "))
            if seleccion2 == 1:
                limpiar_consola()
                registrar_Producto()
            elif seleccion2 == 2:
                limpiar_consola()
                menu_Principal()    
        except ValueError:
            print("debe ingresar una opcion valida")               

#Agregar Productos
def registrar_Producto():
    subtitulo2 = "Registrar Producto"
    subtitulo2 = subtitulo2.center(37)
    print("="*39)
    print(subtitulo2)
    print("="*39)
    print()
    while True:
        try:
            codigo = str(input("Ingrese codigo de Producto: "))
            nombre = str(input("Ingrese nombre de producto: "))
            descripcion = str(input("Ingrese descripcion del producto: "))
            precio = str(input("Ingrese precio del producto: "))
            nuevo_producto = informacion.producto(codigo,nombre,descripcion,precio)
            lista_producto.append(nuevo_producto)
            print()
        except ValueError:
            print("debe ingresar una opcion valida")

        while True:
            try:
                elegir = str(input("¿Desea ingresar otro producto? S/N"))
                if elegir == "s" or "S":
                    limpiar_consola()
                    registrar_Producto()
                elif elegir == "n" or "N":
                    limpiar_consola()
                    menu_Principal()
            except ValueError:
                print("debe ingresar una opcion valida")

#Agregar Cliente
def registrar_Cliente():
    subtitulo3 = "Registrar Cliente"
    subtitulo3 = subtitulo3.center(37)
    print("="*39)
    print(subtitulo3)
    print("="*39)
    print()
    while True:
        try:
            nombre = str(input("Ingrese nombre del cliente: "))
            correo = str(input("Ingrese correo electronico del cliente: "))
            nit = str(input("Ingrese NIT del cliente: "))
            nuevo_cliente = informacion.cliente(nombre,correo,nit)
            lista_cliente.append(nuevo_cliente)
            print()
        except ValueError:
            print("debe ingresar una opcion valida")

        while True:
            try:
                elegir = str(input("¿Desea Registrar otro cliente? S/N"))
                if elegir == "s" or "S":
                    limpiar_consola()
                    registrar_Cliente()
                elif elegir == "n" or "N":
                    limpiar_consola()
                    menu_Principal()
            except ValueError:
                print("debe ingresar una opcion valida")

#Reporte Compra
def reporte():
    pass

#Limpiar consola(Linux / Windows)
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear') #Limpiar consola de sistema (Windows o Linux)

#Creacion de listas para almacenar la informacion
def ejemplo_lista():
    
    #Ejemplo de datos para agregar para probar funcionalidad
    c1 = informacion.cliente("Adam Navas", "adam_navas@hotmail.com",1234564-8 )
    c2 = informacion.cliente("Tania Chacon", "aTania@gmail.com", 2345671-8)
    c3 = informacion.cliente("Pedro Josue", "pedro-j@yahoo.com", 9876543-2)
    p1 = informacion.producto("PR001", "Salsa de Tomate", "salsa marca naturas", 8.50)
    p2 = informacion.producto("PR002", "Salsa de Jitomate", "salsa marca naturas", 6.50)
    p3 = informacion.producto("PR003", "Jalea de fresa", "Jalea marca anabely", 7.25)
    lista_cliente.append(c1)
    lista_cliente.append(c2)
    lista_cliente.append(c3)
    lista_producto.append(p1)
    lista_producto.append(p2)
    lista_producto.append(p3)
#Main
if __name__ == "__main__":
    lista_producto = []
    lista_cliente = []
    ejemplo_lista
    menu_Principal()