# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'note_picker.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import gnp_code as gnp


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 450)
        MainWindow.setWindowIcon(QtGui.QIcon(
            'projects/guitar note picker/guitar-512.png'
        ))

        self.font_main = QtGui.QFont()
        self.font_main.setFamily("Calibri Light")
        self.font_main.setPointSize(16)

        self.font_bold = QtGui.QFont()
        self.font_bold.setFamily("Calibri Light")
        self.font_bold.setPointSize(16)
        self.font_bold.setBold(True)
        self.font_bold.setItalic(True)
        self.font_bold.setWeight(75)

        self.font_small = QtGui.QFont()
        self.font_small.setFamily("Calibri Light")
        self.font_small.setPointSize(12)
        self.font_small.setBold(True)
        self.font_small.setItalic(True)
        self.font_small.setWeight(75)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pB_generate = QtWidgets.QPushButton(self.centralwidget)
        self.pB_generate.setGeometry(QtCore.QRect(100, 20, 250, 50))
        self.pB_generate.setFont(self.font_main)
        self.pB_generate.clicked.connect(self.pick_note)
        self.pB_generate.setObjectName("pB_generate")

        self.pB_answer = QtWidgets.QPushButton(self.centralwidget)
        self.pB_answer.setGeometry(QtCore.QRect(100, 180, 250, 50))
        self.pB_answer.setFont(self.font_main)
        self.pB_answer.clicked.connect(self.show_answer)
        self.pB_answer.setObjectName("pB_answer")

        self.f_upper = QtWidgets.QFrame(self.centralwidget)
        self.f_upper.setGeometry(QtCore.QRect(75, 75, 300, 100))
        self.f_upper.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_upper.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.f_upper.setObjectName("f_upper")

        self.l_text1 = QtWidgets.QLabel(self.f_upper)
        self.l_text1.setGeometry(QtCore.QRect(125, 10, 90, 30))
        self.l_text1.setFont(self.font_main)
        self.l_text1.setAlignment(QtCore.Qt.AlignCenter)
        self.l_text1.setObjectName("l_text1")

        self.l_note1 = QtWidgets.QLabel(self.f_upper)
        self.l_note1.setGeometry(QtCore.QRect(75, 10, 50, 30))
        self.l_note1.setFont(self.font_bold)
        self.l_note1.setAlignment(QtCore.Qt.AlignCenter)
        self.l_note1.setObjectName("l_note1")

        self.l_text2 = QtWidgets.QLabel(self.f_upper)
        self.l_text2.setGeometry(QtCore.QRect(125, 50, 90, 35))
        self.l_text2.setFont(self.font_main)
        self.l_text2.setAlignment(QtCore.Qt.AlignCenter)
        self.l_text2.setObjectName("l_text2")

        self.l_string1 = QtWidgets.QLabel(self.f_upper)
        self.l_string1.setGeometry(QtCore.QRect(75, 50, 50, 35))
        self.l_string1.setFont(self.font_bold)
        self.l_string1.setAlignment(QtCore.Qt.AlignCenter)
        self.l_string1.setObjectName("l_string1")

        self.f_lower = QtWidgets.QFrame(self.centralwidget)
        self.f_lower.setGeometry(QtCore.QRect(25, 235, 400, 150))
        self.f_lower.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.f_lower.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.f_lower.setObjectName("f_lower")

        self.l_note_ans = QtWidgets.QLabel(self.f_lower)
        self.l_note_ans.setGeometry(QtCore.QRect(115, 10, 50, 30))
        self.l_note_ans.setFont(self.font_bold)
        self.l_note_ans.setAlignment(QtCore.Qt.AlignCenter)
        self.l_note_ans.setObjectName("l_note_ans")

        self.l_text3 = QtWidgets.QLabel(self.f_lower)
        self.l_text3.setGeometry(QtCore.QRect(165, 10, 120, 30))
        self.l_text3.setFont(self.font_main)
        self.l_text3.setAlignment(QtCore.Qt.AlignCenter)
        self.l_text3.setObjectName("l_text3")

        self.l_fret2 = QtWidgets.QLabel(self.f_lower)
        self.l_fret2.setGeometry(QtCore.QRect(260, 50, 120, 35))
        self.l_fret2.setFont(self.font_bold)
        self.l_fret2.setAlignment(QtCore.Qt.AlignCenter)
        self.l_fret2.setObjectName("l_fret2")

        self.l_text4 = QtWidgets.QLabel(self.f_lower)
        self.l_text4.setGeometry(QtCore.QRect(140, 50, 100, 35))
        self.l_text4.setFont(self.font_main)
        self.l_text4.setAlignment(QtCore.Qt.AlignCenter)
        self.l_text4.setObjectName("l_text4")

        self.l_fret1 = QtWidgets.QLabel(self.f_lower)
        self.l_fret1.setGeometry(QtCore.QRect(10, 50, 120, 35))
        self.l_fret1.setFont(self.font_bold)
        self.l_fret1.setAlignment(QtCore.Qt.AlignCenter)
        self.l_fret1.setObjectName("l_fret1")

        self.l_string_ans = QtWidgets.QLabel(self.f_lower)
        self.l_string_ans.setGeometry(QtCore.QRect(170, 100, 50, 35))
        self.l_string_ans.setFont(self.font_bold)
        self.l_string_ans.setAlignment(QtCore.Qt.AlignCenter)
        self.l_string_ans.setObjectName("l_string_ans")

        self.l_text5 = QtWidgets.QLabel(self.f_lower)
        self.l_text5.setGeometry(QtCore.QRect(85, 100, 90, 35))
        self.l_text5.setFont(self.font_main)
        self.l_text5.setAlignment(QtCore.Qt.AlignCenter)
        self.l_text5.setObjectName("l_text5")

        self.l_text6 = QtWidgets.QLabel(self.f_lower)
        self.l_text6.setGeometry(QtCore.QRect(220, 100, 90, 35))
        self.l_text6.setFont(self.font_main)
        self.l_text6.setAlignment(QtCore.Qt.AlignCenter)
        self.l_text6.setObjectName("l_text6")

        self.f_lower.raise_()
        self.f_upper.raise_()
        self.pB_generate.raise_()
        self.pB_answer.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Find a Note"))
        self.pB_generate.setText(_translate("MainWindow", "Find a..."))
        self.pB_answer.setText(_translate("MainWindow", "Answer"))
        self.l_text1.setText(_translate("MainWindow", ""))
        self.l_note1.setText(_translate("MainWindow", ""))
        self.l_text2.setText(_translate("MainWindow", ""))
        self.l_string1.setText(_translate("MainWindow", ""))
        self.l_note_ans.setText(_translate("MainWindow", ""))
        self.l_text3.setText(_translate("MainWindow", ""))
        self.l_fret2.setText(_translate("MainWindow", ""))
        self.l_text4.setText(_translate("MainWindow", ""))
        self.l_fret1.setText(_translate("MainWindow", ""))
        self.l_string_ans.setText(_translate("MainWindow", ""))
        self.l_text6.setText(_translate("MainWindow", ""))
        self.l_text5.setText(_translate("MainWindow", ""))

    def pick_note(self):
        self.note_string = gnp.pick_note(raw=True)

        _translate = QtCore.QCoreApplication.translate
        self.l_note1.setText(_translate("MainWindow", self.note_string[0]))
        self.l_string1.setText(_translate("MainWindow", self.note_string[1]))
        self.l_text1.setText(_translate("MainWindow", "on the"))
        self.l_text2.setText(_translate("MainWindow", "string."))

        self.l_note_ans.setText(_translate("MainWindow", ""))
        self.l_string_ans.setText(_translate("MainWindow", ""))
        self.l_fret1.setText(_translate("MainWindow", ""))
        self.l_fret2.setText(_translate("MainWindow", ""))
        self.l_text3.setText(_translate("MainWindow", ""))
        self.l_text4.setText(_translate("MainWindow", ""))
        self.l_text5.setText(_translate("MainWindow", ""))
        self.l_text6.setText(_translate("MainWindow", ""))

    def show_answer(self):
        try:
            self.note_string is True
            frets = gnp.pick_note_answer(self.note_string, raw=True)

            for i in [0, 1]:
                if frets[i] == 0:
                    frets[i] = 'open string'
                elif frets[i] == 1:
                    frets[i] = '1st fret'
                elif frets[i] == 2:
                    frets[i] = '2nd fret'
                elif frets[i] == 3:
                    frets[i] = '3rd fret'
                else:
                    frets[i] = '{}th fret'.format(frets[i])

            _translate = QtCore.QCoreApplication.translate
            self.l_note_ans.setText(_translate("MainWindow",
                                               self.note_string[0]))
            self.l_string_ans.setText(_translate("MainWindow",
                                                 self.note_string[1]))
            self.l_fret1.setText(_translate("MainWindow", frets[0]))
            self.l_fret2.setText(_translate("MainWindow", frets[1]))
            self.l_text3.setText(_translate("MainWindow", "is on the"))
            self.l_text4.setText(_translate("MainWindow", "and the"))
            self.l_text5.setText(_translate("MainWindow", "of the"))
            self.l_text6.setText(_translate("MainWindow", "string."))
            if frets[0] == 'open string':
                self.l_fret1.setFont(self.font_small)
            else:
                self.l_fret1.setFont(self.font_bold)

        except Exception:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
