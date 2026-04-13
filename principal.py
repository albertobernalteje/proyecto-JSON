import funciones

datos_tienda = funciones.cargar_datos()

if datos_tienda is None:
    print("No se puede continuar sin el archivo de datos.")
else:
    opcion = ""
    while opcion != "0":
        print("\n--- MI TIENDA ---")
        print("1. Ver todos los productos")
        print("2. Estadísticas por categoría")
        print("3. Buscar por categoría y precio")
        print("4. Filtrar por ancho máximo")
        print("5. Estadísticas globales")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            funciones.listar_productos(datos_tienda)
        elif opcion == "2":
            funciones.mostrar_estadisticas(datos_tienda)
        elif opcion == "3":
            funciones.buscar_producto(datos_tienda)
        elif opcion == "4":
            funciones.buscar_por_ancho(datos_tienda)
        elif opcion == "5":
            funciones.estadisticas_globales(datos_tienda)
        elif opcion == "0":
            print("Hasta luego.")
        else:
            print("Opción no válida.")

