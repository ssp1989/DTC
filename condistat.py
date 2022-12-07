# if , else , elif , Nested if

a = 15
b = 25

if a>b :
    print('a is greater than b')
else:
    print('b is greater than a')

a = 5
b = 5

if a>b:
    print('a is greater than b')
elif a == b:
    print('a and b are equal')
else:
    print('b is greater than a')

a = 25
b = 35

print('b is greater') if b>a else print('a is greater')

a = 55
b = 55

print('a and b are equal') if a == b  else print('invalid expression')

a = 51
b = 50

print('a and b are not equal') if a != b else print('a and b are equal')


                                     # LOOP STATEMENT
# FOR LOOP

for a in range(5):
    print(a)

for b in range (10,20):
    print(b)

#for c in range(5.5,15.5):    Float or Complex datatypes are not allowed)


for c in range(0,20,2):
    print(c)

for d in range(0,20,3):
    print(d)

for i in range(3):
    a = int(input('enter the value of a :'))
    b = int(input('enter the value of b :'))
    print(a+b)
 


# WHILE LOOP    i+ = 1 and i = i+1 both are same

i = 1
while i<10:
    print(i)
    i = i+2

b = 20
while b>10:
    print(b)
    b = b-1

a = 5
while a<10:
    print(a)
    if(a == 8):
        break
    a = a+1



a = 1
while a<10:
    if(a == 7):
        break
    print(a)
    a = a+1

x = 5
while( x<=15):
    if(x == 12):
        break
    print(x)
    x+= 1


  # TODAYS ASSIGNMENT BY SRI SIR

x = 12
y = 1

while (x<=12):
    while(y<=10):
        print(x,'*',y,'=',x*y)
        y = y+1
    

