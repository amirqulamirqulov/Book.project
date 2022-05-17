from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5

from models import Book_type

class Book_typeWindow(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlags(PyQt5.QtCore.Qt.Window)
        self.setWindowTitle('Book_type')
        self.row_count = 0

        self.initUI()

        self.sel_Book_type = None

    def initUI(self):
        self.setGeometry(100, 100, 400, 400)

        self.ql_Book_type_name = QLabel(self)
        self.ql_Book_type_name.setText("Book_type Name: ")
        self.ql_Book_type_name.move(30, 30)

        self.qle_Book_type_name = QLineEdit(self)
        self.qle_Book_type_name.move(120, 30)

        self.btn_add = QPushButton('Add', self)
        self.btn_add.move(300, 30)
        self.btn_add.clicked.connect(self.onAdd)

        self.btn_update = QPushButton('Update', self)
        self.btn_update.move(300, 60)
        self.btn_update.clicked.connect(self.onUpdate)

        self.btn_delete = QPushButton('Delete', self)
        self.btn_delete.move(300, 90)
        self.btn_delete.clicked.connect(self.onDelete)

        self.table = QTableWidget(self)  # Создаём таблицу
        self.table.move(30, 60)
        self.table.setColumnCount(2)     # Устанавливаем три колонки

        # Устанавливаем заголовки таблицы
        self.table.setHorizontalHeaderLabels(['Id', "Book_type name"])

        # Устанавливаем всплывающие подсказки на заголовки
        self.table.horizontalHeaderItem(0).setToolTip("This is Book_type name")

        self.table.hideColumn(0)

        # Устанавливаем выравнивание на заголовки
        self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)

        # заполняем первую строку
        for book in Book_type.objects():
            self.table.setRowCount(self.row_count + 1)
            self.table.setItem(self.row_count, 0,
                               QTableWidgetItem(str(book.id)))
            self.table.setItem(self.row_count, 1,
                               QTableWidgetItem(str(book)))
            self.row_count += 1

        # делаем ресайз колонок по содержимому
        self.table.resizeColumnsToContents()
        self.table.clicked.connect(self.onClicked)

    def onAdd(self):
        reg = Book_type(self.qle_Book_type_name.text())
        reg.save()
        self.table.setRowCount(self.row_count + 1)
        self.table.setItem(self.row_count, 0,
                           QTableWidgetItem(str(reg.id)))
        self.table.setItem(self.row_count, 1,
                           QTableWidgetItem(str(reg.Name)))
        self.row_count += 1

    def onUpdate(self):
        if self.sel_Book_type is not None:
            self.sel_Book_type.Name = self.qle_Book_type_name.text()
            self.sel_Book_type.save()
            self.table.setItem(
                self.sel_row, 1, QTableWidgetItem(str(self.sel_Book_type)))

    def onDelete(self):
        if self.sel_Book_type is not None:
            self.sel_Book_type.delete()
            self.sel_Book_type = None
            self.table.removeRow(self.sel_row)

    def onClicked(self, item):
        self.sel_row = self.table.currentRow()
        self.qle_Book_type_name.setText(self.table.item(self.sel_row, 1).text())

        self.sel_Book_type = Book_type(self.table.item(
            self.sel_row, 1).text(), self.table.item(self.sel_row, 0).text())
