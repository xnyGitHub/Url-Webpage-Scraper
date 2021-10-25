from flask import Flask, render_template,request,url_for,redirect
from selenium.webdriver.chrome.options import Options


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
    #We will scrape the content here and return it
    pass
        
if __name__ == "__main__":
    app.run(debug=True)
