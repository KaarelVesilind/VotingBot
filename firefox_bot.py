from selenium import webdriver
from time import sleep,localtime,strftime
from random import randint
from selenium.webdriver.firefox.options import Options
class Goldbot():
    def __init__(self):
        opt = Options()
        opt.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.driver = webdriver.Firefox(options=opt, executable_path=r'C:\\Users\\Kaarel Vesilind\\Documents\\Botid\\Draiverid\\geckodriver.exe')
    def videovalik(self):
        self.driver.get("https://novaator.err.ee/k/goldbergimasin")
        sleep(1)
        otsing = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]/div[1]/input')
        self.driver.execute_script('arguments[0].scrollIntoView()', otsing)
        otsing.send_keys('vesilind')
    def hääleta(self):
        video = self.driver.find_element_by_xpath('//*[@id="mediaId_0"]') 
        video.click()
        video.click()

while True:
    bot = Goldbot()
    bot.videovalik()
    sleep(1)
    bot.hääleta()
    print("Firefox, hääletatud kell:",strftime("%H:%M:%S", localtime()))
    sleep(3)
    bot.driver.close()
    sleep(randint(3605,3900))