# Webscraper with Docker,Flask, Command-Line and Unit/Doc-testing

## Description 📝

This is a simple Webscraping script that extracts the text that sits in the body of the HTML page. The user is able to do this in three ways.

1. Pass in the website through the command line.
2. Start a flask server and pass in the website through there.
3. Start a flask server within a docker container and pass it through there.

The code will not allow any sites without the **https://** before it.

---

## Instructions 📌

## Make sure you have Firefox installed otherwise it will not work

#### Navigating to your directory. 🔍

To be able to run the commands for this project, you have to be present in the directory containing the files.

Assuming I have the current file structure.

- C: ¬
  - users/ ¬
    - bob/ ¬
      - desktop ¬
        - my_project ¬
          - file_1.py
          - file_2.py
          - file_3.txt
          - file_4.py

Opening your command prompt you can navigate to this project like so.

Current directory `C:/users/bob/` \
Enter the following:

1. `cd desktop`
2. `cd my_project`
3. `code .` This will open the `my_project` folder in vscode.

---

#### Installing dependencies ⚙️

In the directory where your project lies, enter `pip install -r requirements.txt` to install the dependencies needed for this project.

---

#### Running Flask. ⌨️

To run the flask application, enter the following commands in your terminal

1. To tell Flask where our file is do;
   - Windows `set FLASK_APP=flask_app.py`
   - Mac/Linux `export FLASK_APP=flask_app.py`
2. To tell Flask the environment in which run our application will run in do;
   - Windows `set FLASK_ENV=development`
   - Mac/Linux `export FLASK_ENV=development`
3. To start the server

   - `flask run`

4. Once the application is running, navigate to your localhost:5000 by click on the link http://localhost:5000/
   ![Localhost:5000](https://imgur.com/Biq3aLT.png)

5. Enter the website you want to scrape. Please note, you **MUST** enter the **FULL** link.

   - `https://www.google.com` will work.
   - `www.google.com` will **NOT** work.

6. A page will be shown containing the output. Furthermore, a file called content.txt will be generated in the directory also containing the output.

---

#### Running command-line. 💻

Whilst sitting in the directory of your project, enter the following commands based on your python version.

1. `python arg_app.py --web https://www.google.com`
2. `python3 arg_app.py --web https://www.google.com`

A **content.txt** file will be generated containing the content scraped from the page.

---

#### Running Unit-Testing. ✅

Unit-testing ensures that as developers constantly make improvements and changes to existing code aswell as implement new features, that previous features and blocks of code don't suddenly stop working. The webscraper has been built with this in mind.

To run the unit tests execute the command below.

- `python -m pytest` or `python3 -m pytest`
  ![Testing](https://imgur.com/CYByfQT.png)

##### or for a more verbose output do

- `python -m pytest -v` or `python3 -m pytest -v`
  ![Testing](https://imgur.com/5S9yFD1.png)

---

Test
