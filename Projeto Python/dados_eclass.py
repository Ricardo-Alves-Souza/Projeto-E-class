import pandas as pd
import minhas_funcoes as mf


def eclass():
    # Importa a base de dados
    dados_eclass = importar_dados('Selecione o extraído do e-class.')

    # Seleciona apenas as colunas desejadas
    dados_eclass = dados_eclass[['Nome', 'Conta Gsuite', 'Email']]

    # Altera os campos NAN para str('vazio')
    dados_eclass = dados_eclass.fillna('vazio')

    usuarios_eclass = criar_usuario(dados_eclass)

    return usuarios_eclass


def importar_dados(texto):
    return pd.read_excel(mf.selecionar_arquivo_computador(texto))


def criar_usuario(dados):
    usuarios = {}
    for i in dados.index:
        nome = mf.formatar_nome(dados['Nome'][i])
        email = mf.formatar_email(dados['Email'][i])
        if dados['Conta Gsuite'][i] == 'vazio':
            username = mf.criar_username(dados['Conta Gsuite'][i], nome)
        else:
            username = ''
        usuarios[nome] = [username, email]
    return usuarios
