from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui as py
import urllib.parse
import urllib
import clipboard
from usuarios import criar_usuarios
import openpyxl


def esperar(tempo):
    sleep(tempo)


class Automacao:
    py.PAUSE = 0.2

    def __init__(self):
        self.navegador = ''
        self.link_navegador_usuario = ''
        self.numero = ''
        self.nome = ''
        self.login = ''
        self.senha = ''

    def main(self):
        self.abrir_navegador()
        self.abrir_pagina()
        esperar(3)
        try:
            self.apertar_botao('//*[@id="authorize-button"]')
            self.atualizar_dados_usuario()
        except:
            self.atualizar_dados_usuario()

    def atualizar_dados_usuario(self):
        contador = len(usuarios) + 1
        for nome, valor in usuarios.items():
            username, email, fone = valor
            self.numero = fone
            self.nome = nome
            contador -= 1
            print(f'{contador:<3} - {nome:<45} - {email:<30} - {fone:<12} - {username}')
            self.menu_usuario()
            self.pesquisar_usuario(nome)
            if username != '':
                self._preencher_username(username)
            if email != '':
                self._preencher_email(email)
            self._preencher_fone(fone)
            self._salvar_atualizacoes()
            self.gerar_credencial()
            self.coletar_login_senha()
            self.enviar_whatsapp()
            self.abrir_pagina()

    def abrir_navegador(self):
        servico = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        with open(r"arquivos_de_apoio\chrome.txt", "r") as arquivo:
            self.link_navegador_usuario = arquivo.readlines()
        options.add_argument(
            fr'user-data-dir={self.link_navegador_usuario[0]}\Profile Selenium')
        self.navegador = webdriver.Chrome(options=options, service=servico)
        # py.press('f11')

    def abrir_pagina(self):
        self.navegador.get('https://hub-br.eaportal.org/')

    def apertar_botao(self, xpath):
        self.navegador.find_element(By.XPATH, xpath).click()

    def menu_usuario(self):
        while len((self.navegador.find_elements(By.XPATH, '//*[@id="kt_header_menu"]/ul/li[2]/a/span[2]'))) < 1:
            esperar(1)
        self.navegador.find_element(By.XPATH, '//*[@id="kt_header_menu"]/ul/li[2]/a/span[2]').click()
        esperar(1)

    def pesquisar_usuario(self, nome):
        while len(self.navegador.find_elements(By.XPATH,
                                               '//*[@id="kt_content"]/div/div/app-lista/div[2]/div/div/div[6]/div/input')) < 1:
            esperar(1)
        self.navegador.find_element(By.XPATH,
                                    '//*[@id="kt_content"]/div/div/app-lista/div[2]/div/div/div[6]/div/input').send_keys(nome)
        esperar(1)

        self.navegador.find_element(By.XPATH,
                                    '//*[@id="kt_content"]/div/div/app-lista/div[2]/div/div/div[7]/div/button').click()
        esperar(1)

        while len(self.navegador.find_elements(By.XPATH,
                                               '//*[@id="kt_content"]/div/div/app-lista/div[3]/div/div/div/div['
                                               '2]/div/table/tbody/tr/td[2]/a/span')) < 1:
            esperar(1)
        self.navegador.find_element(By.XPATH,
                                    '//*[@id="kt_content"]/div/div/app-lista/div[3]/div/div/div/div['
                                    '2]/div/table/tbody/tr/td[2]/a/span').click()
        esperar(5)

    def _preencher_username(self, username):
        self.navegador.find_element(By.XPATH,
                                    '//*[@id="kt_content"]/div/div/app-cadastro/div[2]/div/div['
                                    '1]/app-dados-pessoais/div[2]/div[2]/form/div[2]/div[2]/div['
                                    '3]/div/div/input').send_keys(
            username)
        esperar(1)

    def _preencher_email(self, email):
        self.navegador.find_element(By.XPATH,
                                    '//*[@id="kt_content"]/div/div/app-cadastro/div[2]/div/div['
                                    '1]/app-dados-pessoais/div[2]/div[2]/form/div[2]/div[3]/div[1]/div/input').clear()

        self.navegador.find_element(By.XPATH,
                                    '//*[@id="kt_content"]/div/div/app-cadastro/div[2]/div/div['
                                    '1]/app-dados-pessoais/div[2]/div[2]/form/div[2]/div[3]/div['
                                    '1]/div/input').send_keys(
            email)
        esperar(1)

    def _preencher_fone(self, fone):
        self.navegador.find_element(By.XPATH,
                                    '//*[@id="kt_content"]/div/div/app-cadastro/div[2]/div/div['
                                    '1]/app-dados-pessoais/div[2]/div[2]/form/div[2]/div[3]/div[3]/div/input').clear()

        self.navegador.find_element(By.XPATH,
                                    '//*[@id="kt_content"]/div/div/app-cadastro/div[2]/div/div['
                                    '1]/app-dados-pessoais/div[2]/div[2]/form/div[2]/div[3]/div['
                                    '3]/div/input').send_keys(
            fone)
        esperar(1)

    def _salvar_atualizacoes(self):
        self.navegador.find_element(By.XPATH,
                                    '//*[@id="kt_content"]/div/div/app-cadastro/div[2]/div/div['
                                    '1]/app-dados-pessoais/div[2]/div[2]/div/div/button[2]').click()
        esperar(10)

        # Adiciona o nome da pessoa no TxT nomes já enviados
        with open(r"arquivos_de_apoio\lixeira.txt", "a") as arquivo:
            arquivo.write(f'{self.nome}\n')

    def gerar_credencial(self):
        try:
            self.navegador.find_element(By.XPATH,
                                        '//*[@id="kt_content"]/div/div/app-cadastro/div[2]/div/div['
                                        '1]/app-dados-pessoais/div[2]/div[1]/div/button[3]').click()
            esperar(10)
        except:
            py.press('tab')
            esperar(5)
            self.navegador.find_element(By.XPATH,
                                        '//*[@id="kt_content"]/div/div/app-cadastro/div[2]/div/div['
                                        '1]/app-dados-pessoais/div[2]/div[1]/div/button[3]').click()

    def coletar_login_senha(self):
        self._selecionar_link()
        py.press('esc')
        esperar(2)

        self.login = self.navegador.find_element(By.XPATH, '/html/body/table[1]/tbody/tr/td/table/tbody/tr['
                                                           '2]/td/table[2]/tbody/tr[3]/td').text

        self.senha = self.navegador.find_element(By.XPATH, '/html/body/table[1]/tbody/tr/td/table/tbody/tr['
                                                           '2]/td/table[2]/tbody/tr[4]/td').text

    def _selecionar_link(self):
        py.press('esc')
        esperar(0.2)
        py.press('tab')
        py.press('tab')
        py.press('esc')
        py.press('tab')
        py.press('tab')

        esperar(0.2)
        py.hotkey('ctrl', 'c')
        link = clipboard.paste()
        py.hotkey('ctrl', 'w')
        self.navegador.get(link)

    def enviar_whatsapp(self):
        self.navegador.get('https://web.whatsapp.com/')

        text = f'''
        Olá, informamos que a sua conta no portal E-class já está criada. 
        Para acessá-la basta entrar no link - https://login.educacaoadventista.org.br/

        {self.login}
        {self.senha} 

        Obs. A senha fornecida é uma senha provisória, que precisará ser alterada no primeiro acesso!

        Caso o próprio sistema não peça para alterar a senha, faça o seguinte procedimento;
        Entre no E-class→ Acessar → insira seu e-mail {self.login} → na tela de senha procure por “esqueceu a senha”.

        Atenção! Está é uma mensagem automática, responda apenas caso queira iniciar um atendimento.'''

        texto = urllib.parse.quote(text)

        while len(self.navegador.find_elements(By.ID, 'side')) < 1:
            sleep(1)

        link = f'https://web.whatsapp.com/send?phone={self.numero}&text={texto}'
        self.navegador.get(link)

        while len(self.navegador.find_elements(By.ID, 'side')) < 1:
            sleep(1)
        esperar(5)
        self.navegador.find_element(By.XPATH,
                                    '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p').send_keys(
            Keys.ENTER)
        esperar(5)


usuarios = criar_usuarios()
if usuarios:
    executar = Automacao()
    executar.main()
