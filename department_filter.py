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

			#### SOCIAL SCIENCE
			#Filter Sociology
			if 'Sociology' in row[1]:
				with open('../__DEPT_Sociology.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Filter Anthropology
			elif 'Anthropology' in row[1]:
				with open('../__DEPT_Anthropology.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Filter CHDV
			elif 'Comparative Human Development' in row[1]:
				with open('../__DEPT_CHDV.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Filter Econ
			elif 'Economics' in row[1]:
				with open('../__DEPT_Economics.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Filter History
			elif 'History' in row[1]:
				with open('../__DEPT_History.csv', 'a') as f2: f2.write("{}\n".format(row))


			#Filter Political Science
			elif 'Political' in row[1]:
				with open('../__DEPT_Political_Science.csv', 'a') as f2: f2.write("{}\n".format(row))
			elif 'International' in row[1]:
				with open('../__DEPT_Political_Science.csv', 'a') as f2: f2.write("{}\n".format(row))


			#Filter Psychology
			elif 'Psychology' in row[1]:
				with open('../__DEPT_Psychology.csv', 'a') as f2: f2.write("{}\n".format(row))


			#### HUMANITIES


			#Filter Art History
			elif 'Art' in row[1] and 'History' in row[1]:
				with open('../__DEPT_Art_History.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Filter Cinema and Media Studies
			elif 'Cinema' in row[1] and 'Media' in row[1]:
				with open('../__DEPT_Cinema_Media.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Filter Classics
			elif 'Classics' in row[1]:
				with open('../__DEPT_Classics.csv', 'a') as f2: f2.write("{}\n".format(row))


			#Filter Comparitive Literature
			elif 'Comparitive' in row[1] and 'Literature' in row[1]:
				with open('../__DEPT_Comparative_Literature.csv', 'a') as f2: f2.write("{}\n".format(row))
			elif 'Comparitive' in row[1]:
				with open('../__DEPT_Comparative_Literature.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Filter English Language and Literature
			elif 'English' in row[1]:
				with open('../__DEPT_English.csv', 'a') as f2: f2.write("{}\n".format(row))
			elif 'English' in row[1] and 'Literature' in row[1]:
				with open('../__DEPT_English.csv', 'a') as f2: f2.write("{}\n".format(row))


			#Filter Germanic
			elif 'Germanic' in row[1]:
				with open('../__DEPT_Germanic.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Filter Linguistics
			elif 'Linguistics' in row[1]:
				with open('../__DEPT_Linguistics.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Filter Music
			elif 'Music' in row[1]:
				with open('../__DEPT_Music.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Filter Romance
			elif 'Romance' in row[1]:
				with open('../__DEPT_Romance.csv', 'a') as f2: f2.write("{}\n".format(row))
			elif 'Spanish' in row[1]:
				with open('../__DEPT_Romance.csv', 'a') as f2: f2.write("{}\n".format(row))
			elif 'Italian' in row[1]:
				with open('../__DEPT_Romance.csv', 'a') as f2: f2.write("{}\n".format(row))
			elif 'French' in row[1]:
				with open('../__DEPT_Romance.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Filter Philosophy
			elif 'Philosophy' in row[1]:
				with open('../__DEPT_Philosophy.csv', 'a') as f2: f2.write("{}\n".format(row))





			#### NATURAL AND BIOLOGICAL SCIENCES
			
			#Biology
			elif 'Biology' in row[1]:
				with open('../__DEPT_Biology.csv','a') as f1: f1.write("{}\n".format(row))

			#Neuroscience
			elif 'Neurobiology' in row[1]:
				with open('../__DEPT_Neuroscience.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'Neuroscience' in row[1]:
				with open('../__DEPT_Neuroscience.csv','a') as f1: f1.write("{}\n".format(row))

			#Chemistry
			elif 'Chemistry' in row[1]:
				with open('../__DEPT_Chemistry.csv','a') as f1: f1.write("{}\n".format(row))


			#Physics
			elif 'Physics' in row[1]:
				with open('../__DEPT_Physics.csv','a') as f1: f1.write("{}\n".format(row))


			#Math	
			elif 'Mathematics' in row[1]:
				with open('../__DEPT_Mathematics.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'Math' in row[1]:
				with open('../__DEPT_Mathematics.csv','a') as f1: f1.write("{}\n".format(row))

			#Statistics
			elif 'Statistics' in row[1]:
				with open('../__DEPT_Statistics.csv','a') as f1: f1.write("{}\n".format(row))


			#CS
			elif 'Computer' in row[1]:
				with open('../__DEPT_Computer_Science.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'cs.uchicago' in row[1]:
				with open('../__DEPT_Computer_Science.csv','a') as f1: f1.write("{}\n".format(row))


			#Geophysical	
			elif 'Geophysical' in row[1]:
				with open('../__DEPT_Geophysical.csv','a') as f1: f1.write("{}\n".format(row))

			#Astronomy	
			elif 'Astronomy' in row[1]:
				with open('../__DEPT_Astronomy.csv','a') as f1: f1.write("{}\n".format(row))
	


			### PROFESSIONAL SCHOOLS

			#Filter Booth
			elif 'Booth' in row[1]:
				with open('../__DEPT_Booth.csv','a') as f1: f1.write("{}\n".format(row))
			elif '@chicagobooth' in row[1]:
				with open('../__DEPT_Booth.csv','a') as f1: f1.write("{}\n".format(row))

			#Law
			elif 'law.uc' in row[1]:
				with open('../__DEPT_Law.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'Law' in row[1] and 'School' in row[1]:
				with open('../__DEPT_Law.csv','a') as f1: f1.write("{}\n".format(row))

			#Filter Harris School
			elif 'Harris' in row[1] and 'School' in row[1]:
				with open('../__DEPT_Harris.csv', 'a') as f2: f2.write("{}\n".format(row))
	
			#Filter Public Health
			elif 'Public' in row[1] and 'Health' in row[1]:
				with open('../__DEPT_Health.csv', 'a') as f2: f2.write("{}\n".format(row))
			elif 'Global' in row[1] and 'Health' in row[1]:
				with open('../__DEPT_Health.csv', 'a') as f2: f2.write("{}\n".format(row))
			elif 'Health' in row[1]:
				with open('../__DEPT_Health.csv', 'a') as f2: f2.write("{}\n".format(row))

			#Medicine and Hospital
			elif 'uchospital' in row[1]:
				with open('../__DEPT_Medicine_BSD.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'bsd.' in row[1]:
				with open('../__DEPT_Medicine_BSD.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'dacc.' in row[1]:
				with open('../__DEPT_Medicine_BSD.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'Surgery' in row[1]:
				with open('../__DEPT_Medicine_BSD.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'Medicine' in row[1]:
				with open('../__DEPT_Medicine_BSD.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'Medical' in row[1]:
				with open('../__DEPT_Medicine_BSD.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'Pediatric' in row[1]:
				with open('../__DEPT_Medicine_BSD.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'Pediatrics' in row[1]:
				with open('../__DEPT_Medicine_BSD.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'Pathology' in row[1]:
				with open('../__DEPT_Medicine_BSD.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'Radiology' in row[1]:
				with open('../__DEPT_Medicine_BSD.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'Physio' in row[1]:
				with open('../__DEPT_Medicine_BSD.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'Cancer' in row[1]:
				with open('../__DEPT_Medicine_BSD.csv','a') as f1: f1.write("{}\n".format(row))
			elif 'MC' in row[1]:
				with open('../__DEPT_Medicine_BSD.csv','a') as f1: f1.write("{}\n".format(row))


			#Filter Everthing Else
			else:
				with open('../__DEPT_other.csv', 'a') as f2: f2.write("{}\n".format(row))

#Unhash to run
department_filter()
