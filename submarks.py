tamil = int(input('enter the tamil mark :'))
english = int(input('enter the english mark :'))
maths = int(input('enter the maths mark :'))

total = tamil + english + maths
average = total/3.0

print('Total :' , total)
print('average :' , average)

if tamil >= 35 and english >= 35 and maths >= 35:
    print('Result : Pass')
    if average >= 90 and average <= 100:
        print('Grade A')
    elif average >= 80 and average <= 89:
        print('Grade B')
    elif average >= 70 and average <= 79:
        print('Grade C')
    elif average <= 60:
        print('Grade D')
else:
    print('No Grade')
    print('Result : Fail')


