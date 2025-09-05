from random import randint, shuffle

message = "Hello, world!"
class_size = randint(15, 36)
student_marks = list(zip(range(1000, class_size + 1001),
    (randint(40, 100) for s in range(class_size))))
shuffle(student_marks)
marks_list = [s[1] for s in student_marks]
