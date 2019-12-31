from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from random import choice
import time
import re

servidor="https://lima.chateagratis.net"
canal="mexico"
nick="karlitaM23"
data=servidor+"/?nick="+nick+"&channels=%23"+canal
tiempo=1800
repetir=300
archivo="mensajes.txt"

browser = webdriver.Chrome('chromedriver.exe')
actions = ActionChains(browser)

def login(data):
    browser.get(data)

def msg(input):
    txt=open(archivo,'r')
    msgList = [i for i in txt]
    msg=re.sub("\n","",choice(msgList))
    input.send_keys(msg)
    browser.implicitly_wait(2)
    input.send_keys(Keys.RETURN)
    input.clear()

def main():
    login(data)
    browser.implicitly_wait(5)
    time.sleep(10)
    input=browser.find_elements_by_xpath('/html/body/div/div[5]/div[2]/div[1]/textarea')
    browser.implicitly_wait(3)
    time.sleep(3)
    start_time=time.time()
    while True:
        time.sleep(repetir)
        msg(input[0])
        r=round(time.time()-start_time)
        print("Enviado",str(r))
        if r>=tiempo:
            break
if __name__ == '__main__':
    main()
