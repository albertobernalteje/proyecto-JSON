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
