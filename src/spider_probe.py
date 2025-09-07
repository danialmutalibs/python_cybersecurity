from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

visited_urls = set()

def spider_urls(url, keyword, depth=0, max_depth=2):
    if url in visited_urls or depth > max_depth:
        return
    visited_urls.add(url)

    try:
        options = Options()
        options.add_argument("--headless")  # run without opening browser
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(2)  # wait for JS to load

        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()
    except Exception as e:
        print(f"Request failed {url}: {e}")
        return

    a_tags = soup.find_all("a")
    for tag in a_tags:
        href = tag.get("href")
        if href:
            new_url = urljoin(url, href)
            if new_url not in visited_urls:
                print(f"Checking: {new_url}")
                if keyword.lower() in new_url.lower():
                    print(f"✅ Found match: {new_url}")
                spider_urls(new_url, keyword, depth + 1, max_depth)

if __name__ == "__main__":
    url = input("Enter the URL you want to scrap: ")
    keyword = input("Enter the keyword to search for: ")
    spider_urls(url, keyword)
