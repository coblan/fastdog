from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait,TimeoutException
from selenium.webdriver.common.by import By

def visible(driver,selector,timeout=10):
    #ls = driver.find_elements_by_css_selector(selector)
    #cout = 0
    #while not ls:
        #time.sleep(1)
        #cout += 1
        #ls = driver.find_elements_by_css_selector(selector)
        #if cout > timeout:
            #raise UserWarning('超时')

    element = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
    ) 

def hide(driver,selector,timeout=60*5):
    element = WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, selector))
        
    )  

def inputText(driver,selector,text):
    inputele = driver.find_elements_by_css_selector(selector)[0]
    inputele.send_keys(text)

def click(driver,selector):
    btn = driver.find_elements_by_css_selector(selector)[0]
    btn.click()
