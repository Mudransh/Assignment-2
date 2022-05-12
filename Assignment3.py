'''Assignment 3
Mudransh Sethi ,bt21107087'''
from math import *

#Question 1
print("Question 1")
n=int(input("Enter the number: "))
Bin_n=bin(n)
print("The binary equivalent of the number is: ",Bin_n)

#Question 2
print("Question 2")
exp=str(input("Enter the expression to be evaluated: "))
evalexp=eval(exp)
print("THe value of the evaluated expression is: ",evalexp)

#Question 3
print("Question 3")
print("(a) : ",(3*4)*5)
n=float(input("Enter the value of n: "))
print("(b) :",(n*(n-1))/2)
r=float(input("Enter the value of r: "))
print("(c): ",4*pi*(r**2))
a=float(input("Enter the value of a in radians: "))
b=float(input("Enter the value of b in radians: "))
print("(d): ",sqrt((r*((cos(a))**2)+(r*((cos(b))**2)))))
x1=float(input("Enter the value of x1: "))
x2=float(input("Enter the value of x2: "))
y1=float(input("Enter the value of y1: "))
y2=float(input("Enter the value of y2: "))
print("(d) :",(y2-y1)/(x2-x1))

#Question 4
print("Question 4")
alist=[]
for i in range(5):
    alist.append(i)
print("a :",alist)

blist=[]
for i in range(3,5):
    blist.append(i)
print("b :",blist)

clist=[]
for i in range(4,13,3):
    clist.append(i)
print("c :",clist)

dlist=[]
for i in range(15,5,-2):
    dlist.append(i)
print("d :",dlist)

elist=[]
for i in range(5,3):
    elist.append(i)
print("e :",elist)

#Question5
print("Question 5")
hatom=int(input("Enter the number of hydrogen atoms: "))
catom=int(input("Enter the number of carbon atoms: "))
oatom=int(input("Enter the value of oxygen atoms: "))
molwt= (hatom*1.00794)+(catom*12.0107)+(oatom*15.994)
print("Molecular weight of the molecule is: ",molwt)



