##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################



def missing_filter_writer(crosslist_file):
	"""This code uses python to write the bulk of the python commands
	used in the get missing filter."""

	import csv 

	existing_names_infile = open('../'+crosslist_file+'.csv', 'rU')
	existing_names_reader = csv.reader(existing_names_infile, delimiter=',')

	#Generate Match Command String From Filter as a Var
	match_command0 = """     with open('../__MATCHED.csv','a') as f1: f1.write("{}'"""+"""\+"""+"""n".format(row[0]))"""
	match_command = str(match_command0).replace('+', '')

	#print match_command3

	for line in existing_names_reader:
		line0 = str(line)
		line1 = line0.replace('[', '').replace(']', '').replace("'", '')
		line2 = line1.split(' ')


		if len(line2)==5:
			#print line2[1], line2[2], line2[3], line2[4]
			print "if '"+line2[1]+"' and '"+line2[2]+"' and '"+line2[3]+"' and '"+line2[4]+"' in row[0]:"
			print (match_command)
			#command1 = search_term1+'\n'+match_command
			#print command1
			#commands1.append([command1])

		
		elif len(line2)==4:
			commands2 = []
			#print line2[1], line2[2], line2[3]
			print "if '"+line2[1]+"' and '"+line2[2]+"' and '"+line2[3]+"' in row[0]:"
			print (match_command)
		
		elif len(line2)==3:
			#print line2[1], line2[2]
			print "if '"+line2[1]+"' and '"+line2[2]+"' in row[0]:"
			print (match_command)
		else:
			print "WARNING: MISSING DATA"*3
		

missing_filter_writer("Only_Existing_UC_Names")

