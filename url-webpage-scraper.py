#Importing
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #To make browser headless(Run in background)


def startDriver():
    print(platform.system())
    PATH = ""
    if platform.system() == "Windows":
        PATH = "./chromedriver.exe"
    elif platform.system() == "Darwin": #Mac
        if platform.processor() == "i386" or platform.processor() == "arm":
            PATH = "./mac-m1/chromedriver"
        else:
            #Link to chromedriver
            pass

    #Setting up the driver path and options
    options = Options()
    options.add_argument("--headless") #Allows for headless browsing 
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
    #Print the content to the terminal.
    text = driver.find_element_by_tag_name("body").get_attribute("innerText")
    print(text)
    saveToFile(text,URL)
    driver.close()
    
    
def saveToFile(text,URL):
    #Save the text content of the webpage to a file.
    startURL = "www."
    endURL = ".com"
    websiteName = (URL[URL.index(startURL)+len(startURL):URL.index(endURL)])
    with open(websiteName+'Content.txt', 'w') as f:
        f.write(text)
    

if __name__ == "__main__":
    startDriver()