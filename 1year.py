print('Semester 1 :')

s1 = int(input('enter the mark of s1 :'))
s2 = int(input('enter the mark of s2 :'))
s3 = int(input('enter the mark of s3 :'))
s4 = int(input('enter the mark of s4 :'))
s5 = int(input('enter the mark of s5 :'))
s6 = int(input('enter the mark of s6 :'))
s1_l1 = int(input('enter the mark of s1_l1 :'))
s1_l2 = int(input('enter the mark of s1_l2 :'))

total = s1 + s2 + s3 + s4 + s5 + s6 + s1_l1 + s1_l2

print('Total :' , total)

gpa = total/8

print('GPA 1 :' , gpa)

if s1 >= 35 and s2 >= 35 and s3 >= 35 and s4 >= 35 and s5 >= 35 and s6 >= 35 and s1_l1 >= 35 and s1_l2 >= 35:
    print('Result : Pass')
else:
    print('Result : Fail')
    
    if gpa >= 90 and gpa <= 100:
        print('Grade : A')

    elif gpa >= 80 and gpa <= 89:
        print('Grade : B')

    elif gpa >= 70 and gpa <= 79:
        print('Grade : C')

    elif gpa <= 60:
        print('Grade : D')

    else:
        print('No Grade')


print('Semester 2 :')

s2_t1 = int(input('enter the mark of s2_t1 :'))
s2_t2 = int(input('enter the mark of s2_t2 :'))
s2_t3 = int(input('enter the mark of s2_t3 :'))
s2_t4 = int(input('enter the mark of s2_t4 :'))
s2_t5 = int(input('enter the mark of s2_t5 :'))
s2_t6 = int(input('enter the mark of s2_t6 :'))
s2_l1 = int(input('enter the mark of s2_l1 :'))
s2_l2 = int(input('enter the mark of s2_l2 :'))

total2 = s2_t1 + s2_t2 + s2_t3 + s2_t4 +s2_t5 + s2_t6 + s2_l1 + s2_l2

print('Total2 :' , total2)

gpa_2 = total2/8

print('GPA_2 :' , gpa_2)

if s2_t1 >= 35 and s2_t2 >= 35 and s2_t3 >= 35 and s2_t4 >= 35 and s2_t5 >= 35 and s2_t6 >= 35 and s2_l1 >= 35 and s2_l2 >= 35:
    print('Result : Pass')
else:
    print('Result : Fail')

    if gpa_2 >= 90 and gpa_2 <= 100:
        print('Grade : A')

    elif gpa_2 >= 80 and gpa_2 <= 89:
        print('Grade : B')

    elif gpa_2 >= 70 and gpa_2 <= 79:
        print('Grade : C')

    elif gpa_2 <= 60:
        print('Grade : D')

    else:
        print('No Grade')


cgpa = (gpa + gpa_2)/2

print('CGPA :' , cgpa)


if cgpa >= 80:
    print('Graduated in 1st class and eligible for placement training')

elif cgpa >= 60:
    print('Graduated in 1st class')

else:
    print('Graduated in 2nd class')









