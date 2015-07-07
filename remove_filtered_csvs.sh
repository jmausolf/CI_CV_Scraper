##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

### This script exists to assist in the removal of filtered CSVs created by
### name_filter.py. 

### Because name_filter.py runs using an append method, simply re-running the
### script does not overwrite past results. To evaluate changes, the original
### files must first be removed.

### This script simplifies that process.


rm ../__faculty.csv
rm ../__admin.csv
rm ../__other_deans.csv
rm ../__deans_provosts.csv
rm ../__presidents.csv
rm ../__students.csv
rm ../__other_staff_students.csv

