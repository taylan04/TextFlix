
def catalogo(filmes):
    """
    converte uma string com filmes separados por '#' em uma lista de dicionários.

    args:
        filmes (str): string contendo filmes no formato "titulo|ano|categorias|descricao" separados por "#".

    returns:
        catalogo (list): lista de dicionários, cada um representando um filme com campos id, título, ano, gêneros, descrição e visto.
    """
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
    """
    transforma uma string de categorias em uma lista única de categorias limpas.

    args:
        cat (str): string de categorias separadas por vírgula ou ponto e vírgula.

    returns:
        lista_categorias (list): lista de categorias em letras minúsculas, sem duplicatas.
    """
    lista_categorias = cat.replace(";", ",").split(",")
    lista_categorias = [categoria.strip().lower() for categoria in lista_categorias]
    nova_lista = []
    for c in lista_categorias:
        if c not in nova_lista:
            nova_lista.append(c)
    lista_categorias = nova_lista
    return lista_categorias

def solicitar_string_not_null(msg):
    """
    solicita uma entrada do usuário, garantindo que não seja vazia.

    args:
        msg (str): mensagem a ser exibida para o usuário.

    returns:
       string (str): string digitada pelo usuário, não vazia.
    """
    while True:
        string = input(msg)
        if string.strip() == "":
            print("\nParece que você não digitou nada. Tente novamente!\n")
        else:
            return string

# Fiz essa porque caso o input seja vazio, vai pelo valor padrão quando necessário
def solicitar_string(msg):
    """
    solicita uma entrada de string do usuário, permitindo que seja vazia.

    args:
        msg (str): mensagem a ser exibida para o usuário.

    returns:
        str: string digitada pelo usuário.
    """
    return input(msg)

def solicitar_numero(msg):
    """
    solicita um número inteiro do usuário, repetindo a solicitação se o valor for inválido.

    args:
        msg (str): mensagem a ser exibida para o usuário.

    returns:
        int: número inteiro digitado pelo usuário.
    """
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("número inválido!")


