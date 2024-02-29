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
                registrar_Producto()
                #limpiar_consola()
                #menu_Principal()
            elif seleccion == 2:
                limpiar_consola()
                registrar_Cliente()
            elif seleccion == 3:
                limpiar_consola()
                menu_Compra()
                time.sleep(3)
                menu_Principal()
            elif seleccion == 4:
                limpiar_consola()
                reporte()
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
def menu_Compra():
    verificacion = str(input("Ingrese numero de NIT: "))
    datos_cliente = None
    encontro = False
    for cliente in lista_cliente:
        if verificacion == cliente.nit:
            datos_cliente = cliente
            encontro = True #Bandera de verificacion
            break
    if encontro == True:
        limpiar_consola()
        print(f'Bienvenid@ {datos_cliente.nombre_cliente}       Correo: {datos_cliente.correo}      NIT: {datos_cliente.nit}')
        time.sleep(2)
        print()    
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
                    compras(datos_cliente)
                elif seleccion2 == 2:
                    limpiar_consola()
                    menu_Principal()    
            except ValueError:
                print("debe ingresar una opcion valida")
    else:
        print("No se encontro el NIT Buscado")
        time.sleep(3)
        limpiar_consola()
        menu_Compra()               

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
            precio = float(input("Ingrese precio del producto: "))
            nuevo_producto = informacion.producto(codigo,nombre,descripcion,precio)
            lista_producto.append(nuevo_producto)
            print()
        except ValueError:
            print("debe ingresar una opcion valida")

        while True:
            try:
                elegir = str(input("¿Desea ingresar otro producto? S/N: "))
                if elegir == "S":
                    limpiar_consola()
                    registrar_Producto()
                elif elegir == "N":
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
                elegir = str(input("¿Desea Registrar otro cliente? S/N: "))
                if elegir == "S":
                    limpiar_consola()
                    registrar_Cliente()
                elif elegir == "N":
                    limpiar_consola()
                    menu_Principal()
            except ValueError:
                print("debe ingresar una opcion valida")

#Compras que realiza el usuario
def compras(datos_cliente):
    global id
    productos_comprados = []
    total_compra = 0
    total_impuesto = 0
    verificar_estado = True
    while verificar_estado == True :
        try:
            realizar_compra = (input("Ingresar codigo de producto: "))
            for producto in lista_producto:
                if realizar_compra == producto.codigo_producto:
                    productos_comprados.append(informacion.producto(producto.codigo_producto, producto.nombre_producto, producto.descripcion, producto.precio_unitario))
                    total_compra += float(producto.precio_unitario)
                    total_compra = round(total_compra,2)
                    total_impuesto += float(producto.precio_unitario * 0.12)
                    total_impuesto = round(total_impuesto,2)
                    break
            else:
                print("No se encontro el producto deseado, intente de nuevo")
                time.sleep(3)
                limpiar_consola()
                continue
        except ValueError:
                print("debe ingresar una opcion valida")
        try:
            elegir = str(input("¿Desea Realizar otra compra? S/N: "))
            if elegir == "S":
                limpiar_consola()
            elif elegir == "N":
                limpiar_consola()
                comprando = informacion.compra(productos_comprados, datos_cliente, id, total_compra, total_impuesto)
                lista_compras.append(comprando)
                id += 1
                verificar_estado = False
                menu_Principal()
        except ValueError:
                print("debe ingresar una opcion valida")

#Reporte Compra
def reporte():
    titulo_reporte = "Reporte de compra "
    titulo_reporte = titulo_reporte.center(37)
    if id == 1:
        limpiar_consola
        print("Debe registrar una compra primero")
        time.sleep(3)
        limpiar_consola()
        menu_Principal()
    else:
        while True:
            id_reporte = int(input("Ingrese id de compra: "))
            for registro in lista_compras:
                if id_reporte == registro.id:
                        print("="*39)
                        print (titulo_reporte + str(id_reporte))
                        print("="*39)
                        print("CLIENTE:")
                        print(f'    Nombre: {registro.cliente.nombre_cliente}')
                        print(f'    Correo: {registro.cliente.correo}')
                        print(f'    Nit: {registro.cliente.nit}')
                        print()
                        print("ARTICULOS COMPRADOS:")
                        for articulos in registro.lista_producto:
                            print(f"- {articulos.codigo_producto}   {articulos.nombre_producto}   {articulos.precio_unitario}")
                        print()
                        print("TOTAL: Q"+ str(registro.total))
                        print("Impuesto: Q"+ str(registro.impuesto))
                        print("-"*39)
                        time.sleep(6)
                        limpiar_consola()
                        menu_Principal()

#Limpiar consola(Linux / Windows)
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

#Creacion de listas para almacenar la informacion
def ejemplo_lista():
    #Ejemplo de datos para agregar para probar funcionalidad
    c1 = informacion.cliente("Adam Navas", "adam_navas@hotmail.com","1234564-8" )
    c2 = informacion.cliente("Tania Chacon", "aTania@gmail.com", "2345671-8")
    c3 = informacion.cliente("Pedro Josue", "pedro-j@yahoo.com", "9876543-2")
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
    id = 1
    lista_producto = []
    lista_cliente = []
    lista_compras = []
    ejemplo_lista()
    menu_Principal()