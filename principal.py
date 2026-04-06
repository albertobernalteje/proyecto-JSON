import funciones

# Cargamos el archivo
datos_tienda = funciones.cargar_datos()

if datos_tienda == None:
    print("Error: No se encuentra el archivo productos.json")
else:
    opcion = ""
    while opcion != "0":
        print("\n--- MI TIENDA ---")
        print("1. Ver todos los productos")
        print("2. Ver estadísticas")
        print("3. Buscar por filtro")
        print("0. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            funciones.listar_productos(datos_tienda)

        elif opcion == "2":
            funciones.mostrar_estadisticas(datos_tienda)

        elif opcion == "3":
            funciones.buscar_producto(datos_tienda)

        elif opcion == "0":
            print("Adiós")