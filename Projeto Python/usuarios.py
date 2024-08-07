import minhas_funcoes as mf


def criar_usuarios():
    # Importa os dados do SSE e E-class
    dados_sse = mf.sse()
    dados_eclass = mf.eclass()

    # Cria um dicionário com os usuários novos
    lista_usuarios = _verificar_usuarios(dados_sse, dados_eclass)
    criar_txt_usuarios_novos(lista_usuarios)

    return lista_usuarios


def _verificar_usuarios(dados_sse, dados_eclass):
    # Importa o nome das pessoas que o sistema já reenviou o e-mail
    with open(r"arquivos_de_apoio\lixeira.txt", "r") as arquivo:
        nomes_ja_enviados = arquivo.readlines()

    lista_nomes_ja_enviados = []
    for nome in nomes_ja_enviados:
        lista_nomes_ja_enviados.append(nome[:-1])

    dados_usuario = {}
    # Verifica se o usuário da extração do e-class aparece na lista da secretaria
    for usuario, valor in dados_eclass.items():
        username, email_eclass = valor
        if not usuario in lista_nomes_ja_enviados:
            if usuario in dados_sse.keys():
                email_sse = dados_sse[usuario][0]
                fone = dados_sse[usuario][1]
                if len(fone) >= 11:
                    dados_usuario[usuario] = [username, email_sse, fone]

    return dados_usuario


def criar_txt_usuarios_novos(usuarios_novos):
    # Cria um arquivo com os dados dos usuários novos

    # Limpa a lista
    with open(r'arquivos_de_apoio\usuarios_novos.txt', 'w') as arquivos:
        arquivos.write('')

        # Preenche a lista
    for i, usuario in enumerate(usuarios_novos):
        username, email, fone = usuarios_novos[usuario][0], usuarios_novos[usuario][1], usuarios_novos[usuario][2]
        with open(r'arquivos_de_apoio\usuarios_novos.txt', 'a') as arquivos:
            arquivos.write(f'{i:<3} - {usuario:<45} - {email:<35} - {fone:<12} - {username}\n')
