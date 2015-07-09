##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################


def department_filter():
	"""This filter sorts a CSV, where given rows 
	reflect different faculty and staff and their titles. 
	It creates several new CSV's from the input CSV."""

	import csv 

	with open('../EDITED__CLEANED_CVs__MISSING.csv', 'rU') as f:
		for row in csv.reader(f):
			print row
			#Filter Booth
			if 'Booth' in row[1]:
				with open('../__DEPT_Booth.csv','a') as f1: f1.write("{}\n".format(row))

			#Filter Sociology
			elif 'Sociology' in row[1]:
				with open('../__DEPT_Sociology.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Filter ANTH
			elif 'Anthropology' in row[1]:
				with open('../__DEPT_Anthropology.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Filter CHDV
			elif 'Comparative Human Development' in row[1]:
				with open('../__DEPT_CHDV.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Filter Econ
			elif 'Economics' in row[1]:
				with open('../__DEPT_Economics.csv', 'a') as f2: f2.write("{}\n".format(row))


	

			#Filter Everthing Else
			else:
				with open('../__DEPT_other.csv', 'a') as f2: f2.write("{}\n".format(row))

#Unhash to run
department_filter()
