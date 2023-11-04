valores = {
    "titulo": "Branca de Neve",
    "genero": "Ação",
    "duracao": '3:20',
    "diretor": "Waldisney",
    "estudio": "Disney",
    "classificacao": "15",
    "ano": 2006
}

print (', '.join(valores.keys()))
print (', '.join(['?'] * len(valores)))