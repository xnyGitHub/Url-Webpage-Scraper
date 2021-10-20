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
        printContent(driver,URL)
    except Exception as e:
        print(e)
        print("Please read error above")

def printContent(driver,URL):
    text = driver.find_element_by_tag_name("body").get_attribute("innerText")
    print(text)
    saveToFile(text,URL)
    driver.close()
    #Get content
    
def saveToFile(text,URL):
    startURL = "www."
    endURL = ".com"
    websiteName = (URL[URL.index(startURL)+len(startURL):URL.index(endURL)])
    with open(websiteName+'Content.txt', 'w') as f:
        f.write(text)
    #Save to file

if __name__ == "__main__":
    startDriver()