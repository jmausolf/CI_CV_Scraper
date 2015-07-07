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
			result = phonePattern.sub(lambda m: re.sub('\d', '', m.group(1)), line1)

			writer.writerow([result])

	infile.close()
	outfile.close()

#Unhash to run
#phone_number_scrubber("__faculty")


def post_phone_sweep(file_):
	"""After clearing out the phone number, this function
	cleans additional irregularties in the text in addition to 
	degrees and other odd spacing that may interfere with
	the cross-list comparison."""

	filename = "../"+file_+".csv"
	infile = open(filename, 'rU')
	outfile = open("../"+file_+"_Post.csv", 'w')	

	reader = csv.reader(infile)
	writer = csv.writer(outfile)

	print "Cleaning post-phone cleaned file..."
	for line in reader:
			line0 = str(line)
			line1 = line0.replace(',', ' ').replace(';', ' ').replace("['", '').replace("']", '').replace('''"[""''', '').replace('''""]"''', '').replace("\\\\\\\'", "'").replace("\\\\'", "'").replace("\\", '')
			line2 = line1.replace("() -", '').replace("...", '').replace(" . ", '')

			# Replace Degrees Such as Dr. or MD
			line3 = line2.replace('Dr.', '').replace('MD', '').replace('M.D.', '').replace('Md', '').replace('Ph.d.', '').replace('Ph.D.', '').replace('PhD', '').replace('J.D.', '').replace('JD', '').replace('FACS', '')
			# Replace Double/Triple Spacing
			line4 = line3.replace('    ', ' ').replace('  ', ' ').replace("  ", ' ')
			writer.writerow([line4])

	infile.close()
	outfile.close()

#Unhash to run
#post_phone_sweep("__faculty_Phone_Removed_Cleaned")



def merge_files(args, filename):
	#allFiles = ["../NPR_df1.csv", "../NPR_df2.csv", "../NPR_df3.csv", "../NPR_df4.csv", "../NPR_df5.csv", "../NPR_df6.csv", "../NPR_df7.csv", "../NPR_df8.csv", "../NPR_df9.csv"]

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
merge_files(["../__faculty.csv", "../__deans_provosts.csv"], "Filtered_Faculty_Deans_Provosts")



