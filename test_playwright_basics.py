import time

from playwright.sync_api import Page
def test_browser_basic(playwright): #this code is basic one used to invoke any chromium browser. using playwright fixture
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com//")

#page fixture ko use kr rhe h jo Page class se aarha h and
# browser invokation ho rha without specifying browser, context, page.
#suggestion for page..... is coming from this Page class
#to run below code in ui use --headed

def test_browser_shortcut(page:Page):
    page.goto("https://rahulshettyacademy.com//")


def test_corelocator(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise//")
    page.get_by_label("Username").fill("rahulshettyacademy")#make sure input tag is in label tag or there is for - id relation
    page.get_by_label("Password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").click()
    page.get_by_role("link", name="terms and conditions").click()#will look for link with name specified
    page.get_by_role("button", name="Sign In").click()#will look for button with name specified
    time.sleep(5000)

