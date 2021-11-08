from flask import Flask, render_template,request,url_for,redirect,session
import arg_app


app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def homepage():
    if request.method == "POST":
        URL = request.form['website']
        content = arg_app.get_content(URL)
        
        if content != None:
            return render_template(
                'scraped_page.html',content=content
                )
        else:
            return render_template(
                "index.html",content = "Please make sure you enter a valid link"
            )      
    else:
        return render_template(
            "index.html"
            )
    
@app.route('/scraped_page')
def scrapepage():
    #Show the content here
    return render_template("scraped_page.html")
        
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)