from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
from PyQt5.QtGui import QIcon
import pyautogui
  
# window class
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Paint with PyQt5")

        self.setFixedSize(1920, 1080)

        self.setWindowIcon(QIcon('slateicon.ico'))

        self.shapes = []

        # creating image object
        self.image = QImage(self.size(), QImage.Format_RGB32)
  
        # making image color to white
        self.image.fill(Qt.white)
  
        # variables
        # drawing flag
        self.drawing = False
        # default brush size
        self.brushSize = 2
        # default color
        self.brushColor = Qt.black
  
        # QPoint object to tract the point
        self.lastPoint = QPoint()
  
        # creating menu bar
        mainMenu = self.menuBar()
  
        # creating file menu for save and clear action
        fileMenu = mainMenu.addMenu("File")
  
        # adding brush size to main menu
        b_size = mainMenu.addMenu("Brush Size")
  
        # adding brush color to ain menu
        b_color = mainMenu.addMenu("Brush Color")

        b_fill = mainMenu.addMenu("Fill")
  
        # creating save action
        saveAction = QAction("Save", self)
        # adding short cut for save action
        saveAction.setShortcut("Ctrl + S")
        # adding save to the file menu
        fileMenu.addAction(saveAction)
        # adding action to the save
        saveAction.triggered.connect(self.save)

        bl = QAction("black", self)
        b_fill.addAction(bl)
        bl.triggered.connect(self.bla)
  
        # creating clear action
        clearAction = QAction("Clear", self)
        # adding short cut to the clear action
        clearAction.setShortcut("Ctrl + C")
        # adding clear to the file menu
        fileMenu.addAction(clearAction)
        # adding action to the clear
        clearAction.triggered.connect(self.clear)

        pix_4 = QAction("4px", self)
        # adding this action to the brush size
        b_size.addAction(pix_4)
        # adding method to this
        pix_4.triggered.connect(self.Pixel_4)
  
        # similarly repeating above steps for different sizes
        pix_7 = QAction("7px", self)
        b_size.addAction(pix_7)
        pix_7.triggered.connect(self.Pixel_7)
  
        pix_9 = QAction("9px", self)
        b_size.addAction(pix_9)
        pix_9.triggered.connect(self.Pixel_9)
  
        pix_12 = QAction("12px", self)
        b_size.addAction(pix_12)
        pix_12.triggered.connect(self.Pixel_12)

        pix_15 = QAction("15px", self)
        b_size.addAction(pix_15)
        pix_15.triggered.connect(self.Pixel_15)

        huge = QAction("Humungous", self)
        b_size.addAction(huge)
        huge.triggered.connect(self.big)

        black = QAction("Black", self)
        b_color.addAction(black)
        black.triggered.connect(self.blackColor)
  
        green = QAction("Green", self)
        b_color.addAction(green)
        green.triggered.connect(self.greenColor)
  
        yellow = QAction("Yellow", self)
        b_color.addAction(yellow)
        yellow.triggered.connect(self.yellowColor)
  
        red = QAction("Red", self)
        b_color.addAction(red)
        red.triggered.connect(self.redColor)

        white = QAction("Eraser", self)
        b_color.addAction(white)
        white.triggered.connect(self.whiteColor)
  
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
  
    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
  
        if event.button() == Qt.LeftButton:
            # make drawing flag false
            self.drawing = False
  
    # paint event
    def paintEvent(self, event):
        # create a canvas
        canvasPainter = QPainter(self)

        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
  
    # method for saving canvas
    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                          "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
  
        if filePath == "":
            return
        self.image.save(filePath)
  
    # method for clearing every thing on canvas
    def clear(self):
        # make the whole canvas white
        self.image.fill(Qt.white)
        # update
        self.update()

    def bla(self):
        # make the whole canvas white
        self.image.fill(Qt.black)
        # update
        self.update()
  
    # methods for changing pixel sizes
    def Pixel_4(self):
        self.brushSize = 4
  
    def Pixel_7(self):
        self.brushSize = 7
  
    def Pixel_9(self):
        self.brushSize = 9
  
    def Pixel_12(self):
        self.brushSize = 12

    def Pixel_15(self):
        self.brushSize = 15

    def big(self):
        self.brushSize = 150
  
    # methods for changing brush color
    def blackColor(self):
        self.brushColor = Qt.black
  
    def whiteColor(self):
        self.brushColor = Qt.white
  
    def greenColor(self):
        self.brushColor = Qt.green
  
    def yellowColor(self):
        self.brushColor = Qt.yellow
  
    def redColor(self):
        self.brushColor = Qt.red
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# showing the window
window.showMaximized()
  
# start the app
sys.exit(App.exec())
