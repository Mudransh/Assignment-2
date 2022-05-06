#Question1.
#a)
sent="Python is a case sensitive language"
sent_length=len(sent)
print(sent_length)
#b)
reverse_sent=sent[::-1]
print(reverse_sent)
#c
new_string=sent[7:26]
print(new_string)
#d
replaced_sent=sent.replace("a case sensitive","object oriented")
print(replaced_sent)
#e
indices=sent.index("a")
print(indices)
#f
short_sent=sent.replace(" ","")
print(short_sent)

#Question2.
name="Mudransh Sethi"
SID="21107087"
dep_name="Mechanical"
CGPA="9.9"
print(f"Hey, {name} Here!\nMy SID is {SID}\nI am from {dep_name} department and my CGPA is {CGPA}")

#Question3.
a=56
b=10
print("a&b: ",a&b)
print("a|b: ",a|b)
print("a^b: ",a^b)
print("a<<2,b<<2: ",a<<2,b<<2)
print("a>>2,b>>2: ",a>>2,b>>2)

#Question4.
s=str(input("Enter the string - "))
t = s.find('name')
if (t==-1):
    print("No")
else:
    print("yes")

#Question5.
s1=int(input("Enter the value of side 1 of the triangle: "))
s2=int(input("Enter the value of side 2 of the triangle: "))
s3=int(input("Enter the value of side 3 of the triangle: "))
cases = s1+s2>s3 and s2+s3>s1 and s1+s3>s2
match cases:
    case True:
        print("Yes")
    case False:
        print("No")

#Question6.
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
#By using XOR function :
n1=bin((a^b))
n2=n1.count("1")
print(n2)


