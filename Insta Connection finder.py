import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

username=""                 #Use Yours
password=""                 #Use Yours

visited = []
queue = []

visited.append(username)
queue.append(username)
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
# element=driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")
# element.click()
                                        #REACHING PROFILE
time.sleep(3)
element=driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img") #to open option to profile my image
element.click()
time.sleep(1)
element=driver.find_element_by_link_text("Profile")
element.click()
j=0
                                        #BFS
while (j<3):
    s = queue.pop(0) 
    print (s, end = " ")
    driver.get('https://www.instagram.com/'+s) 
    time.sleep(2)
    element=driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")  #following button
    element.click()
    time.sleep(2)
    scroll_box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")      #following list
    last_ht, ht = 0, 1
    while last_ht != ht:
        last_ht = ht
        time.sleep(1.3)
        ht = driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
            return arguments[0].scrollHeight;
            """, scroll_box)
    links = scroll_box.find_elements_by_tag_name('a')
    names = [name.text for name in links if name.text != '']
    # i=0
    # while(i<390):  
    #     print(names[i])
    #     i=i+1
    random.shuffle(names)
    for neighbour in names:   
        if neighbour not in visited: 
            visited.append(neighbour)
            queue.append(neighbour)


                           







