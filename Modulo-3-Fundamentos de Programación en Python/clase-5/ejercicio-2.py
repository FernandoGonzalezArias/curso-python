# 2. utilizando dos while anidados, construya la tablas de mutiplicacion, ejemplo
#     Ejemplo while anidados:
#     while codicion1
#         while codicion2
#             .....


inicio = 1
fin = 10

i = inicio
while i <= fin:
    j = inicio
    while j <= fin:
        print(i, "x", j, "=", i*j)
        j += 1
    i += 1
