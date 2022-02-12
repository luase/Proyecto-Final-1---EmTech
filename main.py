from lifestore_file import lifestore_sales, lifestore_products

"""
Calculo de promedio de rese;as por producto.


Para calcular la rese;a promedio de solamente 1 producto es
necesario:
    -identificar todas las rese;as que pertenecen a ese producto.
        -para esto encontramos en la lista de lifestore_sales la
        sublista de ventas que coincidan su id_product contra el
        id_product del producto que queremos analizar.
    -Una vez tenemos esta lista podemos encontrar su longitud.
    -Iteramos venta por venta y sumamos cada rese;a.
    -Obtenemos el promedio dividiendo la suma total por la longitud
    de la lista.

Que hacemos luego con este resultado?
Si pensamos en hacerlo de nuevo para cada producto de la lista de
ventas, lo mejor seria guardarlo junto al id_product del producto
como una lista.
Para guardarlo como una lista:
    producto_resena = [id_product, promedio]

Despues lo guardariamos en una lista con el resto de pares de
'id-promedio':
    lista_promedios.append(producto_resena)
"""

"""

    * Ejemplo similar, promedio de ventas por mes de los primeros
      15 productos

"""

"""
La info de lifestore_file:

lifestore_products = [id_product, name, price, category, stock]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
"""

names = [row[1][:10] for row in lifestore_products]

for name in names:
    print(name)
