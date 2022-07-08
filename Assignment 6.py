from math import *
#Question 1.
print("Question 1")
sum_num = 0
n=int(input("Enter the value of the number: "))
for i in range(1,n):
    if n%i==0:
        sum_num += i
    else:
        continue
if sum_num==n:
    print("Number is true")
else:
    print("no.")

#Question 2.
print("Question 2")
sent=str(input("Enter the string: ")).replace(" ","")
sent_1=sent[::-1]
if sent==sent_1:
    print(sent,"is a palindrome")
else:
    print(sent,"is not a palindrome")

# Question 3
print("Question 3")

n = int(input("Enter number of rows of Pascal Triangle : "))

for i in range(n):
    for j in range(n - i + 1):
        print(end=" ")
    for j in range(i + 1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print()

#Question 4.
print("Question 4")
sent=str(input("Enter the string"))
def ispangram(abc):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in abc.lower():
            return False
    return True
if (ispangram(sent)==True):
    print("Yes",sent,"is a pangram")
else:
    print("No",sent,"is not a pangram")

#Question 5

print("Question 5")

user_str = str(input("Enter hyphen separated sequence of words : "))
word_list = [n for n in user_str.split("-")] # creating a list of all words after separating them
word_list.sort()
print("Alphabetically sorted hyphen separated list is : ")
print("-".join(word_list))

# Question 6

print("Question 6")


def student_data(student_id, **kwargs):
    print("Student ID : ", student_id)
    if 'student_name' in kwargs:
        print("Student name : ", kwargs['student_name'])
    if 'student_class' in kwargs:
        print("Student class : ", kwargs['student_class'])


student_data(student_id='21107087', student_name='Mudransh Sethi')
print()
student_data(student_id='21107087', student_class='Mechanical')
print()
student_data(student_id='21107087', student_name='Mudransh Sethi', student_class='Mechanical')

#Question 7

print("Question 7")

class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print("Checking for instances : ")
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("Checking whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))

# Question 8

print("Question 8")

class zerosum_solution:
 def findSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(zerosum_solution().findSum([-25, -10, -7, -3, 2, 4, 8, 10]))

# Question 9

print("Question 9")

class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0



