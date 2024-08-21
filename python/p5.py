'''Accept average score from the student of his exam & print his result as follows
0 to 49 is Fail
50 to 74 is Second class
75 to 90 is First class
91 to 100 is Distinction 
check for invalid inputs'''


student_score=int(input("Enter your average score of your exams: "))

if 0 <= student_score and student_score <= 49 :
    print('Result is Fail')
elif student_score <= 74:
    print('Result is Second class')
elif student_score <= 90:
    print('Result is First Class')
elif 91 <= student_score and student_score <= 100 :
    print('Result is Distinction')
else :
    print('Invalid input')