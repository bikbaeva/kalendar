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