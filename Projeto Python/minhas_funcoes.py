from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from dados_atualizados_sse import sse
from dados_eclass import eclass


def selecionar_arquivo_computador(texto):
    janela = Tk()
    arquivo = tkinter.filedialog.askopenfilename(title=texto)
    janela.destroy()
    return arquivo


def formatar_nome(nome):
    # Remove itens específicos da base de dados
    remover = ['Pai', '.', 'Anderson de Oliveira',
               'Marco Aurelio de Almeida', 'Rogéria Fagundes de Melo (falecida)',
               'Julia Graziela dos Santos Silva (falecida)']
    if nome in remover:
        nome = 'vazio'
    return nome.casefold()


def formatar_email(email):
    remover = ['nan', '.@gmail.com', 'rayssamatos525@gmail.com', 'mariliaspirandelli@gmail.com',
               'izildamoreno@outlook.com', 'mariapaixao2008@gmail.com', 'ligia.rodriguess@hotmail.com',
               'carlosluro1@gmail.com', '.', 'vazio', 'ffra.peres@gmail.com']
    if email in remover:
        email = 'vazio'
    return email.casefold()


def formatar_fone(fone):
    fone = fone.replace(' ', '')
    if fone == 'vazio':
        fone = ''
    return fone


def criar_username(username, nome):
    if username == 'vazio':
        nome_split = nome.split()
        remover = ['de', 'da', 'do', 'dos']
        user = []
        for i in nome_split:
            if not i in remover:
                user.append(i)
        username = ''
        if len(user) == 2:
            username = f'{user[-1]}.{user[0]}'
        elif len(user) >= 3:
            username = f'{user[0]}.{user[1]}.{user[-1]}'
    return username
