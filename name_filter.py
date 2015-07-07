##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################


def name_filter():
	"""This filter sorts a CSV, where given rows 
	reflect different faculty and staff and their titles. 
	It creates several new CSV's from the input CSV."""

	import csv 

	with open('../MERGED_NPR_Cleaned.csv', 'rU') as f:
		for row in csv.reader(f):

			#Filter Professors
			if 'Professor' in row[0]:
				with open('../__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Prof.' in row[0]:
				with open('../__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Prof' in row[0]:
				with open('../__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'PROF' in row[0]:
				with open('../__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Asst. Prof.' in row[0]:
				with open('../__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Asst Prof.' in row[0]:
				with open('../__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Assistant. Prof.' in row[0]:
				with open('../__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Assoc. Prof.' in row[0]:
				with open('../__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Associate Prof.' in row[0]:
				with open('../__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Lecturer' in row[0]:
				with open('../__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Lect.' in row[0]:
				with open('../__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))


			#Filter Admin
			elif 'Admin' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Administrative' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Administrative' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Executive Asst' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Executive Assistant' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Asst to' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Assistant to' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Fiscal Assistant' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Project Assistant' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Secretary' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Executive Sec' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Receptionist' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Specialist' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Special Assistant' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Adviser' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Advisor' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Admissions Assoc.' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0])) 
			elif 'Registrar' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Programmer' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Coordinator' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Manager' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Mgr' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Editor' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Ed.' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Teacher' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Analyst' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Consultant' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Admnistrator' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Superviser' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Organist' in row[0]:
				with open('../__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


			# Filter 'Associate/Asst Deans/Provosts/Directors'
			elif 'Assistant Dean' in row[0]:
				with open('../__other_deans.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Assistant Provost' in row[0]:
				with open('../__other_deans.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Assistant Director' in row[0]:
				with open('../__other_deans.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Associate Dean' in row[0]:
				with open('../__other_deans.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Associate Provost' in row[0]:
				with open('../__other_deans.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Associate Director' in row[0]:
				with open('../__other_deans.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Assoc. Dean' in row[0]:
				with open('../__other_deans.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Assoc. Provost' in row[0]:
				with open('../__other_deans.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Assoc. Director' in row[0]:
				with open('../__other_deans.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Deputy Dean' in row[0]:
				with open('../__other_deans.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Deputy Provost' in row[0]:
				with open('../__other_deans.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Deputy Director' in row[0]:
				with open('../__other_deans.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Director ' in row[0]:
				with open('../__other_deans.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


			#Filter Students - Part I
			elif 'Postdoctoral Scholar' in row[0]:
				with open('../__students.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


			#Filter Deans and Provosts
			elif 'Dean' in row[0]:
				with open('../__deans_provosts.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Provost' in row[0]:
				with open('../__deans_provosts.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


			#Filter Presidents
			elif 'President' in row[0]:
				with open('../__presidents.csv', 'a') as f2: f2.write("{}\n".format(row[0]))




			#Filter Students - Part II
			elif 'student' in row[0]:
				with open('../__students.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Student' in row[0]:
				with open('../__students.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


			#Filter Remaining Emeritus to Faculty
			elif 'Emeritus' in row[0]:
				with open('../__faculty.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


			#Filter Everthing Else
			else:
				with open('../__other_staff_students.csv', 'a') as f2: f2.write("{}\n".format(row[0]))

#Unhash to run
name_filter()
