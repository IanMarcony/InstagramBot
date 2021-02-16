from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time
import random

class InstagramBot:
  def __init__(self,username,password):
    self.username=username
    self.password=password
    self.driver=webdriver.Firefox(executable_path='./geckodriver')
  def login(self):
    driver=self.driver
    driver.get("https://www.instagram.com")
    time.sleep(10)
    elementUser = driver.find_element_by_xpath("//input[@name='username']")
    elementUser.click()
    elementUser.clear()
    elementUser.send_keys(self.username)
    elementPass = driver.find_element_by_xpath("//input[@name='password']")
    elementPass.click()
    elementPass.clear
    elementPass.send_keys(self.password)
    elementPass.send_keys(Keys.RETURN)
    time.sleep(5)
    url_p = input("Agora coloque o código da publicação - exemplo: www.instagram.com/p/jhasdaskjch - é este valor depois do /p/ , copie e cole aqui:  ")
    self.gotToPubliForComment(url_p)
  def gotToPubliForComment(self,url):
    driver=self.driver
    driver.get("https://www.instagram.com/p/"+url)
    time.sleep(30)
    tags=[]

    while True:
      msg = input("Digite o que seja comentar, caso não queria mais adicionar à lista digite N ou n: ")
      if(msg=="N" or msg=="n"):
        break
      tags.append(msg)
    print("Quantidade de Comentários: ",len(tags))
    for i in range(1,12500):
      print("Vez: ",i)
      try:
        if(i%20==0):
          driver.get("https://www.instagram.com/p/"+url)
          time.sleep(30)
        driver.find_element_by_class_name('Ypffh').click()
        elementText= driver.find_element_by_class_name('Ypffh')
        elementText.send_keys(tags[random.randint(0,len(tags)-1)])
        time.sleep(60)
        driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
        print("Vez: ",i,", com SUCESSO")
        time.sleep(30)
      except Exception as ex:
        print(ex)
        time.sleep(10)


print("Este bot utiliza o Firefox para manipular o Instagram \n")
print("Certifique-se que sua conta não está ativa com verificação em duas etapas \n")

username = input("Insira seu Username do Instagram: ")
password = getpass("Insira sua Senha do Instagram: ")

print("Caso tudo dê certo você entrará na sua conta \n")

igBotI= InstagramBot(username,password)
igBotI.login()
