from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
def win():
    win = QMessageBox()
    win.setText("Правильно! \n Ви виграли гіроскутер")
    win.exec()
def lose():
    lose = QMessageBox()
    lose.resize(300,150)
    lose.setWindowTitle("Ні, в 2005 році. \n Ви виграли фірмовий плакат")
    lose.move(300,175)
    lose.exec()


app = QApplication([])

window = QWidget()
window.resize(400,200)
window.setWindowTitle("Конкурс від Crazy People")
window.move(500,275)

question = QLabel("В якому році канал отримав ""золоту кнопку"" від YouTube?")
ans1 = QRadioButton("2005")
ans2 = QRadioButton("2010")
ans3 = QRadioButton("2015")
ans4 = QRadioButton("2020")

line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line.addWidget(question, alignment=Qt.AlignCenter)
line1.addWidget(ans1,alignment=Qt.AlignCenter)
line1.addWidget(ans2,alignment=Qt.AlignCenter)
line2.addWidget(ans3,alignment=Qt.AlignCenter)
line2.addWidget(ans4,alignment=Qt.AlignCenter)

line.addLayout(line1)
line.addLayout(line2)

window.setLayout(line)

window.show()

ans1.clicked.connect(win)
ans2.clicked.connect(lose)
ans3.clicked.connect(lose)
ans4.clicked.connect(lose)

app.exec()