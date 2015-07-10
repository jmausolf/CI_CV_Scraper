##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################


import csv, re


def master_name_extract(file_):

	filename = "../"+file_+".csv"
	infile = open(filename, 'rU')
	outfile = open("../__CLEANED_"+file_+".csv", 'w')	

	reader = csv.reader(infile)
	writer = csv.writer(outfile)

	print "Cleaning merged file..."
	for line in reader:
			line0 = str(line)
			line1 = line0.replace(',', ' ').replace(';', ' ').replace("['", '').replace("']", '').replace('["', '').replace('"]', '').replace(' ', '', 1)

			# Split Into Groups
			n = 2
			groups = line1.split(' ')
			names = ' '.join(groups[:n]), ' '.join(groups[n:])

			line2 = str(names)
			line3 = line2.replace("'", '').replace('(', '').replace(')', '').replace('"', '').replace(', ', ' ,')

			writer.writerow([line3])

	infile.close()
	outfile.close()


#Unhash to run
#master_name_extract("CVs__MISSING")



def tester(file_):
	"""This file is used for testing CSVs for python capatability
	and doing minor bulk modifications for later editing in excel"""

	filename = "../"+file_+".csv"
	infile = open(filename, 'rU')
	outfile = open("../__LOWER_"+file_+".csv", 'w')	

	reader = csv.reader(infile)
	writer = csv.writer(outfile)

	print "Cleaning merged file..."
	for line in reader:
			line0 = str(line)
			line1 = line0.replace(';', ' ').replace("['", '').replace("']", '').replace('["', '').replace('"]', '').replace("'", '').replace(' ', '', 1)
			
			line2 = line1.lower()
			line2 = line1.title()
			print line2
			#writer.writerow([line1])
			writer.writerow([line2])

	infile.close()
	outfile.close()


#Unhash to run
#tester("EDIT__CLEANED_CVs__MISSING")
#tester("Bowen_Names")
tester("Only_Existing_UC_Names")
#tester("EDITED__CLEANED_CVs__MISSING")
#tester("EDITED__CLEANED_CVs__MISSING")


