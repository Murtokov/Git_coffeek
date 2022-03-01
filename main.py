import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):

        super().__init__()

        uic.loadUi('main.ui', self)

        self.pushButton.clicked.connect(self.search)

    def search(self, event):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee""").fetchall()
        con.close()

        head = ['ID', 'название сорта', 'тепень обжарки', 'молотый/в зернах',
                'описание вкуса', 'цена', 'объем упаковки']

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)

        for e, i in enumerate(head):
            self.tableWidget.setHorizontalHeaderItem(e, QTableWidgetItem(str(i)))

        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
