from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import platform
import pickle
from time import sleep 


class MyDriver:
    driver = None

    def __init__(self, not_window=False):
        os_info = platform.system()
        if os_info == 'Windows':
            op = webdriver.ChromeOptions()
            if not_window:
                op.add_argument("--headless")

            #op.add_argument("--incognito") # ESTAVA COMENTADO - deixa em janela anonima
            op.add_argument('--no-sandbox')
            op.add_argument("--start-maximized")
            op.add_argument("--disable-dev-shm-usage")  # Para evitar alguns problemas de memória
            op.add_argument("--disable-blink-features=AutomationControlled")  # Desabilita detecção de automação
            op.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
            #op.add_argument(r"user-data-dir=C:\\Users\\dodoc\\AppData\\Local\\Google\\Chrome\\User Data")
            #op.add_argument('window-size=1990,999')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)
            self.driver = driver



        elif os_info == 'Linux':
            op = Options()

            if not_window:
                op.headless = True
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=op)
            self.driver = driver

        # Remover a propriedade 'webdriver'
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # Alterar outras propriedades do navegador para evitar detecção
        driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]})")
        driver.execute_script("Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']})")


    def salvar_sessao(self):
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))

    def carregar_sessao(self):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
