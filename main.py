from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
url = "https://form.gov.sg/657903cb2086120011606261"
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get(url)

responseID = []

# def input(name, block_number, floor_number, unit_number, postal_code, training, status, date ,officer_name, NPC):
def input(name , block_number, floor_number, unit_number, postal_code, training, status, date, officer_name, NPC):
    
    name_input = driver.find_element(By.ID, '5e960d0a78a996001147755b')
    name_input.send_keys(name)

    block_number_input = driver.find_element(By.ID, '646741312034d2001235bdac')
    block_number_input.send_keys(block_number)

    floor_number_input = driver.find_element(By.ID, '646741581e17d000127b9f3b')
    floor_number_input.send_keys(floor_number)
    
    unit_number_input = driver.find_element(By.ID, '646741712014ed0011cdd4a4')
    unit_number_input.send_keys(unit_number)

    postal_code_input = driver.find_element(By.ID, '64674227c36fce00121019ba')
    postal_code_input.send_keys(postal_code)

    mode_of_traning_input = driver.find_element(By.ID, '64674334dcd7850012786996')
    mode_of_traning_input.send_keys(training, Keys.TAB)
   
    status_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, '659ce77a96c159001278539c')))
    status_input.send_keys(status, Keys.TAB)

    date_input = driver.find_element(By.ID, '646743551e17d000127beb5b')
    date_input.clear()
    date_input.send_keys(Keys.BACKSPACE * 10)
    date_input.send_keys(date)

    officer_name_input = driver.find_element(By.ID, '6467436530fc910012d93ed3')
    officer_name_input.send_keys(officer_name)

    
    npc_input= driver.find_element(By.ID, '6467453530fc910012d97feb')
    npc_input.send_keys(NPC, Keys.TAB)
    
    submit_button = driver.find_element(By.CLASS_NAME, 'chakra-button.css-1szjd8b')  
    submit_button.click()  
    
    response_id_element = driver.find_element(By.CLASS_NAME, 'chakra-text.css-jdumc1')
    response_id_text = response_id_element.text
    response_id = response_id_text.split(": ")[1]
    
    # print(response_id)

    responseID.append(response_id)
    # Click on the button
    print(responseID)

    another_form = driver.find_element(By.CLASS_NAME, 'chakra-button.css-4my61l')
    another_form.click()

    

name = "David"
block_number = 123
floor_number = 12
unit_number = 712
postal_code = 12313
training = "Official: House Visit By SPF"
status = "Completed"
date_string = "03/01/2024"
officer_name = "Kelvin"
NPC = "Queenstown NPC"


for i in range(2):
    input(name , block_number, floor_number, unit_number, postal_code, training, status, date_string, officer_name, NPC)
driver.quit()

