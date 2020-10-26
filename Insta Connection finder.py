import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import re 


username=input("Insta user ID ")
src=username
target=input("Enter to whom you want to connect ")
webdriverpath=input("Webdriver path ")
width=int(input("Give width of tree"))
maxDepth=int(input("Give depth of tree"))
password=input("Insta Password ")





                                        #OPEN INSTAGRAM
driver = webdriver.Chrome("D:\software\chrome driver\chromedriver.exe")# Optional argument, if not specified will search path.
driver.maximize_window()  
driver.get('https://www.instagram.com/') 
                                        #CREDENTIAL LOGIN
time.sleep(6)                                        
element=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
element.send_keys(username)
element=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
element.send_keys(password)
element.send_keys(Keys.RETURN)

    


def DLS(src,target,maxDepth,width):    
    if src == target : 
        print("path"+src)
        return True 
    if maxDepth <= 0 : return False 
    i=1
    time.sleep(2)
    while(i<=width):
        time.sleep(3)
        driver.get('https://www.instagram.com/'+src)
        time.sleep(3)
        pvt = driver.page_source
        pvtfound = re.search(r'This Account is Private', pvt)
        if(pvtfound == None) : #if true means private         
            element=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")  #following button
            element.click() #following button
            time.sleep(3)
            person =driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[2]/div[1]/div/div/span/a").text
            time.sleep(3)
            print(person)
            if(DLS(person,target,maxDepth-1,width)): 
                print("path"+person)
                return True
        else:    
            return False
        i=i+1    
    return False    
DLS(src,target,maxDepth,width)
