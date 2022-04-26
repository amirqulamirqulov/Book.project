from models import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from windows.BookWindow import Book_typeWindow
from windows.Book_name import Book_nameWindow
from windows.BooksWindow import BookWindow

class Window(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.initActions()
        self.initMenu()

    def initActions(self):
        self.newAction = QAction("&New...", self)
        self.openAction = QAction("&Open...", self)
        self.saveAction = QAction("&Save", self)
        self.exitAction = QAction("&Exit", self)

        self.Book_typeAction = QAction("&Book_type", self)
        self.Book_typeAction.triggered.connect(self.onBook_typeWindow)
        self.Book_nameAction = QAction("&Book_name", self)
        self.Book_nameAction.triggered.connect(self.onBook_nameWindow)
        self.BookAction = QAction("&Book", self)
        self.BookAction.triggered.connect(self.onBookWindow)


    def initMenu(self):
        menuBar = self.menuBar()
        self.setMenuBar(menuBar)

        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)

        bookMenu = menuBar.addMenu("&Book")
        bookMenu.addAction(self.Book_typeAction)
        bookMenu.addAction(self.Book_nameAction)
        bookMenu.addAction(self.BookAction)

        helpMenu = menuBar.addMenu("&Help")
    
    def onBook_typeWindow(self):
        self.bookw = Book_typeWindow()
        self.bookw.showNormal()

    def onBook_nameWindow(self):
        self.bookw = Book_nameWindow()
        self.bookw.showNormal()

    def onBookWindow(self):
        self.bookw = BookWindow()
        self.bookw.showMaximized()


app = QApplication(sys.argv)
w = Window()
w.showMaximized()
app.exec()