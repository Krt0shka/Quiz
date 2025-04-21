from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton, QGroupBox, QMessageBox, QStyle
from random import choice
from PyQt5 import QtGui
import os
import time

#задаём вопросы
questions = [
    {
        'question': 'Какой город является столицей Франции?',
        'answer1': 'Берлин',
        'answer2': 'Мадрид',
        'answer3': 'Лондон',
        'answer4': 'Париж',
        'correct': 'Париж'
    },
    {
        'question': 'Кто является автором произведения "Война и мир"?',
        'answer1': 'Федор Достоевский',
        'answer2': 'Антон Чехов',
        'answer3': 'Лев Толстой',
        'answer4': 'Александр Пушкин',
        'correct': 'Лев Толстой'
    },
    {
        'question': 'Какой элемент является химическим символом для кислорода?',
        'answer1': 'К',
        'answer2': 'О',
        'answer3': 'Н',
        'answer4': 'С',
        'correct': 'О'
    },
    {
        'question': 'Сколько планет в Солнечной системе?',
        'answer1': '7',
        'answer2': '8',
        'answer3': '9',
        'answer4': '10',
        'correct': '8'
    },
    {
        'question': 'Кто первым ступил на Луну?',
        'answer1': 'Юрий Гагарин',
        'answer2': 'Нил Армстронг',
        'answer3': 'Майкл Коллинз',
        'answer4': 'Базз Олдрин',
        'correct': 'Нил Армстронг'
    },
    {
        'question': 'Какая страна является самой большой по территории?',
        'answer1': 'Китай',
        'answer2': 'Канада',
        'answer3': 'Россия',
        'answer4': 'США',
        'correct': 'Россия'
    },
    {
        'question': 'Какой из этих языков программирования является объектно-ориентированным?',
        'answer1': 'HTML',
        'answer2': 'Java',
        'answer3': 'CSS',
        'answer4': 'SQL',
        'correct': 'Java'
    },
    {
        'question': 'Сколько часов в одном дне?',
        'answer1': '20',
        'answer2': '22',
        'answer3': '24',
        'answer4': '26',
        'correct': '24'
    },
    {
        'question': 'Как называется орган, который качает кровь по всему телу?',
        'answer1': 'Легкие',
        'answer2': 'Печень',
        'answer3': 'Сердце',
        'answer4': 'Почки',
        'correct': 'Сердце'
    },
    {
        'question': 'Какая планета является ближайшей к Солнцу?',
        'answer1': 'Венера',
        'answer2': 'Земля',
        'answer3': 'Меркурий',
        'answer4': 'Марс',
        'correct': 'Меркурий'
    }
]


#счётчики
global c
c = 0
global c2
c2 = 0
global c3
c3 = 3
global quest_num
quest_num = len(questions)
global stime
stime = time.time()

#Результат после вопроса
def resA():
    global c
    global c2
    print(f"Вы ответили правильно на {c2} вопросов из {c} вопросов.")
    print(f"Рейтинг: {round(c2/c*100, 2)}%")

def res():
    etime = time.time()
    res_window = QMessageBox(window)
    res_window.setWindowTitle('Результат')
    res_window.setText(f"Вы ответили правильно на {c2} вопросов из {c} вопросов.\nРейтинг: {round(c2/c*100, 2)}%\nВремя прохождения: {round(etime - stime)} секунд.")

    close = QPushButton("Закрыть")
    close.clicked.connect(app.quit)
    res_window.addButton(close, QMessageBox.AcceptRole)

    res_window.exec_()
#создаём окни
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.setFixedSize(500, 250)
window.setWindowIcon(QtGui.QIcon("C:/Users/Ilya/Desktop/VSCode/VS Code Py/algo/memory_cards/logo.ico"))
print(os.path.exists("C:/Users/Ilya/Desktop/VSCode/VS Code Py/algo/memory_cards/logo.ico"))


#создаём виджеты
question = QLabel('?')
cur_quest = QLabel(f"{quest_num}/10")
group_answers = QGroupBox('Выберите ответ')

