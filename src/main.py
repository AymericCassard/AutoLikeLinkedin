from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement as WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import credentials
from BrowserSingleton import BrowserSingleton

browser = BrowserSingleton()
wait = WebDriverWait(browser, timeout=10)


def waitAndClick(wait, clickable: WebElement):
    wait.until(lambda d: clickable.is_displayed())
    clickable.click()


# Return element that contains searchString in the specified attribute
def searchElement(wait, elements: list[WebElement], attribute: str, searchString: str):
    if searchString == "false":
        searchString = False
    for element in elements:
        if element.get_attribute(attribute).find(searchString) != -1:
            return element
    raise Exception("Element was not found")


def waitPostsCompletion():
    wait = WebDriverWait(browser, 5)
    while 1 == 1:
        try:
            postsList = browser.find_elements(
                By.XPATH, value="//div[@class='scaffold-finite-scroll__content']/div"
            )
            postsNb = len(postsList)
            html.send_keys(Keys.END)
            wait.until(
                lambda d: postsNb
                != len(
                    browser.find_elements(
                        By.XPATH,
                        value="//div[@class='scaffold-finite-scroll__content']/div",
                    )
                )
            )
        except TimeoutException:
            break
        else:
            continue
    return browser.find_elements(
        By.XPATH, value="//div[@class='scaffold-finite-scroll__content']/div"
    )


def login():
    browser.get("https://www.linkedin.com")
    wait.until(
        lambda d: browser.find_element(
            By.XPATH, value="//button[@type='submit']"
        ).is_displayed()
    )

    loginForm = browser.find_element(By.ID, "session_key")
    psswdForm = browser.find_element(By.ID, "session_password")
    button = browser.find_element(By.XPATH, value="//button[@type='submit']")

    loginForm.send_keys(credentials.login)
    psswdForm.send_keys(credentials.psswd)
    button.click()


login()

# pass captcha ;(
# time.sleep(15)
# TODO turn company name into program arg
WantedCompanyName = "Senhub.io"

# Profile picture click > into dropdown
waitAndClick(wait, browser.find_element(By.ID, "ember15"))
# Into profile page
waitAndClick(
    wait,
    browser.find_element(
        By.XPATH,
        value="//a[@class='ember-view artdeco-button artdeco-button--secondary artdeco-button--1 mt2 full-width']",
    ),
)
# Into company profile tab
wait.until(
    lambda d: browser.find_element(
        By.XPATH, value="//div[@class='artdeco-tablist ember-view']"
    ).is_displayed()
)
waitAndClick(
    wait,
    browser.find_element(
        By.XPATH, value="//div[@class='artdeco-tablist ember-view']/button[2]"
    ),
)
# Into followed companies page
waitAndClick(wait, browser.find_element(By.ID, "navigation-index-see-all-companies"))
# Into to be Liked company page
# waitAndClick(browser.find_element(By.XPATH,value="//span[text()='Senhub.io']"))

wait.until(
    lambda d: browser.find_element(
        By.XPATH, value="//a[@data-field='active_tab_companies_interests']"
    ).is_displayed()
)
companiesContainers = browser.find_elements(
    By.XPATH, value="//a[@data-field='active_tab_companies_interests']"
)
for companyContainer in companiesContainers:
    # companySpan = companyContainer.find_element(By.XPATH, value="div/div/div/div/span")
    try:
        companyA = companyContainer.find_element(By.XPATH, value="div/div/img")
        if companyA.get_attribute("alt").find(WantedCompanyName) != -1:
            companyA.click()
            break
    except NoSuchElementException:
        pass
# wait.until(lambda d : len(browser.find_elements(By.XPATH, value="//a")) > 7)
wait.until(lambda d: browser.find_element(By.ID, value="-target-image").is_displayed())
button = searchElement(
    wait, browser.find_elements(By.XPATH, value="//a"), "href", "posts"
)
# Into all posts
button.click()

html = browser.find_element(By.XPATH, value="//html")
wait.until(
    lambda d: browser.find_element(
        By.XPATH, value="//div[@class='scaffold-finite-scroll__content']"
    ).is_displayed()
)
postsList = waitPostsCompletion()
# List with all posts div container
print(postsList)
print(len(postsList))


def clickMatchingButton(buttons, action):
    for button in buttons:
        if button.get_attribute("aria-pressed") is not None:
            likeButton = button
            break


# for post in postsList:
#     buttons = post.find_elements(By.TAG_NAME, "button")
#     for button in buttons:
#         if button.get_attribute("aria-pressed") == "false":
#             button.click()
#         if button.get_attribute("aria-pressed") == "true":
#             button.click()
#         else:
#             print("not LikeButton")
# for button in buttons:
# try:
#     likeButton = searchElement(wait, buttons, "aria-pressed", "false")
# except Exception:
#     print("likeButton was not found")
# if isinstance(buttons, WebElement):
#     print("1")
# else:
#     print(len(button))
# waitAndClick(browser.find_element(By.PARTIAL_LINK_TEXT, "posts"))
print("woohoo pas d'erreur")
