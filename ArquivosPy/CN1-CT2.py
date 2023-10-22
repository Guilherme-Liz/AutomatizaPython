from selenium import webdriver
import datetime
import logging
import time
import os

#Cria um diretório novo para armazenar as prints caso não exista
Armazenar = 'Prints Caminho Positivo'
if not os.path.exists(Armazenar):
    os.makedirs(Armazenar)

#Pega a hora Local do Computador para usar de Nomeação
agora = datetime.datetime.now()
Agora_String = agora.strftime('%Y-%m-%d_%H-%M-%S')
logging.basicConfig(filename='Selenium'+Agora_String+'_log.txt', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


#Teste de Caminho Positivo
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
    driver.find_element('xpath','/html/body/app-root/div/div/app-page/div/section/app-login-master/app-login-ktp/div/form/div[2]/app-input[2]/div/input').send_keys("Guilherme132#")
    logging.info('Preenchimento de Senha no Campo de Login')
    time.sleep (4)
    driver.get_screenshot_as_file((os.path.join(Armazenar, 'Print0003.png')))
    driver.find_element('xpath','/html/body/app-root/div/div/app-page/div/section/app-login-master/app-login-ktp/div/form/div[3]/app-button/button').click()
    logging.info('Click no Botão para realizar Login')
    time.sleep (4)
    driver.get_screenshot_as_file((os.path.join(Armazenar, 'Print0004.png')))
    driver.find_element('xpath','/html/body/app-root/div/div/app-page/div/section/app-select-master/app-profile-select/div[1]/div/div[1]/div').click()
    logging.info('Click No botão de selecionar Perfil de Cliente')
    time.sleep (4)
    driver.get_screenshot_as_file((os.path.join(Armazenar, 'Print0005.png')))
    driver.find_element('xpath','/html/body/app-root/div/div/app-page/div/app-header/nav/div[1]/div/ul/li[2]/div/a').click()
    logging.info('Selecionar Categoria para assistir')
    time.sleep (4)
    driver.get_screenshot_as_file((os.path.join(Armazenar, 'Print0006.png')))
    driver.find_element('xpath','/html/body/app-root/div/div/app-page/div/app-header/nav/div[1]/div/ul/li[2]/app-dropdown-categories/div/div[2]/ul[1]/li').click()
    logging.info('Categoria selecionada')
    time.sleep (4)
    driver.get_screenshot_as_file((os.path.join(Armazenar, 'Print0007.png')))
    driver.find_element('xpath','/html/body/app-root/div/div/app-page/div/section/app-ver-mais/div/div[2]/div[3]/div[2]/app-card/div').click()
    logging.info('Selecionando série para assistir')
    time.sleep (4)
    driver.get_screenshot_as_file((os.path.join(Armazenar, 'Print0008.png')))
    driver.find_element('xpath','/html/body/app-root/div/div/app-page/div/section/app-movies-and-series/div[1]/app-series-banner/div/div[3]/div[4]/app-play-button/button').click()
    logging.info('Clickando na série para assistir')
    time.sleep (4)
    driver.get_screenshot_as_file((os.path.join(Armazenar, 'Print0009.png')))
    driver.find_element('xpath','/html/body/app-root/div/div/app-page/div/section/app-watch-master/app-watch/div[2]/div[3]/div[1]/img').click()
    logging.info('Saindo do Player da série Selecionada')
    time.sleep (4)
    driver.get_screenshot_as_file((os.path.join(Armazenar, 'Print0010.png')))
    driver.find_element('xpath','/html/body/app-root/div/div/app-page/div/app-header/nav/div[2]/app-dropdown-header/div/a/img').click()
    logging.info('Clickando no perfil do usuário')
    time.sleep (4)
    driver.get_screenshot_as_file((os.path.join(Armazenar, 'Print0011.png')))
    driver.find_element('xpath','/html/body/app-root/div/div/app-page/div/app-header/nav/div[2]/app-dropdown-header/div/div[2]/ul[2]/li[4]/a').click()
    logging.info('Saindo do perfil do usuário')
    time.sleep (4)
    driver.get_screenshot_as_file((os.path.join(Armazenar, 'Print0012.png')))

except Exception as e:
    logging.error('Ocorreu um erro: %s', str(e))

driver.quit()