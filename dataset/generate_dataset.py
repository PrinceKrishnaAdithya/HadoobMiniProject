import csv, random

random.seed(42)
subjects = ["Math", "Physics", "Chemistry", "CS", "English", "DataStructures"]
depts    = ["CSE", "ECE", "MECH", "CIVIL"]
names    = ["Aarav","Aditya","Akash","Ananya","Arjun","Bhavya","Deepa",
            "Divya","Farhan","Harsh","Ishaan","Jaya","Karan","Kavya",
            "Lakshmi","Mahesh","Meera","Nikhil","Pooja","Rahul","Ravi",
            "Rohit","Saanvi","Sachin","Sahil","Sai","Sandeep","Shreya",
            "Siddharth","Sneha","Suraj","Tanvi","Tejas","Vaibhav","Yash"]

with open("students.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["RollNo","Name","Dept"] + subjects + ["Total","Percentage","Grade","Result"])
    for i in range(1, 201):
        roll = f"2024{i:03d}"
        name = names[i % len(names)] + (f" {chr(65 + i//len(names))}" if i >= len(names) else "")
        dept = depts[i % 4]
        base = random.randint(30, 95)
        marks = [min(100, max(0, random.randint(max(20, base-20), min(100, base+20)))) for _ in subjects]
        total = sum(marks)
        pct   = round(total / len(subjects), 2)
        grade = ("O" if pct >= 91 else "A+" if pct >= 81 else "A" if pct >= 71 else
                 "B+" if pct >= 61 else "B" if pct >= 51 else "C" if pct >= 40 else "F")
        result = "Pass" if all(m >= 35 for m in marks) and pct >= 40 else "Fail"
        w.writerow([roll, name, dept] + marks + [total, pct, grade, result])

print("Generated students.csv with 200 rows")