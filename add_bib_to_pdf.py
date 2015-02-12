 #!/usr/bin/env python

import os as os
import requests
from tkinter import *

file_name_string = "Y1"

os.chdir("/home/nick/kindle_papers/")

os.system("pdftotext %s.pdf"%file_name_string)
with open (file_name_string+".txt","r") as tfile:
	txt_file = tfile.read()

def find_doi():
	doi = "NULL"
	for item in txt_file.split("\n"):
		if 'doi' in item:
			print(item)
			doi = item.split(' ')[1]
		elif 'DOI' in item:
			print(item)
			doi = item.split(' ')[1]
	return(doi)

def get_ref(doi):
	url = "http://www.doi2bib.org/#/doi/{id}".format(id=doi)
	xhr_url = "http://www.doi2bib.org/doi2bib"
	with requests.Session() as session:
		session.get(url)
		response = session.get(xhr_url, params={'id': doi})
		cite = response.content
	return(cite)

def init_cite_dict():
	cite_dict = {}
	cite_dict['title'] = " NA "
	cite_dict['author'] = " NA "
	cite_dict['year'] = " 0000 "
	cite_dict['number'] = " NA "
	cite_dict['label'] = " NA "
	cite_dict['journal'] = " NA "
	cite_dict['pages'] = " NA "
	cite_dict['doi'] = " NA "
	cite_dict['publisher'] = " NA "
	cite_dict['volume'] = " NA "
	cite_dict['organisation'] = " NA "
	return(cite_dict)

def create_dict_from_web(cite, cite_dict):
	cite = cite.decode("utf-8").split('\n\t')
	cite[0] = 'label = '+cite[0]
	for line in cite:
		cite_dict[line.split(' = ')[0]] = line.split(' = ')[1]
	print(cite_dict.keys())
	return(cite_dict)

def fetch(entries, cite_dict):
	for entry in entries:
		field = entry[0]
		text  = entry[1].get()
		text = text.replace('\n', ' ')
		cite_dict[field] = text

def makeform(root, fields):
	entries = []
	for field in fields:
		row = Frame(root)
		lab = Label(row, width=15, text=field, anchor='w')
		ent = Entry(row)
		row.pack(side=TOP, fill=X, padx=5, pady=5)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT, expand=YES, fill=X)
		ent.insert(0, " NA ")
		entries.append((field, ent))
	return entries

##### some class that is the gui
def create_dict_from_gui(cite_dict):
	print("starting Gui")
	txt_window = Tk()
	S = Scrollbar(txt_window)
	T = Text(txt_window, height=50, width=100)
	S.pack(side=RIGHT, fill=Y)
	T.pack(side=LEFT, fill=Y)
	S.config(command=T.yview)
	T.config(yscrollcommand=S.set)
	T.insert(END, txt_file)


	fields ='label', 'title', 'author', 'year', 'journal', 'organisation', 'publisher', 'pages', 'volume', 'number',
	input_form = Tk()
	ents = makeform(input_form, fields)
	input_form.bind('<Return>', (lambda event, e=ents: fetch(e, cite_dict)))
	b1 = Button(input_form, text='Save', command=(lambda e=ents: fetch(e, cite_dict)))
	b1.pack(side=LEFT, padx=5, pady=5)
	b2 = Button(input_form, text='Quit', command=input_form.quit)
	b2.pack(side=LEFT, padx=5, pady=5)

	txt_window.mainloop()
	input_form.mainloop()


	#window pops up with doi search at top (search), and rest of input boxes below, (submit).
	#input_boxes = Tk()

	return(cite_dict)

def rename_pdf(cite_dict):
	pdf_name = cite_dict['title'][1:-2] + ' ' + cite_dict['year'][:-1] + ' ' + cite_dict['author'][1:-2]
	pdf_name = pdf_name.replace(' ', '\ ')
	if len(pdf_name) > 252:
		pdf_name = pdf_name[:(252-len(pdf_name))]
	pdf_name = pdf_name + '.pdf'
	return(pdf_name)

def update_pdf_meta(cite_dict):
	print("updateing pdf metadata")
	os.system('exiftool -Author=%s G1.pdf'%("'"+'author = '+cite_dict['author'] +"'"))
	os.system('exiftool -Number=%s G1.pdf'%("'"+'issue = '+cite_dict['number'] +"'"))
	os.system('exiftool -UserComment=%s G1.pdf'%("'"+'label = '+cite_dict['label'] +"'"))
	os.system('exiftool -Subject=%s G1.pdf'%("'"+'journal = '+cite_dict['journal'] +"'"))
	os.system('exiftool -SerialNumber=%s G1.pdf'%("'"+'pages = '+cite_dict['pages'] +"'"))
	os.system('exiftool -DOI=%s G1.pdf'%("'"+'doi = '+cite_dict['doi'] +"'"))
	os.system('exiftool -Publisher=%s G1.pdf'%("'"+'publisher = '+cite_dict['publisher'] +"'"))
	os.system('exiftool -Volume=%s G1.pdf'%("'"+'volume = '+cite_dict['volume'] +"'"))
	os.system('exiftool -Title=%s G1.pdf'%("'"+'title = '+cite_dict['title'] +"'"))
	os.system('exiftool -Date=%s G1.pdf'%("'"+'year = '+cite_dict['year'] +"'"))
	os.system('exiftool -Notes=%s G1.pdf'%("'"+'organisation = '+cite_dict['organisation'] +"'"))

def add_to_bib(cite_dict):
	#adds cite_dict info to .bib file
	print("adding cite to .bib file")

def move_pdf(pdf_name):
	os.system('cp %s.pdf %s'%(file_name_string ,pdf_name))
	print("moving pdf")

doi = find_doi()
cite_dict = init_cite_dict()
if doi != "NULL":
	cite = get_ref(doi)
	if cite == 'Invalid DOI':
		cite_dict = create_dict_from_gui(cite_dict)
	else:
		cite_dict = create_dict_from_web(cite, cite_dict)

else:
	cite_dict = create_dict_from_gui(cite_dict)

#kill all tinker windows here

### create a class called cite_dictionary then use init_cite_dict as __init__ function,
### then use the def's as operations on the instance cite_dict of teh class cite_dictionary

print(cite_dict)
pdf_name = rename_pdf(cite_dict)
update_pdf_meta(cite_dict)
move_pdf(pdf_name)
##### dont forget to delete the .txt file #####