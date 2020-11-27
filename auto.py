from selenium import webdriver
import time

i=0
n=5
while i < n:
    i+=1
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com')

    searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
    searchbox.send_keys("creativ cuckoo")

    searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
    searchbutton.click()
    time.sleep(3)

    channelicon = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-renderer[1]/div/div[1]/a')
    channelicon.click()
    time.sleep(3)

    channelvid = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-shelf-renderer/div[1]/div[1]/div/h2/div[2]/ytd-button-renderer/a/paper-button')
    channelvid.click()
    
    time.sleep(20)
    driver.close()