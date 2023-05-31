import random

sustantivos = ["flor", "cielo", "mar", "amor", "suspiro"]
adjetivos = ["hermosa", "serena", "radiante", "eterna", "dulce"]
verbos = ["brilla", "susurra", "acaricia", "envuelve", "enciende"]

def generar_poema():
    verso1 = f"{random.choice(sustantivos)} {random.choice(verbos)}"
    verso2 = f"{random.choice(adjetivos)} {random.choice(sustantivos)}"
    verso3 = f"{random.choice(verbos)} {random.choice(adjetivos)} {random.choice(sustantivos)}"
    
    poema = f"{verso1}\n{verso2}\n{verso3}"
    return poema

poema_generado = generar_poema()
print(poema_generado)
