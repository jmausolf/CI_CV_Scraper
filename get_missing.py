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
missing_filter("__CLEANED_Faculty_Deans_Provosts_")



