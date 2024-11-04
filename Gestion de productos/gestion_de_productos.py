productos = []

def añadir_producto():
    nombre = input("Nombre del producto: ")
    precio = input("Precio del producto: ")
    cantidad = input("Cantidad del producto: ")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    productos.append(producto)
    print("Producto agregado con éxito!")
    pass

def ver_productos():
    print('lista de productos:')
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto['nombre']} - {producto['precio']} - {producto['cantidad']}")
    pass

def actualizar_producto():
    nombre = input("Nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            nuevo_nombre = input("Nuevo nombre del producto: ")
            nuevo_precio = input("Nuevo precio del producto: ")
            nuevo_cantidad = input("Nueva cantidad del producto: ")
            producto['nombre'] = nuevo_nombre
            producto['precio'] = nuevo_precio
            producto['cantidad'] = nuevo_cantidad
            print("Producto actualizado con exito!")
            break
    else:
        print("El producto no existe en la lista de productos.")
    pass

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print("Producto eliminado con exito!")
            break
    else:
        print("El producto no existe en la lista de productos.")
    pass

def guardar_datos():
    with open('productos.txt', 'w') as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']} - {producto['precio']} - {producto['cantidad']}\n")
    print("Datos guardados con exito!")
    pass

def cargar_datos():
    try:
        with open('productos.txt', 'r') as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split('-')
                producto = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }
                productos.append(producto)
    except FileNotFoundError:
        print("No se encontraron datos en el archivo.")
    pass

def menu():
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")
            productos = []

