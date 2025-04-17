from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout

app = QApplication([])
win = QWidget()
win.resize(700, 500)
imege = QLabel("Картинка")
btn = QPushButton("Папка")
files = QListWidget()

btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_mirror = QPushButton("Дзеркало")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")

a = QHBoxLayout()
b = QVBoxLayout()
c = QVBoxLayout()

b.addWidget(btn)
b.addWidget(files)
c.addWidget(imege, alignment=Qt.AlignCenter)

a_tools = QHBoxLayout()
a_tools.addWidget(btn_left)
a_tools.addWidget(btn_right)
a_tools.addWidget(btn_mirror)
a_tools.addWidget(btn_sharp)
a_tools.addWidget(btn_bw)

c.addLayout(a_tools)

a.addLayout(b, 1)  
a.addLayout(c, 3) 
win.setLayout(a)
win.show()
app.exec()