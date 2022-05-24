#Question 1.
print("Question 1")
m=int(input("Enter the marks: "))
if m<25:
    print("Grade = F")
elif 25<=m<45:
    print("Grade = E")
elif 45<=m<50:
    print("Grade = D")
elif 50<=m<60:
    print("Grade = C")
elif 60<=m<80:
    print("Grade = B")
elif m>=80:
    print("Grade = A")
else:
    print("Marks should be between 0-100")

#Question 2.
print("Question 2")
Yr=int(input("Enter the year: "))
if Yr%400==0:
    print("Year is a leap year")
elif Yr%4==0 and Yr%100!=0:
    print("Year is a leap year")
else:
    print("Year is not a leap year")

#Question 3.
print("Question 3")
from random import randint

for i in range(1,11):
    num1=randint(1,10)
    num2=randint(1,10)
    print(f" ques {i}-->  {num1}X{num2}")
    a=int(input("Enter answer : "))
    if a == num1*num2 :
        print("Right !")
    else:
        print(f"Wrong , answer is {num1*num2}")

#Question 4
print("Question 4")
for i in range(200):
    if i%5==2:
        if i%6==3:
            if i%7==2:
                print(i,"is the possible number of candies")
