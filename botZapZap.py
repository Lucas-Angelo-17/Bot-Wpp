from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class zapzapBot:
    def __init__(self):
        self.mensagem = "Salve Salve Familia"
        self. grupos = ["aaaa"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    
    def enviarMensagens(self):
        #<span dir="auto" title="aaaa" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">aaaa</span>
        #<div tabindex="-1" class="p3_M1">
        #<span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)

        for grupo in self.grupos:
            #grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            grupo = self.driver.find_element(by=By.XPATH, valeu = f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            chat_box = self.driver.find_element(by=By.CLASS_NAME, valeu = 'p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            #botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            botao_enviar = self.driver.find_element(by=By.XPATH, valeu = "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = zapzapBot()
bot.enviarMensagens()



        
