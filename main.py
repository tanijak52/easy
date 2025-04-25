from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
import os
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

hl_a = QHBoxLayout()
vl_b = QVBoxLayout()
vl_c = QVBoxLayout()

vl_b.addWidget(btn)
vl_b.addWidget(files)
vl_c.addWidget(imege, alignment=Qt.AlignCenter)

hl_a_tools = QHBoxLayout()
hl_a_tools.addWidget(btn_left)
hl_a_tools.addWidget(btn_right)
hl_a_tools.addWidget(btn_mirror)
hl_a_tools.addWidget(btn_sharp)
hl_a_tools.addWidget(btn_bw)

vl_c.addLayout(hl_a_tools)

hl_a.addLayout(vl_b, 1)  
hl_a.addLayout(vl_c, 3) 
win.setLayout(hl_a)

workdir = "None"

def filter(filtres, extensions):
    result = []

    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                result.append(file)
    return result 
def ChosseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

    print("відкрита папка: " +workdir)
def ShowFiles():
    extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
    ChosseWorkdir()
    filenames = filter(os.listdir(workdir),extensions)
    files.clear()
    for filename in filenames:
        files.addItem(filename)




btn.clicked.connect(ShowFiles)
win.show()
app.exec()