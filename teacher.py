from student_database import set_student, set_rating


def add_student():
    """ получение данных ученика от учителя и их передача для записи"""
    metric = input('Введите данные (Фамилия, Имя, класс через пробел):').split(' ')
    set_student(metric)

def put_rating():
    """ получение данных оценки от учителя и их передача для записи"""
    last_name = input('Введите фамилию фамилию ученика: ')
    lesson = input('Введите название урока')
    raiting = input('Введите оценку или оценки через пробел: ').split()
    set_rating(last_name, lesson, raiting)