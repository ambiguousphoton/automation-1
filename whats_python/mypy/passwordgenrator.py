import random 

a = 1000
b = 9999
password = ""
f = 'abcd'
n = random.randint(a,b)
print(n)

abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQURSTUVWXYZ!@#$%^&*()"
for i in f :
    o = random.randint(0,62)
    password += abc[o]
print(password)
def add(a, b ):
    return a + b

randpassword = add(password,str(n))
print(randpassword)
