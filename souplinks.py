
import requests # helps in sending HTTP requests to a webpage
from bs4 import BeautifulSoup # pulls data out of HTML files
import csv #helps read/write form CSV's

base_url = "http://www.boxofficemojo.com"
#target_url = 'http://www.boxofficemojo.com/studio/?view=company&view2=yearly&yr=2017&p=.htm'
r = []
i = 2000
for j in range(0,18):
	
	target_url = 'http://www.boxofficemojo.com/studio/?view=company&view2=yearly&yr='+str(i)+'&p=.htm'
	r.append(requests.get(target_url)) #send request to page
	i += 1
	#print(r)
	

#print(r)



for i in r:

	content = i.content # render content from page
	#print(content)
	soup = BeautifulSoup(content, "html.parser") #parses html tags
	#print(soup)
	

links = [] #create an empty list 
def collect_links():
	for link in soup.findAll('a'):	
		links.append((link.get('href')))
		
	remove_none = [x for x in links if x is not None]
	proper_links = [link for link in remove_none if "?view=company&view2=yearly&yr=" in link]
	full_links = [base_url + link for link in proper_links]
	full_links = sorted(set(full_links))

	return(full_links)

def write_to_csv():
	with open(' Box_office_llink.csv', 'w') as csvfile:
		fieldnames = ['links']
		writer = csv.writer(csvfile)
		writer.writerow(fieldnames)# writing "links" in column header
		for i in collect_links():
			writer.writerow([i])

write_to_csv()



#print(collect_links())
