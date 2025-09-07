from selenium import webdriver
from selenium.webdriver.chrome.service import Service

cdp = r"C:/Users/user/Desktop/python_cybersecurity/src/chromedriver.exe"
service = Service(executable_path=cdp)

driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
driver.quit()
