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
	#outfile = open('../cleaned_contacts.csv', 'w')
	#outfile = open('../CLEAN_DATA.csv', 'w')

	reader = infile.read()
	#reader = csv.reader(infile, delimiter=',')
	writer = csv.writer(outfile, delimiter='*')

	for line in reader:
			#print line
			line0 = str(line)
			line1 = line0.replace('\n', ' ').replace('\r', ' ')
			#print line1
			#line2 = line1.replace('[', '').replace(']', '').replace("'", '')
			#print line2
			writer.writerow([line1])

	infile.close()
	outfile.close()

#clean_contacts(File)
#clean_contacts("../CLEAN_CONTACTS.txt")


# Set CSV File Name
CSV_File = "../iw.csv"
CSV = str(CSV_File)

def clean_contacts2(infile):
	"""This function takes a CSV of existing scholars CSV text files and department
	and converts it to a cleaned CSV of departments and scholar names."""

	infile = open(CSV, 'rU')
	outfile = open('../cleaned_contacts2_new.csv', 'w')
	#outfile = open('../CLEAN_DATA.csv', 'w')	

	reader = csv.reader(infile)
	writer = csv.writer(outfile)

	for line in reader:
			line0 = str(line)
			#print line0
			line1 = line0.replace("[',", "*break*").replace('[]', '').replace("['", '').replace("']", '').replace(',', '').replace(' -', '')
			# For whichever reason text such as "\x0c" would not replace. These were resolved using Excel's find and replace feature. This was done following the work done in this function.
			#print line1
			line2 = line1.replace('\n', '').replace('\r', '').replace('\n\r', '').replace("*break*", '|')
			print line2
			writer.writerow([line2])

	infile.close()
	outfile.close()

#clean_contacts2(CSV)
#clean_contacts2("../CLEAN_CONTACTS.txt")



# For whichever reason text such as "\x0c" would not replace. These were resolved using Excel's find and replace feature. This was done following the work done in this function.
# Using excel, I replaced:
# "\x0c" with "|"
# "|," with "|"
# "\xa5" with ""
# "\xd0" with ""
# "\xd5s" with ""
# "\x8e" with "e"
# "\x90" with "e"
# "\x97" with "o"
# "\x99" with "o"
# "\x8d" with "c"
# "\xd5" with "'"
# "\xd9" with "u"
# "\x94" with "i"
# "\x92" with "i"
# "\x95" with "i"
# "\x9f" with "u"
# "\x96" with "n"
# "\x89" with "a"
# "," with ";"




def df_split(infile):

	#Define Data (Full Cleaned Data)
	df = pd.read_csv(infile, index_col=0, header=None)

	
	"""
	#df1, df2 = df[:1000, :], df[1000:2000, :]
	#Was working with cleaned_data2.csv
	df1, df2 = df[0:10001], df[10001:20000]
	df3, df4 = df[20000:29998], df[29998:39998]
	df5, df6 = df[39998:49998], df[50000-1:60000-1]
	df7, df8 = df[60000-1:70000-1], df[70000-1:80000-1]
	df9, df10 = df[80000-1:90000-1], df[90000-1:]
	"""

	
	df1, df2 = df[0:9996], df[9996:19999]
	df3, df4 = df[19999:29994], df[29994:39992]
	df5, df6 = df[39992:50000], df[50000:59999]
	df7, df8 = df[59999:69998], df[69998:79994]
	df9 = df[79994:90000]
	


	dfs_names = ['df1', 'df2', 'df3', 'df4', 'df5', 'df6', 'df7', 'df8', 'df9', 'df10']
	dfs = [df1, df2, df3, df4]


	#Generate Commands
	for dfn in dfs_names:

		#filename = "../"+str(df)".csv"
		cmd = str(dfn)+".to_csv("+'"'+"../"+str(dfn)+".csv"+'"'+", encoding='utf-8', header=0)"
		#print cmd 

	print "Writing files..."

	df1.to_csv("../df1.csv", encoding='utf-8', header=0)
	df2.to_csv("../df2.csv", encoding='utf-8', header=0)
	df3.to_csv("../df3.csv", encoding='utf-8', header=0)
	df4.to_csv("../df4.csv", encoding='utf-8', header=0)
	df5.to_csv("../df5.csv", encoding='utf-8', header=0)
	df6.to_csv("../df6.csv", encoding='utf-8', header=0)
	df7.to_csv("../df7.csv", encoding='utf-8', header=0)
	df8.to_csv("../df8.csv", encoding='utf-8', header=0)
	df9.to_csv("../df9.csv", encoding='utf-8', header=0)
	#df10.to_csv("../df10.csv", encoding='utf-8', header=0)

	print "All files written."

df_split("../IW_DATA.csv")
#df_split("../IW_DATA_test.csv")
#df_split("../cleaned_contacts2_new.csv")

#This might need to be added before the header step
#Add headers to python in Excel
#


def clean_contacts3(infile):
	"""This function takes a CSV of existing scholars CSV text files and department
	and converts it to a cleaned CSV of departments and scholar names."""

	#Define Data
	data = pd.read_csv(infile, index_col=0, header=None)
	#infile = open(CSV, 'rU')
	#outfile = open('../cleaned_contacts.csv', 'w')

	transdf = data.transpose()
	#print transdf

	#Used originally
	#transdf.to_csv("../pandas_clean_new.csv", encoding='utf-8')
	transdf.to_csv("../pandas_df1.csv", encoding='utf-8')


#clean_contacts3("../cleaned_contacts2-head_new.csv")
clean_contacts3("../df1.csv")



def convert_trans_df(infile):

	#Define Data
	data = pd.read_csv(infile, delimiter='|')
	#infile = open(CSV, 'rU')
	#outfile = open('../cleaned_contacts.csv', 'w')

	# data
	transdf = data.transpose()
	#print transdf

	#Used originally
	#transdf.to_csv("../pandas_One_Name_Per_Row_new.csv", encoding='utf-8')
	transdf.to_csv("../pandas_df1_One_Name_Per_Row.csv", encoding='utf-8')


#convert_trans_df("../pandas_clean_new.csv")
convert_trans_df("../pandas_df1.csv")

##So even this way, I seem to be getting about 1/5 of the rows. There should be 10,000 not 2,000 or 1,000.

## I might have to break up the CSV prior to the transpose into say 5-10 smaller spreadsheets.
## 


