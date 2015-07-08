##################################
###                            ###
###      Joshua G. Mausolf     ###
###    Computation Institute   ###
###    University of Chicago   ###
###                            ###
##################################

### This script exists to assist in the removal of filtered CSVs created by
### get_missing.py. 

### Because get_missing.py runs using an append method, simply re-running the
### script does not overwrite past results. To evaluate changes, the original
### files must first be removed.

### This script simplifies that process.


rm ../__MISSING.csv
rm ../__MATCHED.csv


