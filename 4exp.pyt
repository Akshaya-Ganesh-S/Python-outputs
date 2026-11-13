import csv
students = [
{"RollNo": "101"
,
"Name": "Anitha"
,
"Department": "CSE"
,
"Mark": 86},
{"RollNo": "102"
,
"Name": "Bala"
,
"Department": "CSE"
,
"Mark": 91},
{"RollNo": "103"
,
"Name": "Chitra"
,
"Department": "ECE"
,
"Mark": 78}
]
# Tuple example: fixed course details
course = ("Python"
, 4)
print("Course Tuple:"
, course)
# Write text file
with open("students.txt"
,
"w") as file:
for student in students:
	file.write(str(student) + "\n")
# Write CSV file
with open("students.csv"
,
"w"
, newline="") as file:
fields = ["RollNo"
,
"Name"
,
"Department"
,
"Mark"]
14 | P a g e
Code/Subject: AD/AM/IT/CB/CZ/CS6102– EXPLORATION IN ARTIFICIAL INTELLIGENCE
writer = csv.DictWriter(file, fieldnames=fields)
writer.writeheader()
writer.writerows(students)
# Read CSV file

print("\n--- Records from CSV ---\n")
with open("students.csv"
,
reader = csv.DictReader(file)
"r") as file:
for row in reader:
print(row["RollNo"], row["Name"],
row["Department"], row["Mark"])