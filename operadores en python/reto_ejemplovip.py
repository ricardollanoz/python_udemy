#sistema de descuento vip
#Una tienda de supermercado ofrece un descuento especial a clientes que compren 10 o mas articulos por dia y
#ademas sena miembros de la tienda.
#El sistema debe solicitar al  cliente indique cuantos aritculos
#ha comprado en el dia y preguntarle si cuent con la membresia de la tienda.
#En caso de haber comprado 10 o mas productos y ser miembro de la tienda, entonces tendrá acceso al descuento vip
productos = 10
num_productos = int(input("Ingrese numero de productos: "))
validador_vip = input("Es vip? (si/no) ").strip().lower()
es_elegible = num_productos >= productos and validador_vip == "si"
print(es_elegible)

