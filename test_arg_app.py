import pytest
import arg_app

#--------------TESING argsparse--------------
def test_get_args():
    parser = arg_app.get_args(['--web','Testing'])
    assert parser.web == 'Testing'

def test_get_args_false():
    parser = arg_app.get_args(['--web','One'])
    assert not parser.web == 'Two'
    
#--------------TESING get_content FUNCTION--------------
def test_get_content_with_working_website():
    """
    Test should pass when a correct link is providing
    
    >>> arg_app.get_content("https://www.google.co.uk") 
    "About Store GmailImages Sign in   United Kingdom Advertising Business How Search works Carbon neutral since 2007 Privacy Terms Settings Before you continue to Google Search Google uses cookies and data to: Deliver and maintain services, like tracking outages and protecting against spam, fraud and abuse Measure audience engagement and site statistics to understand how our services are used If you agree, we’ll also use cookies and data to: Improve the quality of our services and develop new ones Deliver and measure the effectiveness of ads Show personalised content, depending on your settings Show personalised or generic ads, depending on your settings, on Google and across the web For non-personalised content and ads, what you see may be influenced by things like the content that you’re currently viewing and your location (ad serving is based on general location). Personalised content and ads can be based on those things and your activity, like Google searches and videos that you watch on YouTube. Personalised content and ads include things like more relevant results and recommendations, a customised YouTube homepage, and ads that are tailored to your interests. Click 'Customise' to review options, including controls to reject the use of cookies for personalisation and information about browser-level controls to reject some or all cookies for other uses. You can also visit g.co/privacytools at any time. Customise I agree Privacy · Terms"
    
    Passing in a link without https should throw an error
    
    >>> arg_app.get_content("www.google.co.uk")         
    Please enter a valid link
    
    Passing in a fake link should throw an error
    
    >>> arg_app.get_content("https://www.fgdfg54.co.uk") 
    Please enter a valid link

    """
    url = "https://www.google.co.uk"
    content = arg_app.get_content(url)
    assert content

def test_get_content_with_invalid_website():
    url = "https://www.dfasdf.co.uk"
    content = arg_app.get_content(url)
    assert content == None