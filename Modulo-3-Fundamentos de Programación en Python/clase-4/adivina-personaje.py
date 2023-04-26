#escriba un programa que permita adivinar un personaje
#de marvel en base a estas 3 preguntas
#1 ¿ puede volar?
#2 ¿ es humano?
#3 ¿ tiene mascara?

personajes_marvel = {
    "Iron Man": {"vuela": True, "humano": True, "mascara": False},
    "Spider-Man": {"vuela": False, "humano": True, "mascara": True},
    "Thor": {"vuela": True, "humano": False, "mascara": False},
    "Doctor Strange": {"vuela": True, "humano": True, "mascara": True},
    "Black Panther": {"vuela": False, "humano": True, "mascara": True},
    "Vision": {"vuela": True, "humano": False, "mascara": True},
}

print("Adivina el personaje de Marvel.")
print("Responde las siguientes preguntas con 's' para sí y 'n' para no.")

posibles_personajes = list(personajes_marvel.keys())

# Pregunta 1
respuesta = input("¿Puede volar? ")
if respuesta == "s":
    posibles_personajes = [p for p in posibles_personajes if personajes_marvel[p]["vuela"]]
else:
    posibles_personajes = [p for p in posibles_personajes if not personajes_marvel[p]["vuela"]]

# Pregunta 2
respuesta = input("¿Es humano? ")
if respuesta == "s":
    posibles_personajes = [p for p in posibles_personajes if personajes_marvel[p]["humano"]]
else:
    posibles_personajes = [p for p in posibles_personajes if not personajes_marvel[p]["humano"]]

# Pregunta 3
respuesta = input("¿Tiene máscara? ")
if respuesta == "s":
    posibles_personajes = [p for p in posibles_personajes if personajes_marvel[p]["mascara"]]
else:
    posibles_personajes = [p for p in posibles_personajes if not personajes_marvel[p]["mascara"]]

# Verificación de la respuesta
if len(posibles_personajes) == 0:
    print("No he podido adivinar el personaje.")
elif len(posibles_personajes) == 1:
    print("El personaje es:", posibles_personajes[0])
else:
    print("Los posibles personajes son:", posibles_personajes)