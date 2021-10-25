from flask import Flask, render_template,request,url_for,redirect
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import platform

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def homePage():
    if request.method == "POST":
        #If the user presses the button
        pass
    else:
        return render_template("index.html")
    
@app.route('/scraped_page')
def scrapePage():
    #Show the content here
    return render_template("scraped_page.html")
    
def webScraper(userInput):
    #userInput is the link (http://example.com) that the user wants to scrape
    #Setting up the driver path
    PATH = ""
    if platform.system() == "Windows":
        PATH = "./windows/chromedriver.exe"
    elif platform.system() == "Darwin": #Mac
        if platform.processor() == "i386" or platform.processor() == "arm":
            PATH = "./mac-m1/chromedriver"
        else:
            PATH = "./mac/chromedriver"

    #Setting up options
    options = Options()
    options.add_argument("--headless") #Allows for headless browsing 
    driver = webdriver.Chrome(options=options, executable_path=PATH)

    URL = userInput
    
     #Loading the website
    try:
        driver.get(URL)
        content = driver.find_element_by_tag_name("body").get_attribute("innerText")
        return content
    except Exception as e:
        print(e)
        print("Please read error above")
        
if __name__ == "__main__":
    app.run(debug=True)
