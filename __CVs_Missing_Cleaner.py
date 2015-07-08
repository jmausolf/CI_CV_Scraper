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
	outfile = open("../__CLEANED"+file_+".csv", 'w')	

	reader = csv.reader(infile)
	writer = csv.writer(outfile)

	print "Cleaning merged file..."
	for line in reader:
			line0 = str(line)
			line1 = line0.replace(',', ' ').replace(';', ' ').replace("['", '').replace("']", '')
			names = re.split("/\b([A-Z]{1}[a-z]{1,30}[- ]{0,1}|[A-Z]{1}[- \']{1}[A-Z]{0,1} [a-z]{1,30}[- ]{0,1}|[a-z]{1,2}[ -\']{1}[A-Z]{1}[a-z]{1,30}){2,5}/", 'de', 2)
			#names = re.split("^[a-zA-Z0-9_.-]+$", " ", 2)

			#result = names.sub(lambda m: re.sub('/\b', '*', m.group(1)), line1)
			#result = line1.split(' ', 3)

			# So manipulate the name, string, split to columns, import on delimiter and then maybe try to split after .edu

			writer.writerow([names])

	infile.close()
	outfile.close()


#Unhash to run
master_name_extract("CVs__MISSING")



