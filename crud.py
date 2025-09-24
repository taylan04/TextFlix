from util import *

def cadastrar_filme(filmes):
    """
    cadastra um novo filme na lista de filmes.

    args:
        filmes (list): lista de dicionários contendo os filmes cadastrados.

    returns:
        None
    """
    print("\n====Cadastrando Filme====\n")
    titulo = solicitar_string_not_null("Título: ")
    ano = solicitar_numero("Ano de lançamento: ")
    categorias = solicitar_string_not_null("Categorias (separadas por vírgula): ")
    categorias_filtradas = filtrar_categorias(categorias)
    descricao = solicitar_string_not_null("Descrição (Max: 300 caracteres): ")
    while len(descricao) > 300:
        print("\nMáximo de caracteres excedido.")
        descricao = solicitar_string_not_null("Descrição (Max: 300 caracteres): ")
    novo_filme = {"ID": filmes[-1]["ID"] + 1 if filmes else 1,
                  "Título": titulo.capitalize(), 
                  "Ano": ano, 
                  "Gêneros": categorias_filtradas, 
                  "Descrição": descricao, 
                  "Visto": False}
    print("\nFilme cadastrado com sucesso!")
    filmes.append(novo_filme)

def excluir_filme(filmes):
    """
    remove um filme da lista pelo título.

    args:
        filmes (list): lista de dicionários contendo os filmes cadastrados.

    returns:
        None
    """
    titulo = solicitar_string_not_null("\nDigite o título: ")
    for filme in filmes:
        if filme["Título"].lower() == titulo.lower():
            filmes.remove(filme)
            print("\nFilme removido com sucesso!")

def listar_filmes(filmes, ordem):
    """
    lista os filmes ordenados por id, título ou ano.

    args:
        filmes (list): lista de dicionários contendo os filmes cadastrados.
        ordem (str): critério de ordenação ("id", "titulo" ou "ano").

    returns:
        None
    """
    if ordem.lower() == "id":
        filmes_por_id = sorted(filmes, key = lambda f: f["ID"])
        for filme in filmes_por_id:
            print(f"\n{filme}\n")
    elif ordem.lower() == "titulo":
        filmes_por_titulo = sorted(filmes, key = lambda f: f["Título"])
        for filme in filmes_por_titulo:
            print(f"\n{filme}\n")
    elif ordem.lower() == "ano":
        filmes_por_ano = sorted(filmes, key = lambda f: f["Ano"], reverse=True)
        for filme in filmes_por_ano:
            print(f"\n{filme}\n")
    else:
        print("\nOpção inválida!")

def buscar_por_palavras(filmes):
    """
    busca filmes pelo título usando palavras separadas por vírgula e lógica AND ou OR.

    args:
        filmes (list): lista de dicionários contendo os filmes cadastrados.

    returns:
        None
    """
    palavras = solicitar_string_not_null("\nDigite as palavras separadas por vírgula: ")
    tipo = solicitar_string_not_null("\nAND (todas as palavras devem aparecer) ou OR (qualquer palavra encontrada já conta)?: ")
    filmes_encontrados = []
    palavras_separadas = [p.strip().lower() for p in palavras.split(",")]
    
    for filme in filmes:
        titulo_lower = filme["Título"].lower()

        if tipo.lower() == "and":
            if all(palavra in titulo_lower for palavra in palavras_separadas):
                filmes_encontrados.append(filme)
        elif tipo.lower() == "or":
            if any(palavra in titulo_lower for palavra in palavras_separadas):
                filmes_encontrados.append(filme)
    
    if filmes_encontrados:
        print("\n===Filmes encontrados===\n")
        for filme in filmes_encontrados:
            print(filme)
    else:
        print("\nNenhum filme encontrado!")

def marcar_visto(filmes):
    """
    marca um filme como assistido.

    args:
        filmes (list): lista de dicionários contendo os filmes cadastrados.

    returns:
        None
    """
    titulo = solicitar_string_not_null("\nTítulo: ")
    for filme in filmes:
        if filme["Título"].lower() == titulo.lower():
            filme["Visto"] = True
            print("\nFilme marcado como assistido!")

def listar_nao_vistos(filmes):
    """
    lista os filmes que ainda não foram assistidos.

    args:
        filmes (list): lista de dicionários contendo os filmes cadastrados.

    returns:
        None
    """
    filmes_nao_vistos = [filme for filme in filmes if filme["Visto"] == False]
    filmes_vistos = [filme for filme in filmes if filme["Visto"] == True]
    
    print("\n=== Filmes não vistos ===")
    
    if filmes_nao_vistos:
        for filme in filmes_nao_vistos:
            print(f"\n{filme}")
    else:
        print("\nNenhum filme encontrado!")

    print("\n=== Filmes vistos ===")

    if filmes_vistos:
        for filme in filmes_vistos:
            print(f"\n{filme}")
    else:
        print("\nNenhum filme encontrado!")

