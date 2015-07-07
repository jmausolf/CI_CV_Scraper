##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################


import csv, re
import pandas as pd 


def merge_files(args, filename):

	#Unwrap arguments
	argument_list = args

	frame = pd.DataFrame()
	list_ = []

	#Loop over variable arguments
	for file_ in argument_list:
	    df = pd.read_csv(file_,index_col=0, header=None)
	    list_.append(df)
	frame = pd.concat(list_)
	write_file = "../MERGED_"+str(filename)+".csv"
	print "Writing merged file... ", write_file
	frame.to_csv(write_file, encoding='utf-8', header=False)

#Unhash to run
merge_files(["../__faculty.csv", "../__deans_provosts.csv"], "Faculty_Deans_Provosts")



def phone_number_scrubber(file_):
	"""In the original cleaned directory list, phone numbers were widely situated between names, e.g. Dr. Foo (XXX) XXX-XXXX Bar. This function removes the phone numbers to provide a complete uninterrupted word string, e.g. Dr. Foo Bar."""

	filename = "../"+file_+".csv"
	infile = open(filename, 'rU')
	outfile = open("../"+file_+"_Phone_Scrubbed.csv", 'w')	

	reader = csv.reader(infile)
	writer = csv.writer(outfile)

	print "Cleaning merged file..."
	for line in reader:
			line0 = str(line)
			line1 = line0.replace(',', ' ').replace(';', ' ').replace("['", '').replace("']", '')
			phonePattern = re.compile("\d?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4})")
			result = phonePattern.sub(lambda m: re.sub('\d', '', m.group(1)), line1)

			writer.writerow([result])

	infile.close()
	outfile.close()

#Unhash to run
#phone_number_scrubber("MERGED_Faculty_Deans_Provosts")


def post_phone_sweep(file_, outfile_):
	"""After clearing out the phone number, this function
	cleans additional irregularties in the text in addition to 
	degrees and other odd spacing that may interfere with
	the cross-list comparison."""

	filename = "../"+file_+".csv"
	infile = open(filename, 'rU')
	outfile_name = "../__CLEANED_"+outfile_+"_.csv"
	outfile = open(outfile_name, 'w')	

	reader = csv.reader(infile)
	writer = csv.writer(outfile)

	print "Cleaning post-phone cleaned file..."
	for line in reader:
			line0 = str(line)
			line1 = line0.replace(',', ' ').replace(';', ' ').replace("['", '').replace("']", '').replace('''"[""''', '').replace('''""]"''', '').replace("\\\\\\\'", "'").replace("\\\\'", "'").replace("\\", '').replace('"""', '"').replace('""', '"')
			line2 = line1.replace("() -", '').replace("...", '').replace(" . ", '')

			# Replace Degrees Such as Dr. or MD
			line3 = line2.replace('Dr.', '').replace('MD', '').replace('M.D.', '').replace('Md', '').replace('Ph.d.', '').replace('Ph.D.', '').replace('PhD', '').replace('J.D.', '').replace('JD', '').replace('FACS', '')
			# Replace Double/Triple Spacing
			line4 = line3.replace('    ', ' ').replace('  ', ' ').replace("  ", ' ')
			writer.writerow([line4])
	print "Writing cleaned file...", outfile_name

	infile.close()
	outfile.close()

#Unhash to run
#post_phone_sweep("__faculty_Phone_Removed_Cleaned")



File_To_Clean = "MERGED_Faculty_Deans_Provosts"
Scrubbed_File = File_To_Clean+"_Phone_Scrubbed"

phone_number_scrubber(File_To_Clean)
post_phone_sweep(Scrubbed_File, "Faculty_Deans_Provosts")




