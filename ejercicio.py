import random
import textwrap

# Listas de palabras
sujetos = ["El viento", "La luna", "Un viajero", "La memoria", "Mi sombra"]
acciones = ["susurra", "camina", "se esconde", "recuerda", "brilla"]
complementos = ["entre montañas", "sobre el mar", "en mi pecho", "bajo estrellas", "en silencio"]
emociones = ["soledad", "esperanza", "melancolía", "fuego", "infinito"]

# Generar poema
poema = []
for _ in range(4):  # 4 versos
    verso = f"{random.choice(sujetos)} {random.choice(acciones)} {random.choice(complementos)} con {random.choice(emociones)}."
    poema.append(verso)

# Mostrar poema bonito
print("\n✨ Poema generado ✨\n")
for v in poema:
    print(textwrap.fill(v, width=50))

# Decorar con título en ASCII
titulo = "FIN DEL POEMA"
print("\n" + "*" * (len(titulo) + 6))
print(f"** {titulo} **")
print("*" * (len(titulo) + 6))
