max_marks=int(input("enter the maximum marks for 5 subjects = "))
s1=float(input("enter the marks of subject-1 = "))
s2=float(input("enter the marks of subject-2 = "))
s3=float(input("enter the marks of subject-3 = "))
s4=float(input("enter the marks of subject-4 = "))
s5=float(input("enter the marks of subject-5 = "))
tot_marks=s1+s2+s3+s4+s5
avg_marks = tot_marks/5
percent= (tot_marks/max_marks)*100
if percent>=90:
    print("percentage = ",percent)
    print("Grade = A")
elif percent>=80:
    print("percentage = ",percent)
    print("Grade = B")
elif percent>=70:
    print("percentage = ",percent)
    print("Grade = C")
elif percent>=60:
    print("percentage = ",percent)
    print("Grade = D")
elif percent>=50:
    print("percentage = ",percent)
    print("Grade = E")
elif percent <50:
    print("percentage = ",percent)
    print("Fail")
