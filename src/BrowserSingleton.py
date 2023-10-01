from selenium import webdriver

class BrowserSingleton():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BrowserSingleton, cls).__new__(cls)
            cls.instance = webdriver.Firefox()
        return cls.instance    