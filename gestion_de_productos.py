productos = []

def agregar_producto():
    while True:
        try:
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad disponible del producto: "))
            producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
            productos.append(producto)
            print("Producto agregado con éxito!")
            break
        except ValueError:
            print("Error: El precio o la cantidad deben ser números válidos.")

def ver_productos(moneda="PYG", unidad="kilogramos" "unidades""litros"):
    print("Lista de productos:")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto['nombre']}: ${producto['precio']:.2f} - {producto['cantidad']} unidades")

def actualizar_producto():
    while True:
        try:
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            for producto in productos:
                if producto["nombre"] == nombre:
                    print("1. Actualizar nombre")
                    print("2. Actualizar precio")
                    print("3. Actualizar cantidad")
                    opcion = int(input("Ingrese la opción: "))
                    if opcion == 1:
                        producto["nombre"] = input("Ingrese el nuevo nombre: ")
                    elif opcion == 2:
                        producto["precio"] = float(input("Ingrese el nuevo precio: "))
                    elif opcion == 3:
                        producto["cantidad"] = int(input("Ingrese la nueva cantidad: "))
                    print("Producto actualizado con éxito!")
                    return
            print("Producto no encontrado")
            break
        except ValueError:
            print("Error: El precio o la cantidad deben ser números válidos.")


def eliminar_producto():
    while True:
        try:
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            for producto in productos:
                if producto["nombre"] == nombre:
                    productos.remove(producto)
                    print("Producto eliminado con éxito!")
                    return
            print("Producto no encontrado")
            break
        except ValueError:
            print("Error: El nombre del producto debe ser una cadena válida.")


def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']}, {producto['precio']:.2f}, {producto['cantidad']}\n")
    print("Datos guardados con éxito!")


def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo.readlines():
                nombre, precio, cantidad = linea.strip().split(", ")
                productos.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cantidad)})
    except FileNotFoundError:
        pass


cargar_datos()

# Menú principal
while True:
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Guardar datos")
    print("6. Salir")
    opcion = input("Ingrese la opción: ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        ver_productos()
    elif opcion == "3":
        actualizar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        guardar_datos()
    elif opcion == "6":
        break
    else:
        print("Opción inválida")