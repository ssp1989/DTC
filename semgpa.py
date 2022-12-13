
# PROGRAM HAS A DOUBT TO BE CLARIFIED

grades = [4 , 3 , 2 , 1 , 0]
A, B, C, D, F = grades
print(A)
print(B)
print(C)
print(D)
print(F)

print('Semester 1 :')

s1 = str(input('enter the s1 grade :'))
s2 = str(input('enter the s2 grade :'))
s3 = str(input('enter the s3 grade :'))
s4 = str(input('enter the s4 grade :'))
s5 = str(input('enter the s5 grade :'))
s6 = str(input('enter the s6 garde :'))
sem1_l1 = str(input('enter the l1 grade :'))
sem1_l2 = str(input('enter the l2 grade :'))

total = s1 + s2 + s3 + s4 + s5 + s6 + sem1_l1 + sem1_l2

sem1_GPA = total/8.0

print('Total :' , total)
print('GPA :' , sem1_GPA)


