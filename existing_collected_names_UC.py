##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################


import csv
import pandas as pd 


# Set CSV File Name
CSV_File = "../UC-CVs.csv"
CSV = str(CSV_File)

def read_CSV(i, CSV):
	"""Reads the CSV Data for a Given Line i"""
	with open(str(CSV), 'rU') as data_file:
		reader = csv.reader(data_file)
		lines = list(reader)
		output = lines[i]
		return output


def writeExistingNames(infile):
	"""This function takes a CSV of existing scholars CSV text files and department 
	and converts it to a cleaned CSV of departments and scholar names."""

	infile = open(CSV, 'rU')
	outfile = open('../Existing_UC_Names.csv', 'w')

	reader = csv.reader(infile, delimiter=',')
	writer = csv.writer(outfile, delimiter=',')

	for line in reader:
			line0 = str(line)
			line1 = line0.replace('_', ' ').replace('.txt', '').replace('.docx', '').replace('.doc', '').replace('.pdf', '')
			#print line1
			line2 = line1.replace('[', '').replace(']', '').replace("'", '')
			#print line2
			writer.writerow([line2])

	infile.close()
	outfile.close()

#Unhash to test
writeExistingNames(CSV)


def Get_Names_Only(infile):
	"""This function takes a CSV of existing scholars CSV text files and department 
	and converts it to a cleaned CSV of only scholar names."""


	infile = open(CSV, 'rU')
	outfile = open('../Only_Existing_UC_Names.csv', 'w')

	reader = csv.reader(infile, delimiter=',')
	writer = csv.writer(outfile, delimiter=',')

	for line in reader:
			line0 = str(line)
			line1 = line0.replace('_', ' ').replace('.txt', '').replace('.docx', '').replace('.doc', '').replace('.pdf', '')
			line2 = line1.replace('[', '').replace(']', '').replace("'", '')
			line3 = line2.split(',')[1]
			writer.writerow([line3])

	infile.close()
	outfile.close()

#Unhash to test
Get_Names_Only(CSV)



