from bs4 import BeautifulSoup
import urllib
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from datetime import date
import time

def main():
    html = urllib.request.urlopen("https://mca-a2.org/").read()
    soup = BeautifulSoup(html, features="html.parser")

    tag = soup.find_all("td", {"class":"begins"})[0]
    fajr = tag.get_text()[:-3]
    tag = soup.find("td", {"colspan":"2"})
    sunrise = tag.get_text()[:-3]
    tag = soup.find_all("td", {"class":"begins"})[1]
    dhuhr = tag.get_text()[:-3]
    tag = soup.find_all("td", {"class":"begins"})[2]
    asr = tag.get_text()[:-3]
    tag = soup.find_all("td", {"class":"begins"})[3]
    maghrib = tag.get_text()[:-3]
    tag = soup.find_all("td", {"class":"begins"})[4]
    isha = tag.get_text()[:-3]
    
    tag = soup.find_all("td", {"class":"jamah"})[0]
    fajrj = tag.get_text()[:-3]
    tag = soup.find_all("td", {"class":"jamah"})[1]
    dhuhrj = tag.get_text()[:-3]
    tag = soup.find_all("td", {"class":"jamah"})[2]
    asrj = tag.get_text()[:-3]
    tag = soup.find_all("td", {"class":"jamah"})[3]
    magrhibj = tag.get_text()[:-3]
    tag = soup.find_all("td", {"class":"jamah"})[4]
    ishaj = tag.get_text()[:-3]

    schedule= date.today().strftime("%m/%d/%y")+"\nf "+fajr+" "+fajrj+"\ns "+sunrise+"\nd "+dhuhr+" "+dhuhrj+"\na "+asr+" "+asrj+"\nm "+maghrib+" "+magrhibj+"\ni "+isha+" "+ishaj
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get("https://dashboard.thelightphone.com/")
    time.sleep(5)
    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB)
    actions.send_keys("email")#INSERT EMAIL
    actions.send_keys(Keys.TAB)
    actions.send_keys("password")#INSERT PASSWORD
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(5)
    actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(3)
    element = driver.find_element(By.CLASS_NAME, "title")
    action = ActionChains(driver)
    action.move_to_element(element).move_by_offset(0,0).click().perform()
    time.sleep(3)
    element = driver.find_elements(By.CLASS_NAME, "title")[1]
    action = ActionChains(driver)
    action.move_to_element(element).move_by_offset(0,0).click().perform()
    time.sleep(3)
    element = driver.find_elements(By.CLASS_NAME, "pointer")[9]
    action.move_to_element(element).move_by_offset(0,0).click().perform()
    time.sleep(3)
    element = driver.find_elements(By.CLASS_NAME, "py1")[1]
    action.move_to_element(element).move_by_offset(0,0).click().perform()
    time.sleep(3)
    element = driver.find_elements(By.CLASS_NAME, "ml1")[0]
    action.move_to_element(element).move_by_offset(0,0).click().perform()
    time.sleep(3)
    element = driver.find_element(By.CLASS_NAME, "ember-text-area")
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)
    element.send_keys(schedule)
    time.sleep(3)
    element = driver.find_elements(By.CLASS_NAME, "Button--hollow")[0]
    action.move_to_element(element).move_by_offset(0,0).click().perform()
    time.sleep(3)

if __name__ == "__main__":
    main()

