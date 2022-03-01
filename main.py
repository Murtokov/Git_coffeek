import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, \
    QLabel, QLineEdit, QComboBox, QDialog, QPushButton
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):

        super().__init__()

        uic.loadUi('addEditCoffeeForm.ui', self)

        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.run2)

    def search(self):
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

    def run(self):
        dlg = QDialog()
        dlg.resize(375, 320)

        lbl = QLabel('ID:', dlg)
        lbl.move(10, 10)

        lbl2 = QLabel('Название сорта:', dlg)
        lbl2.move(10, 50)

        lbl3 = QLabel('Степень обжарки:', dlg)
        lbl3.move(10, 90)

        lbl4 = QLabel('Молотый/в зёрнах:', dlg)
        lbl4.move(10, 130)

        lbl5 = QLabel('Описание вкуса:', dlg)
        lbl5.move(10, 170)

        lbl6 = QLabel('Цена:', dlg)
        lbl6.move(10, 210)

        lbl7 = QLabel('Объём упаковки:', dlg)
        lbl7.move(10, 250)

        self.le = QLineEdit(dlg)
        self.le.move(120, 10)
        self.le.resize(200, 20)

        self.le2 = QLineEdit(dlg)
        self.le2.move(120, 50)
        self.le2.resize(200, 20)

        self.le3 = QLineEdit(dlg)
        self.le3.move(120, 90)
        self.le3.resize(200, 20)

        self.le4 = QLineEdit(dlg)
        self.le4.move(120, 130)
        self.le4.resize(200, 20)

        self.le5 = QLineEdit(dlg)
        self.le5.move(120, 170)
        self.le5.resize(200, 20)

        self.le6 = QLineEdit(dlg)
        self.le6.move(120, 210)
        self.le6.resize(200, 20)

        self.le7 = QLineEdit(dlg)
        self.le7.move(120, 250)
        self.le7.resize(200, 20)

        self.btn = QPushButton('Добавить', dlg)
        self.btn.move(10, 280)
        self.btn.resize(100, 30)
        self.btn.clicked.connect(self.work)

        dlg.setWindowTitle("Добавить элемент")
        dlg.exec_()

    def work(self):
        self.ID = str(self.le.text())
        self.nazv_sorta = "'" + str(self.le2.text()) + "'"
        self.step_obzh = "'" + str(self.le3.text()) + "'"
        self.mol_zern = "'" + str(self.le4.text()) + "'"
        self.opis_vk = "'" + str(self.le5.text()) + "'"
        self.cen = str(self.le6.text())
        self.obem = "'" + str(self.le7.text()) + "'"

        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT ID FROM coffee""").fetchall()
        con.close()
        result = [str(i[0]) for i in result]
        if self.ID in result:
            pass
        else:
            con = sqlite3.connect("coffee.sqlite")
            cur = con.cursor()
            sql = f"INSERT INTO coffee (ID, nazv, step," \
                  f" mol, opis, price, obem)" \
                  f" VALUES({self.ID}, {self.nazv_sorta}, {self.step_obzh}, {self.mol_zern}" \
                  f", {self.opis_vk}, {self.cen}, {self.obem})"

            # res =  cur.execute("""SELECT * FROM coffee""").fetchall()
            #
            # sql = "INSERT INTO coffee(ID, nazv) VALUES(2, 'sdss')"
            cur.execute(sql)
            con.commit()

    def run2(self):
        dlg2 = QDialog()
        dlg2.resize(375, 320)

        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT ID FROM coffee""").fetchall()
        con.close()

        lbl = QLabel('ID:', dlg2)
        lbl.move(10, 10)

        lbl2 = QLabel('Название сорта:', dlg2)
        lbl2.move(10, 50)

        lbl3 = QLabel('Степень обжарки:', dlg2)
        lbl3.move(10, 90)

        lbl4 = QLabel('Молотый/в зёрнах:', dlg2)
        lbl4.move(10, 130)

        lbl5 = QLabel('Описание вкуса:', dlg2)
        lbl5.move(10, 170)

        lbl6 = QLabel('Цена:', dlg2)
        lbl6.move(10, 210)

        lbl7 = QLabel('Объём упаковки:', dlg2)
        lbl7.move(10, 250)

        self.sel = QComboBox(dlg2)
        self.sel.addItems((str(tmp_[0]) for tmp_ in result))
        self.sel.move(120, 10)
        self.sel.resize(200, 20)

        self.le2 = QLineEdit(dlg2)
        self.le2.move(120, 50)
        self.le2.resize(200, 20)

        self.le3 = QLineEdit(dlg2)
        self.le3.move(120, 90)
        self.le3.resize(200, 20)

        self.le4 = QLineEdit(dlg2)
        self.le4.move(120, 130)
        self.le4.resize(200, 20)

        self.le5 = QLineEdit(dlg2)
        self.le5.move(120, 170)
        self.le5.resize(200, 20)

        self.le6 = QLineEdit(dlg2)
        self.le6.move(120, 210)
        self.le6.resize(200, 20)

        self.le7 = QLineEdit(dlg2)
        self.le7.move(120, 250)
        self.le7.resize(200, 20)

        self.btn = QPushButton('Добавить', dlg2)
        self.btn.move(10, 280)
        self.btn.resize(100, 30)
        self.btn.clicked.connect(self.work2)

        dlg2.setWindowTitle("Изменить элемент")
        dlg2.exec_()

    def work2(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        self.ID = str(self.sel.currentText())
        result = cur.execute(f"""SELECT * FROM coffee WHERE ID = {self.ID}""").fetchall()

        try:
            self.nazv_sorta = "'" + str(self.le2.text()) + "'"
            if self.nazv_sorta != "''":
                result = f"UPDATE coffee " \
                      f"SET nazv = {self.nazv_sorta} " \
                      f"WHERE ID = {self.ID}"
                cur.execute(result)
                con.commit()
        except:
            pass

        try:
            self.step_obzh = "'" + str(self.le3.text()) + "'"
            if self.step_obzh != "''":
                result = f"UPDATE coffee " \
                      f"SET step = {self.step_obzh} " \
                      f"WHERE ID = {self.ID}"
                cur.execute(result)
                con.commit()
        except:
            pass

        try:
            self.mol_zern = "'" + str(self.le4.text()) + "'"
            if self.mol_zern != "''":
                result = f"UPDATE coffee " \
                      f"SET mol = {self.mol_zern} " \
                      f"WHERE ID = {self.ID}"
                cur.execute(result)
                con.commit()
        except:
            pass

        try:
            self.opis_vk = "'" + str(self.le5.text()) + "'"
            if self.opis_vk != "''":
                result = f"UPDATE coffee " \
                      f"SET opis = {self.opis_vk} " \
                      f"WHERE ID = {self.ID}"
                cur.execute(result)
                con.commit()
        except:
            pass

        try:
            self.cen = str(self.le6.text())
            if self.cen != "''":
                result = f"UPDATE coffee " \
                      f"SET cen = {self.cen} " \
                      f"WHERE ID = {self.ID}"
                cur.execute(result)
                con.commit()
        except:
            pass
        try:
            self.obem = "'" + str(self.le7.text()) + "'"
            if self.obem != "''":
                result = f"UPDATE coffee " \
                      f"SET obem = {self.obem} " \
                      f"WHERE ID = {self.ID}"
                cur.execute(result)
                con.commit()
        except:
            pass

        # con = sqlite3.connect("coffee.sqlite")
        # cur = con.cursor()
        # sql1 = f"DELETE from films where ID = {self.ID}"
        # sql = f"INSERT INTO coffee (ID, nazv, step," \
        #       f" mol, opis, price, obem)" \
        #       f" VALUES({self.ID}, {self.nazv_sorta}, {self.step_obzh}, {self.mol_zern}" \
        #       f", {self.opis_vk}, {self.cen}, {self.obem})"
        #
        # print(sql)
        # cur.execute(sql1)
        # cur.execute(sql)
        # con.commit()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())