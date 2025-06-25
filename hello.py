from operator import truediv
import re

print("hello world")
name = "pavani" #python is dynamically typed no need to mention data type explicitely
age = 25
name1, age1 = "teju" , 24
print(name, age) #if botj variables has same name it takes the closer one
print(name , age)
print ("my name is" + name)
print("my age is " , age)
print(f"my age is {age}")
print("my age is" + str(age))
# in python concatenate a string and an integer using the + operator.
# In Python, you can only concatenate strings with other strings.
x = True
if x:
    print("hello python")
y = False
if y:
    print("hello java")
#strings
arn = "arn:aws:iam::523224779633:user/Pavani"
print (arn.split("/"))
print(arn.split("/")[1])
print(arn.split("/")[0])
print(len(arn)) #0...
print(name.upper())
print(name.lower())
r = age/age1
print(r)
p = round((3.14567),2)
print(p)
a,b = 2,4
print(b-a)
print(b/a)
print(a+b)
print(a*b)
print(b%2)
text = "my name is teju"
pattern = r"name"
match1 = re.match(pattern ,text)
if match1:
    print("match found",match1.group()) # used to find errors in a log file
else:
    print("match not found")
 


