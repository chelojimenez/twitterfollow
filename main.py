from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

archivo = open("cuenta.txt", "r")
usuario = archivo.readline()
contra = archivo.readline()
archivo2 = open("hashtags.txt", "r")
lineas = archivo2.readlines()
hashtags = []
for tag in lineas:
    hashtags.append(tag)

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome("chromedriver.exe")
    
    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/login?lang=es")
        sleep(15)
        user = bot.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")
        contrasena = bot.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")
        
        user.clear()
        contrasena.clear()
        user.send_keys(usuario)
        contrasena.send_keys(contra)

        contrasena.send_keys(Keys.RETURN)
        sleep(3)
    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get("https://twitter.com/search?q=" + hashtag + "&src=typed_query")
        sleep(3)
        for i in range(1,7):
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')




bot = TwitterBot(usuario, contra)
bot.login()
#[bot.like_tweet(tag) for tag in hashtags]

