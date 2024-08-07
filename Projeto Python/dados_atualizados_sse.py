import pandas as pd
import minhas_funcoes as mf


def sse():
    # Importa a base de dados
    dados_sse = importar_dados('Selecione o arquivo extraído pela finanças estudantis.')

    # Seleciona apenas as colunas desejadas
    dados_sse = dados_sse[
        ['NOME_ALUNO', 'TELEFONE_RESPONSAVEL', 'NOME DO PAI', 'E-MAIL DO PAI', 'TELEFONE_PAI', 'NOME DA MÃE',
         'E-MAIL DA MÃE', 'TELEFONE_MÃE']]

    # Altera os valores NAN para str('vazia').
    dados_sse = dados_sse.fillna('vazio')

    # Cria um dicionário com nome, email e telefone do usuário
    usuarios_sse = criar_usuario(dados_sse)
    return usuarios_sse


def importar_dados(texto):
    return pd.read_excel(mf.selecionar_arquivo_computador(texto))


def criar_usuario(dados):
    usuarios = {}
    for i in dados.index:
        # Pai
        nome_pai, email_pai, fone_pai = str(dados['NOME DO PAI'][i]), str(dados['E-MAIL DO PAI'][i]), str(
            dados['TELEFONE_PAI'][i])
        nome, email, fone = _formatar_usuario(nome_pai, email_pai, fone_pai)
        usuarios[nome] = [email, fone]

        # Mãe
        nome_mae, email_mae, fone_mae = str(dados['NOME DA MÃE'][i]), str(dados['E-MAIL DA MÃE'][i]), str(
            dados['TELEFONE_MÃE'][i])
        nome, email, fone = _formatar_usuario(nome_mae, email_mae, fone_mae)
        usuarios[nome] = [email, fone]

        # Aluno
        nome_aluno, email_aluno, fone_aluno = str(dados['NOME_ALUNO'][i]), '', str(dados['TELEFONE_RESPONSAVEL'][i])
        nome, email, fone = _formatar_usuario(nome_aluno, email_aluno, fone_aluno)
        usuarios[nome] = [email, fone]
    return usuarios


def _formatar_usuario(nome, email, fone):
    nome = mf.formatar_nome(nome)
    email = mf.formatar_email(email)
    fone = mf.formatar_fone(fone)

    if nome != 'vazio' and email != 'vazio':
        return nome, email, fone
    else:
        return '', '', ''
