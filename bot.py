from selenium import webdriver  
import os
import time

class InstaBot:
    def __init__(self,username, password):

        '''
            Initalting and instance of instagram bot class
            calls the login method to authenticate a user
         args: 
            #* username:str : the username for instagram
            #* password :str :the password for instagram
        attrib:
            #* Driver : selenium.webdriver.Chrome : The driver that is used to automate
            
        
        '''
        self.baseURL="https://www.instagram.com/"
        self.username = username  
        self.password = password
        self.driver = webdriver.Chrome("./chromedriver")
        self.login()
        
        

    def login(self):
        
        self.driver.get(f"{self.baseURL}accounts/login/")
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click() 
        #?why is Log in working with single quote and not double quote? WTF?
        self.driver.get(f'{self.baseURL}alpharoy14')
    def nav_user(self,user):
        self.driver.get(f'{self.baseURL}{user}')
    def follow_user(self,user):
        self.nav_user()
        #TODO follow button




if __name__ == "__main__":
    ig_bot=InstaBot("Temp","Temp")
    time.sleep(3)
    ig_bot.nav_user("alpharoy14")
    print (ig_bot.username)





