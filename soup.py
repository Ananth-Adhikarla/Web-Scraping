
import requests 
from bs4 import BeautifulSoup 
import csv 
 
def collect_links():

	i = 2000
	base_url = "http://www.boxofficemojo.com"	
	target_url = "http://www.boxofficemojo.com/studio/?view=company&view2=yearly&yr="+str(i)+"&p=.htm"
	r = []
	
	
	for j in range(0,18):
	
		target_url = 'http://www.boxofficemojo.com/studio/?view=company&view2=yearly&yr='+str(i)+'&p=.htm'
		r.append(requests.get(target_url)) #send request to page
		i += 1

	for i in r:
	
		content = i.content # render content from page
		#print(content)
		soup = BeautifulSoup(content, "html.parser") #parses html tags
		#print(soup)
	

	links = [] 

	for link in soup.findAll('a'):	
		links.append((link.get('href')))
		
	remove_none = [x for x in links if x is not None]
	proper_links = [link for link in remove_none if "?view=company&view2=yearly&yr=" in link]
	full_links = [base_url + link for link in proper_links]
	full_links = sorted(set(full_links))

	return full_links

def clean_up(link):

	
		r = requests.get(link)

		content = r.content 
		#print(content)
		soup = BeautifulSoup(content, "html.parser") 
		#print(soup)
		
		return soup
	
def get_table_header(soup1):
	
	head_list = []
	final_head = []
	trs = soup1.findAll('tr')
	
	for tr in trs:
		if('bgcolor' in tr.attrs and ( tr.attrs['bgcolor'] == '#dcdcdc')):
			for td in tr:
				head_list.append([td.text])
	
	print(head_list)
	del head_list[0]
	del head_list[0]
	del head_list[0]	
	del head_list[6]
	del head_list[6]
	del head_list[6]
	print(head_list)
	
	for word in head_list:

		n = word[0].split("\n")
		final_head.append(*n)	

	#print(final_head[0])

	return final_head


def get_table_data(soup1):
	
	movie_list = []
	final_list = []
	fin_list = []
	trs = soup1.findAll('tr')
	
	for tr in trs:
		if('bgcolor' in tr.attrs and ( tr.attrs['bgcolor'] == '#ffffff' or tr.attrs['bgcolor'] == '#f4f4ff')):
			movie_list.append([tr.text]) 
			
	for word in movie_list:
		n = word[0].split("\n")
		del n[6]
		final_list.append(n)
		#print(final_list)

	return final_list
	

def write_to_csv(x,y):

	r1 = x[0]
	r2 = x[1]
	r3 = x[2]
	r4 = x[3]
	r5 = x[4]
	r6 = x[5]
 	
	with open(' Box_office_bs4.csv', 'a+') as csvfile:
		
		writer = csv.writer(csvfile)
		writer.writerow([r1,r2,r3,r4,r5,r6])
		for i in y:
			writer.writerow(i)
		writer.writerow(" ")


z = collect_links()

for i in z:
	w = clean_up(i)
	x = get_table_header(w)
	y = get_table_data(w)
	write_to_csv(x,y)
	

#print(collect_links())
