name = input('학생의 이름을 입력하세요 : ')
student_id = input('학생의 학번을 입력하세요 : ')
student = Student(name, student_id)

korean_quiz = int(input('학생의 국어 성적을 입력하세요 : '))
math_quiz = int(input('학생의 수학 성적을 입력하세요 : '))
science_quiz = int(input('학생의 과학 성적을 입력하세요 : '))

student.set_korean_quiz(korean_quiz)
student.set_math_quiz(math_quiz)
student.set_science_quiz(science_quiz)

print(student)
