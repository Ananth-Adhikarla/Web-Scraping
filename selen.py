import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Firefox, FirefoxProfile
import csv

url = "http://www.boxofficemojo.com/studio/"
driver = webdriver.Firefox()
driver.wait = WebDriverWait(driver, 5)
movie_list = []
movie_text = []

def looping_pages():
	for i in range(2000,2018):
		print("Currently processing year : ", i )
		if( i == 2017 ):
			driver.get("http://www.boxofficemojo.com/studio/")
			link = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table[3]/tbody/tr/td[1]/table/tbody')
	
			for tr in link.find_elements_by_xpath('.//tr'):
				td =  tr.text
				movie_list.append([td])
			
			time.sleep(5)
		else:
			driver.get(url)
			button = driver.find_element_by_link_text(str(i)).click()
			link = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/table[3]/tbody/tr/td[1]/table/tbody')
	
			for tr in link.find_elements_by_xpath('.//tr'):
				td =  tr.text
				movie_list.append([td])

			time.sleep(5)

	return movie_list	

def creating_list(text):

	print(text)	
	for j in text:
		m = j[0].split(" ")
		if( len(m) == 6 ):
			print(m)
			movie_text.append(m)		
		if( len(m) == 7):
			m[1] = m[1]+' '+m[2]
			m[2] = m[3]
			m[3] = m[4]
			m[4] = m[5]
			m[5] = m[6]
			del m[6]
			print(m)
			movie_text.append(m)
		if( len(m) == 8):
			m[1] = m[1]+' '+m[2]+' '+m[3]
			m[2] = m[4]
			m[3] = m[5]
			m[4] = m[6]
			del m[5]
			del m[6]
			print(m)
			movie_text.append(m)
						
		
	return movie_text

def write_to_csv():

	count = 0
	with open('Box_office_selenium.csv', 'a+') as csvfile:
		
		writer = csv.writer(csvfile)
	
		for i,j in enumerate(movie_text):
			count += 1
			writer.writerow(j)
			
		writer.writerow(" ")

	print("Total number of records processed : ",count)
print(looping_pages())
#creating_list(x)
#write_to_csv()

