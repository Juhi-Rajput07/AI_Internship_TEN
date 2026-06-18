#TASK1 (EXPERIMENT WITH ALL  ARITHMETIC OPERATORS)
a = 2
b = 3
print("Sum is", a+b)
print("2 mul by 3 is ", 2*3)
print("2 divide by 3 is ", 2/3)
print("2 power 3 is ", 2**3)
print("modulo od 2 and 3 is ", 2%3)


#TASK2 (Take two numbers from the user)
num1 = int(input("Enter the first number:"))
num2 = int(input("ENnter the second number:"))
print("Addition :",num1 + num2)
print("Subtraction :",num1 - num2)
print("Multiplication :",num1 * num2)
print("Division :",num1 / num2)


#TASK3 (TAKE USER'S AGE / VOTING ELLIGIBLITY CHECK)
age = int(input("Enter your age:"))
if age >= 18:
    print("Eligible to Vote")
else:
    print("NOt ELigible to Vote")




#MINI TASK
#STUDENT GRADE CALCULATOR

marks = int(input("Enter your marks:"))
if 90 <= marks <= 100:
    print("A")
elif 80 <= marks <= 89:
    print("B")
elif 70 <= marks <=79:
    print("C")    
elif 60 <= marks <=69:
    print("D")
elif marks < 60:
    print("F")
else:
    print("Enter a valid marks:")
    