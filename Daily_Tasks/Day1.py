#TASK1. (CREATE VARIABLES)
fruit = 'apple'
num = 10
pie = 3.14
bool = True
print(fruit)
print(num)
print(pie)
print(bool)


#TASK2 (TAKING USER INPUT)
Name = input("Enter Your Name:")
Age = int(input("Enter Your Age:"))
College = input("Enter Your College Name:")
Branch = input("Enter Your Branch:")
print("Name:", Name)
print("Age:", Age)
print("College:", College)
print("Branch:", Branch)


#TASK3.   (TYPE CONVERSION)
print(type(fruit)) #str
print(type(num)) #int
print(type(pie)) #float
print(type(bool)) #bool

print(float(num)) #10.0
print(int(pie)) #3
print(str(bool)) #True
print(type(str(num))) #str





# MINI TASK  ( 15 MINUTES )

# STUDENT PROFILE GENERATOR

Name = input("Enter Your Name:")
Age = int(input("Enter Your Age:"))
College = input("Enter Your College Name:")
Branch = input("Enter Your Branch:")
Interest = input("Enter Your Interest:")
Graduation_Year = int(input("Enter Your Graduation Year:"))

print("Name:" , Name)
print("Age:" , Age)
print("College:" , College)
print("Branch:" , Branch)
print("Interest:" , Interest)
print("Graduation Year:" , Graduation_Year)
print("I will graduate in", Graduation_Year)