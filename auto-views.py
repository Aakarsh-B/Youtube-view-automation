from selenium import webdriver
import time

i=0
n=5
while i < n:
    i+=1
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com/channel/UCTAkHQQ0y1gA0rZanPjdzYQ')

    channelvid = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-shelf-renderer/div[1]/div[1]/div/h2/div[2]/ytd-button-renderer/a/paper-button')
    channelvid.click()
    
    time.sleep(20)
    driver.close()