#радио кнопки
ans_1 = QRadioButton('')
ans_2 = QRadioButton('')
ans_3 = QRadioButton('')
ans_4 = QRadioButton('')

#объеденяем радио кнопки в группу
ans_layout1 = QVBoxLayout()
ans_layout1.setSpacing(20)
ans_layout1.addWidget(ans_1, alignment=Qt.AlignCenter)
ans_layout1.addWidget(ans_2, alignment=Qt.AlignCenter)

#расставляем радио кнопки и добавляем лайауты
ans_layout2 = QVBoxLayout()
ans_layout2.setSpacing(20)
ans_layout2.addWidget(ans_3, alignment=Qt.AlignCenter)
ans_layout2.addWidget(ans_4, alignment=Qt.AlignCenter)
ans_layout = QHBoxLayout()
ans_layout.addLayout(ans_layout1)
ans_layout.addLayout(ans_layout2)
group_answers.setLayout(ans_layout)


#добавляем функцию к кнопке ответа
def show_result():
    if button.text() == 'Ответить':
        if len(questions) == 0:
            res()
        counter = 0
        for ans in (ans_1, ans_2, ans_3, ans_4):
            if ans.isChecked():
                counter += 1
        if counter == 0:
            return 0
        
        for ans in (ans_1, ans_2, ans_3, ans_4):
            ans.show()
        help_btn.hide()
        for ans in (ans_1, ans_2, ans_3, ans_4):
            #проверяем каждую книпку на её состояние
            if ans.isChecked():
                button.setText('Следующий вопрос')
                answer_group.show()
                group_answers.hide()
                #если правильно
                if ans.text() == window.correct:
                    is_correct.setStyleSheet('color: #339900;')
                    is_correct.setText('Правильно!')
                    global c2
                    c2 += 1
                        
                          
                #если неправильно
                else:
                    is_correct.setStyleSheet('color: #FF0000;')
                    is_correct.setText('Неправильно.')
        resA()
        global quest_num
        quest_num = len(questions)
        cur_quest.setText(f"{quest_num}/10")
    else:
        help_btn.show()
        set_question()
        answer_group.hide()
        group_answers.show()
        button.setText('Ответить')

#кнопка и её функция
button = QPushButton('Ответить')
button.clicked.connect(show_result)

#подсказка
def quest_help():
    global c3
    if c3 > 0:
        c3 -= 1
        help_btn.hide()
        help_btn.setText(f"Подсказка({c3}/3)")
        correct = window.correct
        answers = [ans_1, ans_2, ans_3, ans_4]
        while True:
            random_ans = choice(answers)
            if random_ans.text() != correct:
                index = answers.index(random_ans)
                answers[index].hide()
                break
            else:
                pass
    else:
        pass

help_btn = QPushButton(f"Подсказка({c3}/3)")
help_btn.clicked.connect(quest_help)

#группа для ответа и текста
answer_group = QGroupBox('Правильный ответ:')
is_correct = QLabel('Правильно')
answer_line = QVBoxLayout()
answer_line.addWidget(is_correct, alignment=Qt.AlignCenter)
answer_group.setLayout(answer_line)
answer_group.hide()

#главный лайаут
line = QVBoxLayout()
line.addWidget(cur_quest, alignment=Qt.AlignRight)
line.addWidget(question, alignment=Qt.AlignCenter)
line.addWidget(group_answers, alignment=Qt.AlignCenter)
line.addWidget(answer_group, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
line.addWidget(help_btn, alignment=Qt.AlignCenter)
line.setSpacing(20)

#устанавливаем лайаут на окно
window.setLayout(line)
window.show()

#ставим случайный вопрос и правильную кнопку
def set_question():
    if len(questions) == 0:
        print("Test Complete!")
    else:
        global c
        global c3
        c += 1
        if c3 == 0:
            help_btn.hide()
        q = choice(questions)
        text_question, a1, a2, a3, a4, correct = q.values()
        question.setText(text_question)
        ans_1.setText(a1)
        ans_2.setText(a2)
        ans_3.setText(a3)
        ans_4.setText(a4)
        window.correct = correct
        questions.pop(questions.index(q))


set_question()

app.exec_()