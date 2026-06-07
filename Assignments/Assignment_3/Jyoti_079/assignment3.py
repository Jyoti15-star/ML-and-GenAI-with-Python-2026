#1Create a function to print first 10 natural numbers.
def printNo(i):
    print(i,end=" ")
for i in range(1,11):
    printNo(i)
print()

#2Create a function to calculate sum of first N natural numbers.
n=int(input("Enter a no.:"))
def sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    print("sum of first",n,"natural nos.:",sum)
sum(n)

#3Create a function to reverse a number.
s=int(input("Enter a no.:"))
def reverse(s):
    reverse=0
    while s>0:
        reverse=reverse*10+s%10
        s=s//10
    return reverse
result=reverse(s)
print("The reverse of",s,":",result)


#4Create a function to count digits in a number.
x=int(input("Enter a no.:"))
def count(n):
    original=n
    count=0
    while n>0:
        count+=1
        n=n//10
    print("The No. of digits in",original,"is",count)
count(x)

#5Create a function to check palindrome number.
def checkPalindrome(s):
    if s==result:
        print(s,"is a palindrome")
    else:
        print(s,"is not a palindrome")
checkPalindrome(s)

#6Create a function to generate Fibonacci series.
p = int(input("Enter the number of terms: "))
def fibonacci(p):
    a = 0
    b = 1
    for i in range(1,p+1):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(p)
print()

#7Calculator Using Functions 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b

print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(num1, num2))
elif choice == 2:
    print("Result =", subtract(num1, num2))
elif choice == 3:
    print("Result =", multiply(num1, num2))
elif choice == 4:
    print("Result =", divide(num1, num2))
else:
    print("Invalid Choice")

#8Create a text file and store student details.
file = open("student.txt", "w")

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
course = input("Enter Course: ")

file.write("Student Details\n")
file.write("Name: " + name + "\n")
file.write("Roll Number: " + roll_no + "\n")
file.write("Course: " + course + "\n")

file.close()

print("Student details stored successfully in student.txt")

#9Read data from a file.
file = open("student.txt", "r")
data = file.read()
print("Student Details:")
print(data)
file.close()

#10Handle division by zero using exception handling. 
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#11Create a Student class with name and marks. 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

s1 = Student(name, marks)
s1.display()

