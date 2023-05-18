requisitos = {
    "titulo": "requerido",
    "notas": "requerido",
    "foto": "opcional"
}


print (requisitos)

#acceder a una propiedad
print(f'Las notas son de tipo: {requisitos["notas"]}')
print(f'la foto es de tipo: {requisitos["foto"]}')

# modificar una propiedad
requisitos["foto"] = "requerido"
print(f'la foto es de tipo: {requisitos["foto"]}')
requisitos["notas"] = "opcional"
print(f'Las notas son de tipo: {requisitos["notas"]}')


## Practica -> Construir un diccionario de datos para guardar
##             la informacion de un avion, coloque al menos 6 propiedades
##             imprima tres de ellas y cambie el valor de dos
##             al menos debe existior una propiedad booleana, una entera , un flotante
##             un arreglo, un diccionario y un string

avion = {
    "piloto": {
        "nombre": "Carlos",
        "apellido": "Azócar"
    },
    "cantidad_motores": 2,
    "operativo": True,
    "encendido": False,
    "activo": False,
    "do_escala": True,
    "is_flying": True,
    "is_own": True,
    "seats": ['economic', 'turist', 'executive'],
    "capacidad_cargo": 1.7,
    "cantidad_pasajeros": 400,
    "modelo": "Boeing 747 MAX"
}

## Costruya un programa que le solicite el peso en kg de una persona
## y si el peso esta entre 60 - 70 recomiende una dieta de 5 comidas alta en carbohidratos
## si el peso esta entre 70 y 80  recomiende una dieta de 4 comidas alta en proteinas
## si el peso es mayor a 80 recomiende una dieta de 3 comidas alta en fibras
## utilice solo dicionarios para agrupar los respectivos menues.
# Dieta recomendada en función del rango de peso
dietas = {
    'flaco': {
        'numero_comidas': 5,
        'tipo_dieta': 'alta en carbohidratos',
        'menu': [
            'Desayuno: Pan con mermelada y juguito de naranja',
            'colación: Barra de proteina',
            'Almuerzo: Pasta con salsa de tomate',
            'once: avena y granola',
            'Cena: Arroz con vegetales'
        ]
    },
    'medio': {
        'numero_comidas': 4,
        'tipo_dieta': 'alta en proteínas',
        'menu': [
            'desayuo: Huevos revueltos con tostadas',
            'almuerzo: Pechuga de pollo con ensalada',
            'once:  jugo con proteinas',
            'Cena: pollo a la parrilla con brócoli'
        ]
    },
    'obeso': {
        'numero_comidas': 3,
        'tipo_dieta': 'alta en fibra',
        'menu': [
            'Desayuno: Avena con frutas y nueces',
            'Almuerzo: Quinoa con vegetales',
            'once: Ensalada de  porotos negros '
        ]
    }
}

# Solicitar el peso de la persona
peso = float(input("Ingrese su peso en kg: "))

# condicional para decidir

#dieta_recomendada pasa a ser una propiedad del diccionario 

if peso >= 60 and peso <= 70:
    dieta_recomendada = 'flaco'
elif peso >= 71 and peso <= 80:
    dieta_recomendada = 'medio'
elif peso > 80:
    dieta_recomendada = 'obeso'
else:
    dieta_recomendada = None

# Imprimir la dieta recomendada
if dieta_recomendada:
    print("Su nutricionista le recomienda una dieta de", dietas[dieta_recomendada]['numero_comidas'], "comidas",dietas[dieta_recomendada]['tipo_dieta'])
    print("El menú es:")
    for comida in dietas[dieta_recomendada]['menu']:
        print(comida)
else:
    print("coloque un peso real ")