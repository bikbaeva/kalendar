Для начала установила программу Qt Desinder, в данной программме создала
окно с календарем. 
В меню во вклатке Display Widgets выбираем календарь
и перетаскиваем в редактор. Сохраняем файл в ui файл. 
Затем конвертируем в PYthon запускаем команду в терминале 
В календаре подсвечивается только выбранная дата. 
Чтобы дата была подсвечена постоянно, нужно сделать свой виджет на основе 
встроенного. 
Создаем файл CustomCalendar.py, в котором расширяем класс QtWidgets.QCalendarWidget:

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class MyCalendar(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)

Теперь нужно выделять ячейки в календаре:

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class MyCalendar(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)

    def paintCell(self, painter, rect, date):
        QtWidgets.QCalendarWidget.paintCell(self, painter, rect, date)
        if date == date.currentDate():
            painter.setBrush(QtGui.QColor(0, 200, 200, 50))
            painter.drawRect(rect)

Сначала вызывается метод родителя.
Затем можно добавить то, что нам нужно.

Теперь в файле design.py подключаем модуль CustomCalendar и заменяем QtWidgets.QCalendarWidget на MyCalendar:

from PyQt5 import QtCore, QtGui, QtWidgets
from CustomCalendar import MyCalendar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 502)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.calendarWidget = MyCalendar(self.centralWidget)
        self.calendarWidget.setGeometry(QtCore.QRect(60, 50, 471, 341))
        self.calendarWidget.setObjectName("calendarWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

Чтобы приложение запустилось, нужно создать файл с логикой приложения logic.py:

from PyQt5 import QtWidgets
import sys
import design


class CalendarApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
Запускаем приложение
