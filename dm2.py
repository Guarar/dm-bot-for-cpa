# solo dm, no likes
# loggea con usuarios, busca hashtags, se va al perfil de cada hashtag (total de 6 por usuario), y les envia dm, despues lo borra del txt
from logging import exception
from weakref import ref
from selenium import webdriver
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.utils import download_file



from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager as CM

f = open('accounts.json',)
datas = json.load(f)




def doesnt_exist(driver, classname):
    try:
        driver.find_element_by_class_name(classname)
    except NoSuchElementException:
        return True
    else:
        return False

def doesnt_existxpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return True
    else:
        return False

#usernames = []

with open('usernames.txt', 'r') as f:
    #for line in f:
        #usernames.append(line.rstrip("\n"))
    usernames = [line.strip() for line in f]

#with open('messages_rap.txt', 'r') as f:
with open('messages_au_giveaway.txt', 'r') as f:
    messages = [line.strip() for line in f]

with open('messages_au_giveawaylink.txt', 'r') as f:
    messageslink = [line.strip() for line in f]

#with open('tagsrap.txt', 'r') as f:
with open('tagsau.txt', 'r') as f:
    tags = [line.strip() for line in f]



between_messages = 5
refresht = 4


#/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/p    we could connect to instagram
# /html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/p                    password incorret
#/html/body/div[1]/div[1]/div[2]/h1/span                    xpath this page isnt working
def main(data):
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options, executable_path=CM().install())
    browser.get('https://instagram.com')
    time.sleep(random.randrange(3,4))
    if doesnt_existxpath(browser, '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/span'):
        print('Iniciando bien')
    else:
        browser.refresh()
        time.sleep(random.randrange(3,4))

    
    
    
    # inicio de sesion
    

    input_username = browser.find_element_by_name('username')
    input_password = browser.find_element_by_name('password')

    input_username.send_keys(data["username"])
    time.sleep(random.randrange(1,2))
    
    input_password.send_keys(data["password"])
    time.sleep(random.randrange(1,2))

    input_password.send_keys(Keys.ENTER)

    print('Iniciando sesion con ---> ' + data["username"])
    time.sleep(6)

    # ==========================================

    # Enviar DMS ============================


    time.sleep(2)
    #checa si el reload page existe
    if doesnt_existxpath(browser, '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/span'):
        print('Refresh Pass')
        time.sleep(1)
    else:
        browser.refresh()
        time.sleep(random.randrange(3,4))
        

        #checa si tiro letras rojas al iniciar sesion, para else refresh
    if doesnt_existxpath(browser, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/p'):
        print('Sign In Pass')
        time.sleep(1)
    else:
        browser.refresh()
        time.sleep(random.randrange(3,4))
        input_username = browser.find_element_by_name('username')
        input_password = browser.find_element_by_name('password')

        input_username.send_keys(data["username"])
        time.sleep(random.randrange(1,2))
        
        input_password.send_keys(data["password"])
        time.sleep(random.randrange(1,2))

        input_password.send_keys(Keys.ENTER)

        print('Iniciando sesion con ---> ' + data["username"])
        time.sleep(6)
    


        #comprueba si el div exite, true = no inciado sesion        false = si inicio sesion
    if doesnt_existxpath(browser, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/p'):


        browser.get('https://www.instagram.com/direct/inbox/')
        time.sleep(2)

        #comprueba refresh
        if doesnt_existxpath(browser, '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/span'):
            print('______')
            time.sleep(4)
        else:
            browser.refresh()
            time.sleep(random.randrange(3,4))

        #comprueba el not now
        #if doesnt_existxpath(browser, '/html/body/div[5]/div/div/div/div[3]/button[2]'):
        #        print('not now pasado')
        #else:
        #click not now
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        time.sleep(random.randrange(1,2))

        i = 0
        for user in usernames:
            

            if i >= 3:
                print('Limite Completado')
                break
            
            #click new msj
            browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()

            time.sleep(1)
            #input para el username a enviar
            browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)

            #clicke el primer perfil
            time.sleep(random.randrange(2,3))
            browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]').find_element_by_tag_name('button').click()

            #click next
            time.sleep(random.randrange(3,4))
            browser.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()

            #estabelece el textarea
            time.sleep(random.randrange(4,5))
            text_area = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            

            text_area.send_keys('Hola ' + user + random.choice(messages))
            
            time.sleep(random.randrange(3,5))
            text_area.send_keys(Keys.ENTER)
            text_area = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            text_area.send_keys(messageslink)
            time.sleep(random.randrange(3,5))
            text_area.send_keys(Keys.ENTER)
            print(f'Message successfully sent to {user}')
            time.sleep(random.randrange(1,2))

            #vamos a eliminar el username usado
            with open("usernames.txt", "r") as f:
                lines = f.readlines()
            with open("usernames.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != user:
                        time.sleep(1)
                        print('adios ' + user)
                        f.write(line)
            time.sleep(1)
            i += 1   
            
                
            
    else:
        print('There was a proble, skipping to next account')
    time.sleep(3)       
    browser.close()

while True:
    for data in datas:
        main(data)

# Sending messages:
# def send_message(users, messages):
