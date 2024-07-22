from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Users\\AppData\\Local\\Google\\Chrome\\User Data")
navegador = webdriver.Chrome(options=chrome_options)


url='https://web.whatsapp.com/'
# Localiza o elemento pela classe especificada
class_name_label_chat = "selectable-text copyable-text x15bjb6t x1n2onr6"
navegador.get(url)
teste=0

while True:
    while len(navegador.find_elements(By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/canvas')) ==1:
        print(len(navegador.find_elements(By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/canvas')))
        pass
    while len(navegador.find_elements(By.ID, 'side'))<1:
        pass
    # Localiza o elemento pelo XPath
    title_value = "Nego"
    xpath = f'//span[@title="{title_value}"]'
    elementos = navegador.find_elements(By.XPATH,xpath)
    
    if elementos:
        # Acessa o primeiro elemento encontrado na lista
        elemento = elementos[0]
        
        # Clica no elemento
        elemento.click()
        print(f"Clicou no elemento com o título '{title_value}'")
        xpath_filho='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        pais=navegador.find_elements(By.ID,'main')
        pai = pais[0]
        caixa_textos=pai.find_elements(By.XPATH,xpath_filho)
        if caixa_textos:
            caixa_texto=caixa_textos[0]
            caixa_texto.click()
            if teste <= 100:
                teste+=1
                caixa_texto.click()
                mensagem = "Bot_teste"
                caixa_texto.send_keys(mensagem)
                caixa_texto.send_keys(Keys.ENTER)
            else:
                exit()


        
    else:
        print(f"Elemento com o título '{title_value}' não encontrado")
        
    # Exemplo de interação (por exemplo, obter o texto do elemento)
  