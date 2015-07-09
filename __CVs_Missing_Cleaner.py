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
			#names = re.split("/\b([A-Z]{1}[a-z]{1,30}[- ]{0,1}|[A-Z]{1}[- \']{1}[A-Z]{0,1} [a-z]{1,30}[- ]{0,1}|[a-z]{1,2}[ -\']{1}[A-Z]{1}[a-z]{1,30}){2,5}/", '"^[a-zA-Z0-9_.-]+$"', 3)
			#names = re.split("^[a-zA-Z0-9_.-]+$", " ", 2)

			#result = names.sub(lambda m: re.sub('/\b', '*', m.group(1)), line1)
			n = 2
			groups = line1.split(' ')
			names = ' '.join(groups[:n]), ' '.join(groups[n:])

			line2 = str(names)
			line3 = line2.replace("'", '').replace('(', '').replace(')', '').replace('"', '')

			#names = line1.split(' ', 4)

			# So manipulate the name, string, split to columns, import on delimiter and then maybe try to split after .edu

			#writer.writerow([line1])
			writer.writerow([line3])

	infile.close()
	outfile.close()


#Unhash to run
master_name_extract("CVs__MISSING")