def buscar_por_substring(filmes):
    """
    busca filmes cujo título contenha uma substring.

    args:
        filmes (list): lista de dicionários contendo os filmes cadastrados.

    returns:
        None
    """
    substring = solicitar_string_not_null("\nDigite uma substring para a busca: ")
    filmes_filtrados = [filme for filme in filmes if substring.lower() in filme["Título"].lower()]
    filmes_ordenados_ano = sorted(filmes_filtrados, key = lambda f: f["Ano"], reverse=True)
    if filmes_ordenados_ano:
        print("\n===Filmes Encontrados===")
        for filme in filmes_ordenados_ano:
            print(f"\n{filme}")
    else:
        print("\nNenhum filme encontrado!")

def filtrar_por_genero(filmes):
    """
    filtra filmes por gênero e lista ordenados por título.

    args:
        filmes (list): lista de dicionários contendo os filmes cadastrados.

    returns:
        None
    """
    genero = solicitar_string_not_null("\nPor qual gênero deseja realizar a busca? ")
    filmes_encontrados = [filme for filme in filmes if genero.lower() in filme["Gêneros"]]
    filmes_ordenados = sorted(filmes_encontrados, key = lambda f: f["Título"])
    if filmes_ordenados:
        print("\n===Filmes Encontrados===")
        for filme in filmes_ordenados:
            print(f"\n{filme}")

def abreviar_sinopse(filmes):
    """
    gera uma versão abreviada da sinopse dos filmes, encurtando palavras maiores que 6 caracteres.

    args:
        filmes (list): lista de dicionários contendo os filmes cadastrados.

    returns:
        None
    """
    sinopses_abreviadas = []
    vogais = "aeiouAEIOU"
    for filme in filmes:
        novo_filme = filme.copy() #precisei do copy pra nao alterar a sinopse original
        descricao = novo_filme["Descrição"]

        if len(descricao) <= 50:
            sinopses_abreviadas.append(novo_filme)
        else:
            palavras = descricao.strip().split(" ")
            lista_auxiliar = []
            for palavra in palavras:
                if len(palavra) > 6:
                    abreviada = palavra[:6]
                    while abreviada[-1] in vogais:
                        abreviada = abreviada[:-1]
                    abreviada += "."
                    lista_auxiliar.append(abreviada)
                else:
                    lista_auxiliar.append(palavra)

            novo_filme["Descrição"] = " ".join(lista_auxiliar)
            sinopses_abreviadas.append(novo_filme)

    for filme in sinopses_abreviadas:
        print(f"\n{filme}")

def top_palavras(filmes):
    """
    lista as k palavras mais frequentes nos títulos e descrições dos filmes (mínimo 5 caracteres).

    args:
        filmes (list): lista de dicionários contendo os filmes cadastrados.

    returns:
        None
    """
    k = solicitar_numero("\nDigite a quantidade de palavras frequentes que deseja ver: ")
    top_palavras = {}
    for filme in filmes:
        palavras = filme["Título"].strip().split() + filme["Descrição"].strip().split()
        for palavra in palavras:
            if len(palavra) >= 5:
                palavra2 = palavra.lower()
                if palavra2 not in top_palavras:
                    top_palavras[palavra2] = 1
                else:
                    top_palavras[palavra2] += 1

    palavras_ordenadas = sorted(top_palavras, key=lambda x: x[1], reverse=True)
    palavras_k = palavras_ordenadas[:k]
    print(palavras_k)

def ranking(filmes, palavras_chave, k):
    """
    gera um ranking de filmes baseado na frequência das palavras-chave na descrição.

    args:
        filmes (list): lista de dicionários contendo os filmes cadastrados.
        palavras_chave (str): palavras separadas por vírgula para calcular o ranking.
        k (int): quantidade de filmes a serem listados no ranking.

    returns:
        None
    """
    filmes_score = []
    palavras = [palavra.strip().lower() for palavra in palavras_chave.split(",") if len(palavra.strip()) >= 5]
    for filme in filmes:
        score = 0
        for palavra in palavras:
            score += filme["Descrição"].lower().count(palavra)
        filmes_score.append([filme, score])
    
    filmes_score_ordenado = sorted(filmes_score, key = lambda f:f[1], reverse=True)
    for filme in filmes_score_ordenado[:k]:
        print(f"\n{filme[0]} | SCORE: {filme[1]}")
        
        

        


