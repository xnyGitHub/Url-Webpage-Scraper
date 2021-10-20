#Importing
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #To make browser headless(Run in background)


def startDriver():
    #Setting up the driver path and options
    PATH = "./chromedriver" 
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, executable_path=PATH)

    #Taking in user input
    URL = input("Enter a website: ")

    #Loading the website
    try:
        driver.get(URL)
        # printContent(hURL)
    except Exception as e:
        print(e)
        print("Please read error above")
    #Do something

def printContent():
    pass
    #Get content
    
def saveToFile():
    pass
    #Save to file

if __name__ == "__main__":
    startDriver()