##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################


import csv, re
import pandas as pd 



##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################


def missing_filter(_file):
	"""This filter sorts a CSV."""

	import csv 

	with open('../'+_file+'.csv', 'rU') as f:
		for row in csv.reader(f):

			#Filter Professors
			if 'Kathleen' and "Cagney" in row[0]:
				with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Hans' and 'Joas' in row[0]:
				with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))


			#Filter Everthing Else
			else:
				with open('../__MISSING.csv', 'a') as f2: f2.write("{}\n".format(row[0]))

#Unhash to run
#missing_filter("__NAMES___CLEANED_Faculty_Deans_Provosts__")
#missing_filter("__CLEANED_Faculty_Deans_Provosts_")


def missing_filter_writer2(crosslist_file):
	"""This filter sorts a CSV."""

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
		



missing_filter_writer2("Only_Existing_UC_Names")


def missing_filter_writer(master_file, crosslist_file):
	"""This filter sorts a CSV."""

	import csv 

	with open('../'+master_file+'.csv', 'rU') as f:
		for row in csv.reader(f):
			existing_names_infile = open('../'+crosslist_file+'.csv', 'rU')
			existing_names_reader = csv.reader(existing_names_infile, delimiter=',')

			for line in existing_names_reader:
				line0 = str(line)
				line1 = line0.replace('[', '').replace(']', '').replace("'", '')
				line2 = line1.split(' ')
				#print len(line2)
				if len(line2)==5:
					print line2[1], line2[2], line2[3], line2[4]
				elif len(line2)==4:
					print line2[1], line2[2], line2[3]
				elif len(line2)==3:
					print line2[1], line2[2]
				else:
					print "WARNING: MISSING DATA"*3


				#except:
				#	try:
				#		print line2[1], line2[2], line2[3]
				#	except:
				#		print line2[1], line2[2]




#missing_filter_writer("__CLEANED_Faculty_Deans_Provosts_", "Only_Existing_UC_Names")






def missing_filter1(master_file, crosslist_file):
	"""This filter sorts a CSV."""

	import csv 



	existing_names_infile = open('../'+crosslist_file+'.csv', 'rU')
	existing_names_reader = csv.reader(existing_names_infile, delimiter=',')

	for line in existing_names_reader:
		line0 = str(line)
		line1 = line0.replace('[', '').replace(']', '').replace("'", '')
		line2 = line1.split(' ')
		#print len(line2)
		if len(line2)==5:

			print line2[1], line2[2], line2[3], line2[4]
			with open('../'+master_file+'.csv', 'rU') as f:
				for row in csv.reader(f):
					#print row[0]
					# Filter all Matching Faculty, Deans, and Provosts from Crosslist File
					
					if line2[1] and line2[2] in row:
						print "AWESOME"*5
						"""
						with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
					# Send Everything Else to Missing File
					else:
						with open('../__MISSING.csv', 'a') as f2: f2.write("{}\n".format(row[0]))

				elif len(line2)==4:
					#print line2[1], line2[2], line2[3]
					if line2[1] and line2[2] and line[3] in row[0]:
						with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
					# Send Everything Else to Missing File
					else:
						with open('../__MISSING.csv', 'a') as f2: f2.write("{}\n".format(row[0]))

				elif len(line2)==3:
					#print line2[1], line2[2]
					if line2[1] and line2[2] in row[0]:
						with open('../__MATCHED.csv','a') as f1: f1.write("{}\n".format(row[0]))
					# Send Everything Else to Missing File
					else:
						with open('../__MISSING.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
				"""
				else:
					print "WARNING: MISSING DATA"*3







#missing_filter1("__CLEANED_Faculty_Deans_Provosts_", "Only_Existing_UC_Names")


def missing_filter3(master_file, crosslist_file):
	"""This filter sorts a CSV."""

	import csv 

	with open('../'+master_file+'.csv', 'rU') as f:
		for row in csv.reader(f):
			existing_names_infile = open('../'+crosslist_file+'.csv', 'rU')
			existing_names_reader = csv.reader(existing_names_infile, delimiter=',')

			for line in existing_names_reader:
				line0 = str(line)
				line1 = line0.replace('[', '').replace(']', '').replace("'", '')
				line2 = line1.split(' ')
				#print len(line2)
				if len(line2)==5:
					print line2[1], line2[2], line2[3], line2[4]
				elif len(line2)==4:
					print line2[1], line2[2], line2[3]
				elif len(line2)==3:
					print line2[1], line2[2]
				else:
					print "WARNING: MISSING DATA"*3


				#except:
				#	try:
				#		print line2[1], line2[2], line2[3]
				#	except:
				#		print line2[1], line2[2]




#missing_filter3("__CLEANED_Faculty_Deans_Provosts_", "Only_Existing_UC_Names")


