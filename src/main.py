from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
import time
import credentials
from BrowserSingleton import BrowserSingleton
 
def waitAndClick(wait, clickable: WebElement):        
    wait.until(lambda d : clickable.is_displayed())
    clickable.click() 

# Return element that contains searchString in the specified attribute
def searchElement(wait, elements: list[WebElement],attribute: str , searchString: str):   
    print(len(elements))
    for element in elements:        
        print(element.get_attribute(attribute))
        print(element.get_attribute(attribute).find(searchString))
        if element.get_attribute(attribute).find(searchString) != -1:
            return element
    raise Exception("Element was not found")

browser = BrowserSingleton()
browser.get("https://www.linkedin.com")
title = browser.title
wait = WebDriverWait(browser, timeout=10)
# TODO turn company name into program arg
WantedCompanyName = "Senhub.io"

wait.until(lambda d : browser.find_element(By.XPATH, value="//button[@type='submit']").is_displayed())

loginForm = browser.find_element(By.ID,"session_key")
psswdForm = browser.find_element(By.ID,"session_password")
button = browser.find_element(By.XPATH, value="//button[@type='submit']")

loginForm.send_keys(credentials.login)
psswdForm.send_keys(credentials.psswd)
button.click()

#pass captcha ;(
# time.sleep(15)

#Profile picture click > into dropdown
waitAndClick(wait, browser.find_element(By.ID, "ember15"))
#Into profile page
waitAndClick(wait, browser.find_element(By.XPATH, value="//a[@class='ember-view artdeco-button artdeco-button--secondary artdeco-button--1 mt2 full-width']"))
#Into company profile tab
wait.until(lambda d : browser.find_element(By.XPATH, value="//div[@class='artdeco-tablist ember-view']").is_displayed())
waitAndClick(wait, browser.find_element(By.XPATH, value="//div[@class='artdeco-tablist ember-view']/button[2]"))
#Into followed companies page
waitAndClick(wait, browser.find_element(By.ID, "navigation-index-see-all-companies"))
#Into to be Liked company page
# waitAndClick(browser.find_element(By.XPATH,value="//span[text()='Senhub.io']"))

wait.until(lambda d : browser.find_element(By.XPATH, value="//a[@data-field='active_tab_companies_interests']").is_displayed())
companiesContainers = browser.find_elements(By.XPATH, value="//a[@data-field='active_tab_companies_interests']")
for companyContainer in companiesContainers:    
    # companySpan = companyContainer.find_element(By.XPATH, value="div/div/div/div/span")
    try:
        companyA = companyContainer.find_element(By.XPATH, value="div/div/img")                
        if companyA.get_attribute("alt").find(WantedCompanyName) != -1:
            companyA.click()
            break            
    except NoSuchElementException:
        pass
wait.until(lambda d : len(browser.find_elements(By.XPATH, value="//a")) > 7)
button = searchElement(wait, browser.find_elements(By.XPATH, value="//a"),"href","posts")
print("button =" + button.text)
print(button.location)
#Into all posts
button.click()
# waitAndClick(browser.find_element(By.PARTIAL_LINK_TEXT, "posts"))
print("woohoo pas d'erreur")