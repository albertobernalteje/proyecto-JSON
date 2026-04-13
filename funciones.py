import json

def cargar_datos():
    try:
        f = open("productos.json", encoding="utf-8")
        datos = json.load(f)
        f.close()
        return datos
    except:
        return None

def listar_productos(datos):
    # Cogemos la lista de productos
    lista = datos["productos"]
    
    # Ordenamos la lista usando una burbuja simple o el método sort básico
    lista.sort(key=lambda p: p["precio"], reverse=True)
    
    print("\nLISTADO DE PRODUCTOS (MÁS CAROS PRIMERO):")
    for p in lista:
        print("Nombre:", p["nombre"], "-", "Precio:", p["precio"], "€")

def mostrar_estadisticas(datos):
    lista = datos["productos"]
    categorias = []
    
    # Primero sacamos qué categorías existen sin repetir
    for p in lista:
        if p["categoria"] not in categorias:
            categorias.append(p["categoria"])
    
    print("\nESTADÍSTICAS POR CATEGORÍA:")
    # Para cada categoría, contamos y sumamos puntos
    for cat in categorias:
        contador = 0
        suma_puntos = 0
        for p in lista:
            if p["categoria"] == cat:
                contador = contador + 1
                suma_puntos = suma_puntos + p["puntuacion"]
        
        media = suma_puntos / contador
        print("Categoría:", cat, "| Unidades:", contador, "| Media:", media)

def buscar_producto(datos):
    print("\n--- BUSCADOR ---")
    cat_buscada = input("¿Qué categoría buscas?: ")
    precio_limite = float(input("¿Precio máximo?: "))
    
    lista = datos["productos"]
    encontrado = False
    
    for p in lista:
        # Comprobamos si coincide la categoría y el precio
        if p["categoria"].lower() == cat_buscada.lower():
            if p["precio"] <= precio_limite:
                encontrado = True
                print("Producto:", p["nombre"])
                print("Precio:", p["precio"], "€")
                print("Proveedor:", p["proveedor"])
                if p["en_oferta"] == True:
                    print("¡Está en oferta!")
                print("-------------------")
                
    if encontrado == False:
        print("No hemos encontrado nada con esos filtros.")

def buscar_por_ancho(datos):
    ancho_max = float(input("\n¿Ancho máximo en cm?: "))
    
    lista = datos["productos"]
    encontrado = False
    
    # Recorremos los productos y comprobamos el ancho dentro de dimensiones
    print("\nProductos que caben en", ancho_max, "cm de ancho:")
    for p in lista:
        if p["dimensiones"]["ancho_cm"] <= ancho_max:
            encontrado = True
            print("Nombre:", p["nombre"])
            print("Categoría:", p["categoria"])
            print("Stock:", p["stock"])
            print("-------------------")
    
    if encontrado == False:
        print("No hay productos que quepan en ese espacio.")

def estadisticas_globales(datos):
    lista = datos["productos"]
    
    # Empezamos con el primer producto como referencia
    mas_caro = lista[0]
    mas_barato = lista[0]
    mas_stock = lista[0]
    suma_precios = 0
    suma_puntos = 0
    en_oferta = 0
    sin_oferta = 0
    
    # Recorremos todos los productos para sacar los valores
    for p in lista:
        if p["precio"] > mas_caro["precio"]:
            mas_caro = p
        if p["precio"] < mas_barato["precio"]:
            mas_barato = p
        if p["stock"] > mas_stock["stock"]:
            mas_stock = p
        suma_precios = suma_precios + p["precio"]
        suma_puntos = suma_puntos + p["puntuacion"]
        if p["en_oferta"] == True:
            en_oferta = en_oferta + 1
        else:
            sin_oferta = sin_oferta + 1
    
    media_precio = suma_precios / len(lista)
    media_puntos = suma_puntos / len(lista)
    
    print("\nESTADÍSTICAS GLOBALES:")
    print("Producto más caro:", mas_caro["nombre"], "-", mas_caro["precio"], "€")
    print("Producto más barato:", mas_barato["nombre"], "-", mas_barato["precio"], "€")
    print("Media de precios:", round(media_precio, 2), "€")
    print("Producto con más stock:", mas_stock["nombre"], "-", mas_stock["stock"], "uds.")
    print("En oferta:", en_oferta, "| Sin oferta:", sin_oferta)
    print("Media de puntuación:", round(media_puntos, 2))
    
    # Mostramos el listado completo con la información relevante
    print("\nLISTADO DE PRODUCTOS:")
    for p in lista:
        print("Nombre:", p["nombre"], "| Precio:", p["precio"], "€ | Puntuación:", p["puntuacion"], "| Stock:", p["stock"], "| Oferta:", p["en_oferta"])


