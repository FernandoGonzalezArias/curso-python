# 6. Se le asignado una tarea para programar un algoritmo para una lavadora, debe investigar cuanta agua se neceita para lavar prendas
#     con las siguientes caracteriticas, algodon, nilon, poliester, debe investigar para una lavadora de xx kg cuantas prendas de cada una puede 
#     lavar entendiendo, que solo se puede lavar ropa de un mismo tipo y asi poder calcular lo siguiente

#     Por ejemplo, si la carga es 10, la cantidad de agua que requiere es 5 y la cantidad de ropa a lavar es 14, entonces necesitas 5 * 1.1 ^ (14 - 10) cantidad de agua.

#     Escribe una función para calcular cuánta agua se necesita si tienes una cantidad de ropa.
#     La función aceptará 2 argumentos: - carga lavadora y ropa.

def cantidad_de_agua(carga_lavadora, cantidad_ropa):
    # Verificamos el tipo de tela
    tipo_tela = input("Ingrese el tipo de tela (algodon, nylon o poliester): ")
    if tipo_tela not in ["algodon", "nylon", "poliester"]:
        return "Error: tipo de tela no válido"

    # Definimos la cantidad de agua necesaria por kilogramo de ropa para cada tipo de tela
    agua_por_kg = {"algodon": 5, "nylon": 4, "poliester": 3}

cantidad_de_agua( )