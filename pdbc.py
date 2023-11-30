import csv

mydict =[ {'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
		{'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
		{'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
		{'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
		{'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
		{'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]
csvfields = ['name', 'branch', 'year', 'cgpa']
filename = "C:/Users/DammannagariGangadha/Desktop/input/univ2.csv"
with open(filename, "w") as fp:
    d = csv.DictWriter(fp, fieldnames=csvfields)
    d.writeheader()
    d.writerows(mydict)
