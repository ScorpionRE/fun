from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import random
import xlrd

brower=webdriver.Chrome('D:/ctf/chromedriver.exe')
brower.implicitly_wait(3)
brower.set_window_size(452,790)

def like(words):
	brower.get("https://passport.weibo.cn/signin/login")

	elem = brower.find_element_by_xpath("//*[@id='loginName']")
	elem.send_keys("your own username")
	elem = brower.find_element_by_xpath("//*[@id='loginPassword']")
	elem.send_keys("your own password")
	elem = brower.find_element_by_xpath("//*[@id='loginAction']")
	elem.send_keys(Keys.ENTER)
	time.sleep(10)
	brower.get("https://m.weibo.cn/detail/... ")
	
	while True:
		try:
			for x in range(0,999,1):
				target = brower.find_elements_by_xpath("//*[@class='lite-iconf lite-iconf-like']/../../..")
				brower.execute_script('arguments[0].scrollIntoView();',target[x])
				m = target[x].text
				if m.find(words) != -1:
					print(m)
					time.sleep(1)
					like = brower.find_elements_by_xpath("//*[@class='lite-iconf lite-iconf-like']")
					like[x].click()
				
						
		except:
			brower.execute_script('window.scrollBy(0,50)')
		time.sleep(3)


def huati(keyword):
	for x in range(0,999,1):
		brower.get("https://s.weibo.com")
		elem = brower.find_element_by_xpath("//*[@class='search-input']/input")
		elem.send_keys(keyword)
		elem = brower.find_element_by_xpath("//*[@class='s-btn-b']")
		ActionChains(brower).move_to_element(elem).click().perform()
		time.sleep(3)
	






if __name__ == '__main__':
	like("关键词")
	#huati("话题")