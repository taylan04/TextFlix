
def catalogo(filmes):
    catalogo = []
    filmes_separados = filmes.split("#")
    contador = 0
    
    for filme in filmes_separados:
        titulo, ano, categorias, descricao = filme.split("|")
        lista_categorias = filtrar_categorias(categorias)
        contador += 1
        info = {"ID": contador,
                "Título": titulo.capitalize(),
                "Ano": int(ano),
                "Gêneros": lista_categorias,
                "Descrição": descricao.capitalize(),
                "Visto": False
                }
        catalogo.append(info)
    return catalogo

def filtrar_categorias(cat):
    lista_categorias = cat.replace(";", ",").split(",")
    lista_categorias = [categoria.strip().lower() for categoria in lista_categorias]
    nova_lista = []
    for c in lista_categorias:
        if c not in nova_lista:
            nova_lista.append(c)
    lista_categorias = nova_lista
    return lista_categorias

def solicitar_string_not_null(msg):
    while True:
        string = input(msg)
        if string.strip() == "":
            print("\nParece que você não digitou nada. Tente novamente!\n")
        else:
            return string

# Fiz essa porque caso o input seja vazio, vai pelo valor padrão quando necessário
def solicitar_string(msg):
    return input(msg)

def solicitar_numero(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("número inválido!")


