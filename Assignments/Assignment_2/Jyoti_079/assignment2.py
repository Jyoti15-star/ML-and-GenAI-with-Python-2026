#1Find sum of first 10 natural numbers.
sum = 0
for i in range(1,11):
    sum = sum+i
print("sum=",sum)

#2Find factorial of a number.
n = int(input("Enter a no.:"))
factorial = 1
for i in range(1,n+1):
    factorial= factorial*i
print("Factorial of",n,"is:",factorial)

#3Print Fibonacci Series
x = int(input("Enter no. of terms:"))
a=0
b=1
for i in range(1,x+1):
    print(a, end=" ")
    c=a+b
    a=b
    b=c
print()

#4Find largest among 3 numbers.
p=int(input("Enter first number: "))
q=int(input("Enter second number: "))
r=int(input("Enter third number: "))
if p>=q and p>=r:
    print(p,"is the largest no.")
elif q>=p and q>=r:
    print(q,"is the largest no.")
else:
    print(r,"is the largest no.")

#5Create Student Result System
s = int(input("Enter no. of students:"))
for i in range(1,s+1):
    name=input("Enter student name:")
    RollNo=input("Enter roll no. of the student:")
    science=int(input("Enter the marks of the student of science:"))
    maths=int(input("Enter the marks of the student of maths:"))
    total=maths+science
    percentage=total/200*100
    print("The percentage:",percentage)
    if percentage>=90:
        print("The grade is A")
    elif percentage<90 and percentage>=80:
        print("The grade is B")
    else:
        print("The grade is C")



