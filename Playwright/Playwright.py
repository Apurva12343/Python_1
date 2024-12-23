import re
from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=2000)
    page = browser.new_page()
    page.goto("https://playwright.dev/python/")
    #click on a link by name of the link
    docs = page.get_by_role("link",name="Docs")
    docs.click()
    #to get the url of the clicked link
    print("docs: ",page.url)
    browser.close()