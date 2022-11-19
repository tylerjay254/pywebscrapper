from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.core.utils import read_version_from_cmd, PATTERN

import os 

#driver istallation 

def driverinstaller(browser):
    '''takes the name of users browser as argument'''
    
    #chrome 
    if browser == "chrome"or "google-chrome":
        # check version 
        version = read_version_from_cmd("/usr/bin/google-chrome --version", PATTERN["google-chrome"])

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version= version).install()))
    
    #chromium

    elif browser == "chromium":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    elif browser == "brave":
        webdriver.Chrome(service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
    
    #firefox
    elif browser == "firefox" or "mozilla-firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    #edge
    elif browser == "msedge"or "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        

    #opera
    elif browser == "opera" or "opera-mini":
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        

    else :
        return f'The browser indicated is not supported'




driverinstaller("chrome")












