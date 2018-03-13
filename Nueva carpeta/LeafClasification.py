# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pqtDesigner.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Leaf_Classification(object):
    def setupUi(self, Leaf_Classification):
        Leaf_Classification.setObjectName(_fromUtf8("Leaf_Classification"))
        Leaf_Classification.resize(700, 400)
        Leaf_Classification.setMinimumSize(QtCore.QSize(600, 400))
        Leaf_Classification.setMaximumSize(QtCore.QSize(700, 400))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setBold(True)
        font.setWeight(75)
        Leaf_Classification.setFont(font)
        self.label = QtGui.QLabel(Leaf_Classification)
        self.label.setGeometry(QtCore.QRect(180, 0, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lbluploadPhoto = QtGui.QLabel(Leaf_Classification)
        self.lbluploadPhoto.setGeometry(QtCore.QRect(20, 60, 241, 191))
        self.lbluploadPhoto.setAcceptDrops(True)
        self.lbluploadPhoto.setAlignment(QtCore.Qt.AlignCenter)
        self.lbluploadPhoto.setObjectName(_fromUtf8("lbluploadPhoto"))
        self.btnUploadPhoto = QtGui.QPushButton(Leaf_Classification)
        self.btnUploadPhoto.setGeometry(QtCore.QRect(170, 280, 101, 41))
        self.btnUploadPhoto.setObjectName(_fromUtf8("btnUploadPhoto"))
        self.btnDeletePhoto = QtGui.QPushButton(Leaf_Classification)
        self.btnDeletePhoto.setGeometry(QtCore.QRect(30, 280, 101, 41))
        self.btnDeletePhoto.setObjectName(_fromUtf8("btnDeletePhoto"))
        self.lblResultPhoto = QtGui.QLabel(Leaf_Classification)
        self.lblResultPhoto.setGeometry(QtCore.QRect(370, 110, 271, 211))
        self.lblResultPhoto.setText(_fromUtf8(""))
        self.lblResultPhoto.setObjectName(_fromUtf8("lblResultPhoto"))
        self.btnPreprocess = QtGui.QPushButton(Leaf_Classification)
        self.btnPreprocess.setGeometry(QtCore.QRect(30, 350, 241, 31))
        self.btnPreprocess.setObjectName(_fromUtf8("btnPreprocess"))
        self.label_5 = QtGui.QLabel(Leaf_Classification)
        self.label_5.setGeometry(QtCore.QRect(450, 80, 131, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.btnNaivesBayes = QtGui.QPushButton(Leaf_Classification)
        self.btnNaivesBayes.setGeometry(QtCore.QRect(370, 342, 131, 41))
        self.btnNaivesBayes.setObjectName(_fromUtf8("btnNaivesBayes"))
        self.pushButton_5 = QtGui.QPushButton(Leaf_Classification)
        self.pushButton_5.setGeometry(QtCore.QRect(520, 340, 131, 41))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.retranslateUi(Leaf_Classification)
        QtCore.QMetaObject.connectSlotsByName(Leaf_Classification)

    def retranslateUi(self, Leaf_Classification):
        Leaf_Classification.setWindowTitle(_translate("Leaf_Classification", "Leaf Classification", None))
        self.label.setText(_translate("Leaf_Classification", "Leaves Classifcation Software", None))
        self.lbluploadPhoto.setText(_translate("Leaf_Classification", "Upload photo here", None))
        self.btnUploadPhoto.setText(_translate("Leaf_Classification", "Upload Photo", None))
        self.btnDeletePhoto.setText(_translate("Leaf_Classification", "Delete", None))
        self.btnPreprocess.setText(_translate("Leaf_Classification", "Preprocess", None))
        self.label_5.setText(_translate("Leaf_Classification", "Classification Result", None))
        self.btnNaivesBayes.setText(_translate("Leaf_Classification", "NaivesBayes", None))
        self.pushButton_5.setText(_translate("Leaf_Classification", "Random Forest", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Leaf_Classification = QtGui.QWidget()
    ui = Ui_Leaf_Classification()
    ui.setupUi(Leaf_Classification)
    Leaf_Classification.show()
    sys.exit(app.exec_())

