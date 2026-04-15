#   Instructions:
#   1. Create a credentials.txt with your email on line 1 and password on line 2.
#   2. Install dependencies:
#       pip install playwright
#       playwright install chromium
#   3. Run the script and solve the CAPTCHA when prompted.
#------------------

import os
import re
import time
from playwright.sync_api import sync_playwright

# Credentials
with open("credentials.txt") as f:
    USERNAME, PASSWORD = f.read().strip().splitlines()[:2]

# Configuration
LOGIN_URL = "https://dcon26.mapyourshow.com/8_0/login/login.cfm"
GALLERY_URL = "https://dcon26.mapyourshow.com/8_0/explore/session-gallery.cfm"

DOWNLOAD_DIR = "Conference_Papers"

SESSION_LINK_SELECTOR = ".bb-0.color-inherit"
HANDOUT_SELECTOR = "li.o-List_Columns_Item a"


def slugify(text):
    return re.sub(r'[\\/*?:"<>|]', "", text).strip('.')

def run(playwright):

    # Browser
    browser_main = playwright.chromium.launch(headless=False,timeout=50000)

    browser = browser_main.new_context(
        viewport={'width': 1800, 'height': 900},
        accept_downloads=True,
        )
    page = browser.new_page()
    page.set_default_navigation_timeout(50000)

    # Login
    page.goto(LOGIN_URL, wait_until="domcontentloaded")
    time.sleep(1)
    page.get_by_role("textbox").fill(USERNAME)

    input("Fill in CAPTCHA, press continue on browser, then press ENTER here: ... ")

    page.get_by_role("textbox").fill(PASSWORD)
    page.locator(".btn-v2.primary").click()

    # Find sessions
    page.goto(GALLERY_URL, wait_until="domcontentloaded")
    page.get_by_text("See All Results").click()

    input("Scroll to bottom to load all sessions. Then press ENTER here: ... ")

    session_links = page.locator(SESSION_LINK_SELECTOR)
    count = session_links.count()

    for i in range(count):
        current_link = page.locator(SESSION_LINK_SELECTOR).nth(i)
        title = slugify(current_link.inner_text())
        session_dir = os.path.join(DOWNLOAD_DIR, title)
        if not os.path.exists(session_dir):
            os.makedirs(session_dir)
        print(f"[{i+1}/{count}] Opening: {title}")
        with browser.expect_page() as page_two_info:
            current_link.click(button="middle")
        page_two = page_two_info.value
        page_two.bring_to_front()
        time.sleep(1)

        if(page_two.get_by_role("button", name="Okay, Got it!").is_visible()):
            page_two.get_by_role("button", name="Okay, Got it!").click()
            time.sleep(1)

        resources_tab = page_two.get_by_role("tab", name="resources")
        if resources_tab.is_visible():
            resources_tab.click()
            time.sleep(1)

        handout_links = page_two.locator(HANDOUT_SELECTOR)
        if (handout_links.count()>0):
            for j in range(handout_links.count()):
                paper_linky = "https://dcon26.mapyourshow.com" + handout_links.nth(j).get_attribute("href")
                paper_name = slugify(handout_links.nth(j).inner_text()) + ".pdf"
                paper = browser.request.get(paper_linky)
                with open(os.path.join(session_dir, paper_name), "wb") as f:
                    f.write(paper.body())
                paper.dispose()
                print(f"  Saved: {paper_name}")

        time.sleep(1)
        page_two.close()

    page.close()
    browser.close()

    # Cleaning
    for d in os.listdir(DOWNLOAD_DIR):
        path = os.path.join(DOWNLOAD_DIR, d)
        if os.path.isdir(path) and not os.listdir(path):
            os.rmdir(path)
            print(f"Deleted empty folder: {d}")

if __name__ == "__main__":
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    with sync_playwright() as playwright:
        run(playwright)
