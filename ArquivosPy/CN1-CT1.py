from selenium import webdriver
import datetime
import logging
import time
import os

#Cria um diretório novo para armazenar as prints caso não exista
Armazenar = 'Prints Caminho Negativo'
if not os.path.exists(Armazenar):
    os.makedirs(Armazenar)

#Pega a hora Local do Computador para usar de Nomeação
agora = datetime.datetime.now()
Agora_String = agora.strftime('%Y-%m-%d_%H-%M-%S')
logging.basicConfig(filename='Selenium'+Agora_String+'_log.txt', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


#Teste de Caminho Negativo
driver = webdriver.Firefox()
url_login = "https://play.watch.tv.br/login"
try:
    driver.get(url_login)
    driver.maximize_window()
    time.sleep (4)
    driver.get_screenshot_as_file((os.path.join(Armazenar, 'Print0001.png')))
    logging.info('Página Acessada')
    driver.find_element('xpath','/html/body/app-root/div/div/app-page/div/section/app-login-master/app-login-ktp/div/form/div[2]/app-input[1]/div/input').send_keys("guilherme.liz14@gmail.com")
    logging.info('Preenchimento de Email no Campo de Login')
    time.sleep (4)
    driver.get_screenshot_as_file((os.path.join(Armazenar, 'Print0002.png')))
    driver.find_element('xpath','/html/body/app-root/div/div/app-page/div/section/app-login-master/app-login-ktp/div/form/div[2]/app-input[2]/div/input').send_keys("123321")
    logging.info('Preenchimento de Senha errada no Campo')
    time.sleep (4)
    driver.get_screenshot_as_file((os.path.join(Armazenar, 'Print0003.png')))
    driver.find_element('xpath','/html/body/app-root/div/div/app-page/div/section/app-login-master/app-login-ktp/div/form/div[3]/app-button/button').click()
    logging.info('Click no Botão para realizar Login')
    time.sleep (4)
    driver.get_screenshot_as_file((os.path.join(Armazenar, 'Print0004.png')))
    
except Exception as e:
    logging.error('Ocorreu um erro: %s', str(e))

driver.quit()