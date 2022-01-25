from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QGroupBox, QButtonGroup
from random import shuffle, randint
from sys import exit
from time import sleep

class Question():
    def __init__ (self, question, right_answer, wrong1, wrong2, wrong3):   
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3          

def check_results():
    if answers[0].isChecked():
        LabelAnswer.setText ("Правильно!")
        window.total += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        LabelAnswer.setText ("Неправильно")
        window.score += 1

def choise():
    if answer.text() == "Наступне питання":
        next_question ()
    else:
        show_results ()

def show_results ():
    check_results ()
    toolbar.hide ()
    toolbar2.show ()
    answer.setText ("Наступне питання")
    
def show_question (): 
    toolbar.show ()
    toolbar2.hide ()
    answer.setText ("Відповісти")
    btngroup.setExclusive (False)
    rbtn1.setChecked (False)
    rbtn2.setChecked (False)
    rbtn3.setChecked (False)
    rbtn4.setChecked (False)
    btngroup.setExclusive (True)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText (q.wrong1)
    answers[2].setText (q.wrong2)
    answers[3].setText (q.wrong3)
    question.setText (q.question)
    show_question ()

def next_question():
    if len (question_list) <= 0:
        msg = QMessageBox ()
        try:
            widsotok = (window.total / (window.total + window.score)) * 100
        except:
            winner = QLabel ("Всі відповіді правильні!")
        msg.setWindowTitle ("Ваші результати:")
        msg.setText ("Відсоток правильних відповідей: " + str(round(widsotok, 0)) + "%")
        msg.exec_ ()

        sleep (10)
        exit ()

    window.cur_quest = randint (0, len (question_list) - 1)
    q = question_list [window.cur_quest]
    ask (q)
    del question_list[window.cur_quest]

question_list = list()
question_list.append(Question ("Скільки буде 3³?", "27", "9", "6", "99"))
question_list.append(Question ("Яким членом речення виражається звертання?", "Воно не є членом речення", "Підмет", "Означення", "Додаток"))
question_list.append(Question ("Скільки годин на добу рослини фотосинтезуються?", "7 год.", "12 год.", "24 год.", "Вони фотосинтезуються увесь час, поки є світло"))
question_list.append(Question ("Який заповідник в Україні найбільший?", "Аскания-Нова", "Канівський заповідник", "Карпатський заповідник", "Ґорґани"))
question_list.append(Question ("Які з цього переліку є легкозаймистими речовинами?", "Папір", "Залізо", "Тканина", "Дерево"))
question_list.append(Question ("Скільки всього областей в Україні (без автономної республіки Крим)?", "24", "20", "8", "40"))
question_list.append(Question ("Що таке віла?", "Степова русалка", "Роскішний будинок за містом", "Знаряддя праці", "Прилад для їжі"))
question_list.append(Question ("Який літак виготовлено в Україні?", "Мрія", "Антей", "Військово-Транспортний літак Ан-12", "Пасажирський літак Ан-24"))
question_list.append(Question ("Який це зв'язок словосполучення?\nвстати зі стільця.", "Керування", "Узгодження", "Прилягання", "Це не словосполучення"))
question_list.append(Question ("Одна з природничих наук.", "Хімія", "Математика", "Істоія", "Українська література"))

app = QApplication ([])
window = QWidget ()
toolbar = QGroupBox ("Варіанти відповідей:")
toolbar2 = QGroupBox ("Результат:")
toolbar2.hide()
window.setWindowTitle ("Пам'ятні картки - українська версія")
rbtn1 = QRadioButton ("Київ")
rbtn2 = QRadioButton ("Одеса")
rbtn3 = QRadioButton ("Запоріжжя")
rbtn4 = QRadioButton ("Львів")

window.total = 0
window.score = 0

LabelAnswer = QLabel ()
LoAnswer = QVBoxLayout ()
LoAnswer.addWidget (LabelAnswer)
toolbar2.setLayout (LoAnswer)
answers = [rbtn1, rbtn2, rbtn3, rbtn4]

btngroup = QButtonGroup ()
btngroup.addButton (rbtn1)
btngroup.addButton (rbtn2)
btngroup.addButton (rbtn3)
btngroup.addButton (rbtn4)

vl1 = QVBoxLayout ()
vl2 = QVBoxLayout ()
hl1 = QHBoxLayout ()

vl1.addWidget (rbtn1)
vl1.addWidget (rbtn2)
vl2.addWidget (rbtn3)
vl2.addWidget (rbtn4)
hl1.addLayout (vl1)
hl1.addLayout (vl2)
toolbar.setLayout (hl1)
question = QLabel ("Яке найбрудніше місто в Україні?")
answer = QPushButton ("Відповідь:")


mainline = QVBoxLayout ()
mainline.addWidget (question, alignment = Qt.AlignHCenter)
mainline.setSpacing (30)
mainline.addWidget (toolbar)
mainline.addWidget (toolbar2)
mainline.setSpacing (30)
mainline.addWidget (answer, stretch = 3)

window.cur_quest = 0
next_question ()
window.setLayout (mainline)
answer.clicked.connect (choise)

window.show ()
app.exec_ ()