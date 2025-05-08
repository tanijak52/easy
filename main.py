from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PIL import ImageEnhance
import os

app = QApplication([])
win = QWidget()
win.resize(700, 500)
image = QLabel("Картинка")
btn = QPushButton("Папка")
files = QListWidget()
workdir = "None"

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
vl_c.addWidget(image, 95 )

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

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"
        self.fullname = None

    def loadImage(self, dir, filename):
        self.filename = filename
        self.dir = dir
        path = os.path.join(self.dir, self.filename)
        self.image = path
        self.fullname = path

    def showImage(self):
        image.hide()
        pixmapimage = QPixmap(self.fullname)
        w, h = image.width(), image.height()
        pixmapimage =  pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        image.setPixmap(pixmapimage)
        image.show()

    def saveImage(self):
        save_path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(save_path) or os.path.isdir(save_path)): 
            os.mkdir(save_path)
        self.image.save(os.path.join(save_path, self.filename))

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def do_sharp(self):
        self.image = self.image()
        self.image = ImageEnhance.Contrast(image)
        self.image = image.enhance(1.5)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_mirror(self):
        self.mirrored_image = image.transpose(image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_right(self):
        self.rotated_image = image.transpose(image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_left(self):
        self.rotated_left = image.transpose(image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)



def filter(files, extensions):
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
    extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp', '.avif']
    ChosseWorkdir()
    filenames = filter(os.listdir(workdir),extensions)
    files.clear()
    for filename in filenames:
        files.addItem(filename)

workImage = ImageProcessor()

def showChosenImage():
    if files.currentRow () >= 0:
        filename = files.currentItem().text()
        workImage.loadImage(workdir, filename)
        workImage.showImage()


files.currentRowChanged.connect(showChosenImage)
btn.clicked.connect(ShowFiles)
btn_bw.clicked.connect(workImage.do_bw)
btn_sharp.clicked.connect(workImage.do_sharp)
btn_mirror.clicked.connect(workImage.do_mirror)
btn_right.clicked.connect(workImage.do_right)
btn_left.clicked.connect(workImage.do_left)
win.show()
app.exec()