from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import credentials

browser = webdriver.Firefox()
browser.get("https://www.linkedin.com")
title = browser.title
wait = WebDriverWait(browser, timeout=10)
loginForm = browser.find_element(By.ID,"session_key")
psswdForm = browser.find_element(By.ID,"session_password")
submitButton = browser.find_element(By.XPATH, value="//button[@type='submit']")

wait.until(lambda d : submitButton.is_displayed())

loginForm.send_keys(credentials.login)
psswdForm.send_keys(credentials.psswd)
submitButton.click()

print(loginForm)
print(psswdForm)
print(submitButton)
print(title)