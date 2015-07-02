##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################


import csv
import pandas as pd 

import sys, os
import csv
import pandas as pd 

# Set File Name
Text_File = "../iw.txt"
File = str(Text_File)

def clean_contacts(infile):
	"""This function takes a text file of raw existing faculty and staff and cleans
	the data to searchable entries."""

	infile = open(File, 'rU')
	outfile = open('../cleaned_contacts.csv', 'w')

	reader = infile.read()
	#reader = csv.reader(infile, delimiter=',')
	writer = csv.writer(outfile, delimiter=',')

	for line in reader:
			#print line
			#line0 = str(line)
			line1 = line.replace('\n', ' ').replace('\r', ' ')
			print line1
			#line2 = line1.replace('[', '').replace(']', '').replace("'", '')
			#print line2
			#writer.writerow([line2])

	#infile.close()
	#outfile.close()

#clean_contacts(File)


# Set CSV File Name
CSV_File = "../iw.csv"
CSV = str(CSV_File)

def clean_contacts2(infile):
	"""This function takes a CSV of existing scholars CSV text files and department
	and converts it to a cleaned CSV of departments and scholar names."""

	infile = open(CSV, 'rU')
	outfile = open('../cleaned_contacts2.csv', 'w')

	reader = csv.reader(infile)
	writer = csv.writer(outfile)

	for line in reader:
			line0 = str(line)
			#print line0
			line1 = line0.replace("[',", "*break*").replace('[]', '').replace("['", '').replace("']", '')
			#print line1
			line2 = line1.replace('\n', '').replace('\r', '').replace('\n\r', '').replace("*break*", '|')
			print line2
			writer.writerow([line2])

	infile.close()
	outfile.close()

clean_contacts2(CSV)

def clean_contacts3(infile):
	"""This function takes a CSV of existing scholars CSV text files and department
	and converts it to a cleaned CSV of departments and scholar names."""

	#Define Data
	data = pd.read_csv(infile, index_col=0)
	#infile = open(CSV, 'rU')
	#outfile = open('../cleaned_contacts.csv', 'w')

	transdf = data.transpose()
	print transdf


	transdf.to_csv("pandas_clean.csv", encoding='utf-8')

	#reader = csv.reader(infile)
	#writer = csv.writer(outfile)

	#for line in reader:
			#line0 = str(line)
			#print line0
			#line1 = line0.replace('\r\n', '')
			#print line1
			#line2 = line1.replace('[', '').replace(']', '').replace("'", '')
			#print line2
			#writer.writerow([line2])

	#infile.close()
	#outfile.close()

clean_contacts3("../cleaned_contacts2-head.csv")