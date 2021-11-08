#Importing
import sys
import os
import argparse
from selenium import webdriver
from selenium.webdriver.firefox.options import Options #To make browser headless(Run in background)
from get_gecko_driver import GetGeckoDriver

def get_args(args):
    parser = argparse.ArgumentParser(description='A tutorial of argparse!')
    parser.add_argument("--web", required=True, type=str, help= "Enter the full link of the website")
    return parser.parse_args(args)


def get_content(URL):
    #Pulling in the latest chromedriver
    get_driver = GetGeckoDriver()
    get_driver.install()
    
    #Setting up the driver path and options
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    #Loading the website
    try:
        driver.get(URL)
        content = driver.find_element_by_tag_name("body").get_attribute("innerText")
        content =  content.replace('\n',' ')
        driver.quit()
        return content
    except Exception as e:
        print("Please enter a valid link")
  
    
def save_content(text):
    #Save the text content of the webpage to a file.
    with open("content.txt", 'w+') as w:
        w.write(text)
    
    #print(text)

def main():
    URL = get_args(sys.argv[1:])
    content = get_content(URL.web)
    save_content(content)

if __name__ == "__main__":
    main()