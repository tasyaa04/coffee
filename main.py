import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.sqlite")
        res = self.con.cursor().execute("SELECT * FROM drink").fetchall()    # вывод наборов на экран
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(0, 10)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(6, 40)
        self.tableWidget.setColumnWidth(4, 260)
        self.tableWidget.setColumnWidth(5, 40)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Название"))
        self.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Степень обжарки"))
        self.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Тип"))
        self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem("Описание вкуса"))
        self.tableWidget.setHorizontalHeaderItem(6, QTableWidgetItem("Объём"))
        self.tableWidget.setHorizontalHeaderItem(5, QTableWidgetItem("Цена"))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
