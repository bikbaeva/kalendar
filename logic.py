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