from util import * 

def entrar_opcao():
    print("\n")
    print("---- Menu ----")
    print("[1] - Cadastrar Filme")
    print("[2] - Remover Filme")
    print("[3] - Listar Filmes")
    print("[4] - Buscar no título")
    print("[5] - Buscar por substring")
    print("[6] - Filtrar por gênero")
    print("[7] - Marcar como visto")
    print("[8] - Listar não vistos")
    print("[9] - Abreviar sinopse dos filmes")
    print("[10] - Palavras mais frequentes do catálogo")
    print("[11] - Ranking de relevância")
    print("[0] - Sair")
    opcao = solicitar_numero("Entre com uma opção: ")
    return opcao