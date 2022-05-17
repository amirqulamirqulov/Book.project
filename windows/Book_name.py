from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5

from models import Book_type, Book_name


class Book_nameWindow(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def onAdd(self):
        book_type = Book_type.get_by_id(self.cbb_book_type.currentData())

        book_name = Book_name(self.le_dist.text(), book_type.id)
        book_name.save()

        row_count = self.table.rowCount()
        self.table.setRowCount(row_count + 1)
        self.table.setItem(row_count, 0,
                           QTableWidgetItem(str(book_type.id)))
        self.table.setItem(row_count, 1,
                           QTableWidgetItem(str(book_type.Name)))
        self.table.setItem(row_count, 2,
                           QTableWidgetItem(str(book_name.id)))
        self.table.setItem(row_count, 3,
                           QTableWidgetItem(str(book_name.Name)))

    def onUpd(self):
        if  self.sel_Book_name  is not None:

            book_name = self.le_dist.text()
            book_id = self.cbb_book_type.currentData()
            book_name_id = int(self.table.item(self.sel_row, 2).text())

            bookk = Book_name(book_name, book_id, book_name_id)
            bookk.save()

            self.fillTable()
            

    def onDel(self):
        if self.sel_Book_name is not None:
            book_name = self.le_dist.text()
            book_id = self.cbb_book_type.currentData()
            book_name_id = int(self.table.item(self.sel_row, 2).text())

            bookk = Book_name(book_name, book_id, book_name_id)
            bookk.delete()

            self.fillTable()


    def initUI(self):

        self.setGeometry(200, 200, 680, 400)
        self.resize(680, 400)

        self.qlb_book_type = QLabel("Book_type", self)
        self.qlb_book_type.move(30, 30)

        self.cbb_book_type = QComboBox(self)
        self.cbb_book_type.move(90, 30)

        self.qlb_dist = QLabel("Book name", self)
        self.qlb_dist.move(310, 30)

        self.le_dist = QLineEdit(self)
        self.le_dist.move(380, 30)

        self.btn_add = QPushButton("Add", self)
        self.btn_add.move(530, 30)
        self.btn_add.clicked.connect(self.onAdd)

        self.btn_upd = QPushButton("Update", self)
        self.btn_upd.move(530, 60)
        self.btn_upd.clicked.connect(self.onUpd)

        self.btn_del = QPushButton("Delete", self)
        self.btn_del.move(530, 90)
        self.btn_del.clicked.connect(self.onDel)

        self.table = QTableWidget(self)
        self.table.setGeometry(30, 60, 480, 300)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ["book id", 'book_type name', 'books id', 'books name'])
        self.table.setRowCount(0)
        self.table.hideColumn(0)
        self.table.hideColumn(2)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setColumnWidth(1, 140)
        self.table.setColumnWidth(3, 150)
        

        for dist in Book_name.objects():
            book_type = dist.Book_type
            row_count = self.table.rowCount()
            self.table.setRowCount(row_count + 1)
            self.table.setItem(row_count, 0,
                               QTableWidgetItem(str(book_type.id)))
            self.table.setItem(row_count, 1,
                               QTableWidgetItem(str(book_type.Name)))
            self.table.setItem(row_count, 2,
                               QTableWidgetItem(str(dist.id)))
            self.table.setItem(row_count, 3,
                               QTableWidgetItem(str(dist.Name)))

        self.table.resizeColumnsToContents()
        self.table.clicked.connect(self.onClicked)

        self.cbb_book_type.currentIndexChanged.connect(self.fillTable)
        for book in Book_type.objects():
            self.cbb_book_type.addItem(book.Name, book.id)


    def onClicked(self, item):
        self.sel_row = self.table.currentRow()
        self.le_dist.setText(self.table.item(self.sel_row, 3).text())

        self.sel_Book_name = Book_name(self.table.item(
            self.sel_row, 3).text(), self.table.item(self.sel_row, 2).text()
            , self.table.item(self.sel_row, 0).text())

        
    

    def fillTable(self):
        self.table.clear()
        self.table.setHorizontalHeaderLabels(
            ["Book_type id", "Book type name", "Bookid", "Book name"])
        self.table.setRowCount(0)
        self.table.hideColumn(0)
        self.table.hideColumn(2)
        current_id = self.cbb_book_type.currentData()
        for book in Book_name.objects():
            if current_id == book.Bookid:
                books = book.Book_type
                rowCount = self.table.rowCount()
                self.table.setRowCount(rowCount + 1)
                self.table.setItem(rowCount, 0,
                                   QTableWidgetItem(str(books.id)))
                self.table.setItem(rowCount, 1,
                                   QTableWidgetItem(str(books.Name)))
                self.table.setItem(rowCount, 2,
                                   QTableWidgetItem(str(book.id)))
                self.table.setItem(rowCount, 3,
                                   QTableWidgetItem(str(book.Name)))
        self.table.resizeColumnsToContents()




        
