# Proyecto JSON — Mi Tienda

## Descripción del JSON

Archivo extraído de la API pública DummyJSON: https://dummyjson.com/products, traducido al español y ampliado con dos campos nuevos: en_oferta (boolean) y proveedoR (string).

Contiene un array de 30 productos. Cada producto tiene 4 niveles de profundidad:

Nivel 1: el array productos
Nivel 2: campos simples de cada producto (nombre, precio, categoría…)
Nivel 3: objetos y arrays anidados (dimensiones, reseñas, meta, etiquetas)
Nivel 4: campos dentro de esos objetos (ancho_cm, alto_cm, puntuacion de reseña…)


## Funciones

-- **cargar_datos()** — Abre productos.json y devuelve el diccionario. Captura errores de archivo y de formato JSON.

-- **listar_productos(datos)** — Muestra todos los productos ordenados de mayor a menor precio con nombre, marca, categoría y precio.

-- **mostrar_estadisticas(datos)** — Muestra cuántos productos hay por categoría y la media de puntuación de cada una.

-- **buscar_producto(datos)** — Pide una categoría y un precio máximo por teclado y muestra los productos que cumplen ambos filtros con su proveedor y si están en oferta.

-- **buscar_por_ancho(datos)** — Pide un ancho máximo en cm y filtra los productos que caben en ese espacio, mostrando su categoría y stock.

-- **estadisticas_globales(datos)** — Muestra el producto más caro, el más barato, la media de precios, el de mayor stock, cuántos están en oferta y la media de puntuación. Incluye un listado completo de todos los productos.


## Problemas encontrados

-- Al buscar por categoría, si el usuario escribe la categoría con mayúsculas o minúsculas distintas no hay problema porque se usa .lower(), pero si escribe tildes mal sí falla ya que la comparación es exacta.

-- La primera vez que se ejecutó el programa desde otra carpeta no encontraba el archivo productos.json porque la ruta era relativa. Hay que ejecutarlo siempre desde la misma carpeta donde está el archivo.

-- Al imprimir precios con muchos decimales el resultado quedaba poco limpio, por ejemplo 9.990000000001. Se solucionó usando round() en los cálculos de medias.


## Decisiones tomadas

-- Se usó sorted() en lugar de .sort() para no modificar la lista original del diccionario y evitar efectos no deseados entre funciones.

-- El código se dividió en principal.py (menú y flujo) y funciones.py (toda la lógica).
