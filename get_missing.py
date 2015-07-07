##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################


import csv, re
import pandas as pd 



def phone_number_scrubber(file_):
	"""In the original cleaned directory list, phone numbers were widely situated between names, e.g. Dr. Foo (XXX) XXX-XXXX Bar. This function removes the phone numbers to provide a complete uninterrupted word string, e.g. Dr. Foo Bar."""

	filename = "../"+file_+".csv"
	infile = open(filename, 'rU')
	outfile = open("../"+file_+"_Phone_Removed_Cleaned.csv", 'w')	

	reader = csv.reader(infile)
	writer = csv.writer(outfile)

	print "Cleaning merged file..."
	for line in reader:
			line0 = str(line)
			line1 = line0.replace(',', ' ').replace(';', ' ').replace("['", '').replace("']", '')
			phonePattern = re.compile("\d?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4})")
			result = phonePattern.sub(lambda m: re.sub('\d', 'X', m.group(1)), line1)
			writer.writerow([result])

	infile.close()
	outfile.close()

#Unhash to run
post_merge_clean("__faculty")