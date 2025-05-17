
#import libraries
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QGroupBox, QButtonGroup
from random import shuffle, choice
class Question():
    def __init__(self, question, r_a, w_a1, w_a2, w_a3):
        self.question = question
        self.right_answer = r_a
        self.wrong_answer1 = w_a1
        self.wrong_answer2 = w_a2
        self.wrong_answer3 = w_a3

questions = []
questions.append(Question('Ктоя?',
                          'УТка',
                          'Медвед',
                          'КОт',
                          'ТАрак'))

questions.append(Question('Где я?',
                          'Болото',
                          'Школа',
                          'Дом',
                          'Холодильник'))

questions.append(Question('FAV_singer?',
                          'kets4eki',
                          'asteria',
                          'odetari', 
                          'lumi'))









# create part
def show_result():
    quesGroup.hide()
    ansGroup.show()
    btn.setText('Следующий вопрос')
    print('СТатистика')
    print('-Всего вопросов:', window.total)
    print('-Правильных ответов:', window.score)
    rating = window.score / window.total * 100
    print('Рейтинг:', rating, '%' )


def show_question():
    ansGroup.hide()
    quesGroup.show()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    r_btn1.setChecked(False)
    r_btn2.setChecked(False)
    r_btn3.setChecked(False)
    r_btn4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()
        
def ask(q:Question):
    shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong_answer1)
    buttons[2].setText(q.wrong_answer2)
    buttons[3].setText(q.wrong_answer3)
    question.setText(q.question)
    answer2.setText(q.right_answer)
    show_question()

def check_answer():
    if buttons[0].isChecked():
        answer1.setText('Правильно')
        window.score +=1
        show_result()
    elif buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():
        answer1.setText('Не правильно')
        show_result()
     
def next_question():
    window.total +=1
    rand_q = choice(questions)
    ask(rand_q)


       


#app
app = QApplication([])

#window
window = QWidget()
window.score = 0
window.total = 0



window.setWindowTitle('Memory card')
window.resize(500, 500)

#window widgets
question = QLabel('ВОпрос')
answer1 = QLabel('Правильно/НЕправильно')
answer2 = QLabel('Правильный ответ')
quesGroup = QGroupBox('Группа1')
ansGroup = QGroupBox('Группа2')
ansGroup.hide()
btn = QPushButton('Ответить')

r_btn1 = QRadioButton('1 варик')
r_btn2 = QRadioButton('2 варик')
r_btn3 = QRadioButton('3 варик')
r_btn4 = QRadioButton('4 варик')
buttons = [r_btn1, r_btn2, r_btn3, r_btn4]
RadioGroup = QButtonGroup()
RadioGroup.addButton(r_btn1)
RadioGroup.addButton(r_btn2)
RadioGroup.addButton(r_btn3)
RadioGroup.addButton(r_btn4)

v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
v_line3 = QVBoxLayout()
v_line4 = QVBoxLayout()
h_line = QHBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()

#add part

#group

#Group1
v_line1.addWidget(r_btn1)
v_line1.addWidget(r_btn3)
v_line2.addWidget(r_btn2)
v_line2.addWidget(r_btn4)

h_line.addLayout(v_line1)
h_line.addLayout(v_line2)

quesGroup.setLayout(h_line)

#Group2
v_line4.addWidget(answer1)
v_line4.addWidget(answer2)

ansGroup.setLayout(v_line4)

#all window
h_line1.addWidget(question, alignment=Qt.AlignCenter)
h_line2.addWidget(quesGroup)
h_line2.addWidget(ansGroup)
h_line3.addWidget(btn, alignment=Qt.AlignCenter)

v_line3.addLayout(h_line1)
v_line3.addLayout(h_line2)
v_line3.addLayout(h_line3)

window.setLayout(v_line3)











next_question()

btn.clicked.connect(start_test)






window.show()
app.exec()