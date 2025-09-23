from crud import *
from util import *
from menu import *
from filmes import string_filmes

filmes = catalogo(string_filmes)
opcao = entrar_opcao()
while (opcao != 0):
    match opcao:
        case 1: cadastrar_filme(filmes)
        case 2: excluir_filme(filmes)
        case 3: 
            ordem = solicitar_string("\nOrdenar por id (padrão), por titulo ou por ano? ")
            if ordem == "":
                ordem = "id"
            listar_filmes(filmes, ordem)
        case 4: 
            buscar_por_palavras(filmes)
        case 5: 
            buscar_por_substring(filmes)
        case 6:
            filtrar_por_genero(filmes)
        case 7:
            marcar_visto(filmes)
        case 8:
            listar_nao_vistos(filmes)
        case 9:
            abreviar_sinopse(filmes)
        case 10:
            top_palavras(filmes)
        case 11:
            #coloquei os inputs aqui porque no AT pede para a função recebê-los.
            palavras = solicitar_string_not_null("\nDigite as palavras separadas por vírgula para a organização do ranking: ")
            numero = solicitar_numero("\nDigite quantos filmes do ranking que ver: ")
            ranking(filmes,palavras,numero)
        case _: print("\nErro: opção inválida")
    opcao = entrar_opcao()

