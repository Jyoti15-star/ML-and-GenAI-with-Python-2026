#Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation
#Detail of the student
name= input("Enter the name of the student:")
Roll_No= input("Enter the roll no. of the student:")
# marks of the student
maths= int(input("Enter the marks of maths(out of 100):"))
science = int(input("Enter the marks of science(out of 100):"))
total = maths+ science 
percentage = (total/200)*100
print("the total marks in maths and science:",total)
print("the percentage of marks is:",percentage)

