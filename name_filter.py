




def name_filter():
	import csv 
	with open('../Cleaned_One_Name_Per_Row.csv', 'rU') as f:
		for row in csv.reader(f):

			#Filter Professors
			if 'Professor' in row[0]:
				with open('__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Prof.' in row[0]:
				with open('__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Prof' in row[0]:
				with open('__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'PROF' in row[0]:
				with open('__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Asst. Prof.' in row[0]:
				with open('__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Asst Prof.' in row[0]:
				with open('__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Assistant. Prof.' in row[0]:
				with open('__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Assoc. Prof.' in row[0]:
				with open('__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))
			elif 'Associate Prof.' in row[0]:
				with open('__faculty.csv','a') as f1: f1.write("{}\n".format(row[0]))


			#Filter Deans and Provosts
			elif 'Dean' in row[0]:
				with open('__deans_provosts.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Provost' in row[0]:
				with open('__deans_provosts.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


			#Filter Admin
			elif 'Admin' in row[0]:
				with open('__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Administrative' in row[0]:
				with open('__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Administrative' in row[0]:
				with open('__admin.csv', 'a') as f2: f2.write("{}\n".format(row[0]))


			#Filter Students
			elif 'student' in row[0]:
				with open('__students.csv', 'a') as f2: f2.write("{}\n".format(row[0]))
			elif 'Student' in row[0]:
				with open('__students.csv', 'a') as f2: f2.write("{}\n".format(row[0]))



			#Filter Everthing Else
			else:
				with open('__other_staff_student.csv', 'a') as f2: f2.write("{}\n".format(row[0]))

name_filter()
