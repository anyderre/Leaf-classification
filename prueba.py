import cv2
import numpy as np
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtGui import QDialog, QPushButton
from skimage.feature import greycomatrix, greycoprops
import os
import errno
import glob
from PyQt4 import QtGui, QtDesigner


def getFeatures(image):
    G = greycomatrix(np.array(image, dtype=np.uint8), [1], [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4], levels=256)
    leaves = []

    leaves.append([str(greycoprops(G, prop="contrast")[0][0]),
                   str(greycoprops(G, prop="homogeneity")[0][0]),
                   str(greycoprops(G, prop="ASM")[0][0]),
                   str(greycoprops(G, prop="dissimilarity")[0][0]),
                   str(greycoprops(G, prop="energy")[0][0])])

    return leaves


# ARFF Creation
def generateDataset(files):
    try:
        atrributes = ["Contrast", "Homogeneity", "ASM", "Dissimilarity", "Energy"]

        arff = open('LeavesCopy.arff', 'w')
        arff.write('@RELATION Leaf_Classification\n\n')
        for word in atrributes:
            arff.write('@ATTRIBUTE ')
            arff.write(str(word))
            arff.write(' numeric\n')

        arff.write('@ATTRIBUTE class {Aguacate, Guayacan, Coralillo}\n\n')
        arff.write('@DATA\n')
        # Counting word frequencies for each verse
        cont = 0
        for file in files:
            file = cv2.imread(file)
            file = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)
            if cont < 30:
                for l in getFeatures(file):
                    for el in l:
                        arff.write(el + ",")
                    print
                    arff.write("Aguacate\n")
                print "was there Aguacate"
            elif cont < 60:
                for l in getFeatures(file):
                    for el in l:
                        arff.write(el + ",")
                    arff.write("Coralillo\n")
                print "was there Coralillo"
            else:
                for l in getFeatures(file):
                    for el in l:
                        arff.write(el + ",")
                    arff.write("Guayacan\n")
                print "was there Guayacan"
            cont += 1
        return True
    except Exception, e:
        raise Exception(e.message)
    return False


class GetFileFromSystem(QWidget):
    def __init__(self, parent=None):
        super(GetFileFromSystem, self).__init__(parent)
        layout = QVBoxLayout()


        self.label = QLabel("Upload your photo")
        self.addWidget(self.label)

        self.upload = QPushButton("Upload")
        self.upload.clicked.connect(self.getFile)
        layout.addWidget(self.upload)
        self.setLayout(layout)
        self.setWindowTitle("Predict Leaves'Trees")

    def getFile(self):
        filename =QFileDialog.open(self,"Open File", "c:\\Users\\Dany\\Desktop\\", "Image Files (*.jpg *.png *.gif)")
        self.label.setPixmap(QPixmap(filename))


    def b1_clicked(win):
        filename = QtGui.QFileDialog().getOpenFileName(win, "Open File", ".")
        label = QLabel()
        pixMap = QPixmap(filename)
        label.setPixmax(pixMap)
        vBox = QBoxLayout()
        vBox.addWidget(label)
        win.setLayout(vBox)



def main():
    app= QApplication(sys.argv)
    ex = GetFileFromSystem()
    ex.show()
    sys.exit(app.exec_())


files = glob.glob("C:\Users\Dany\PycharmProjects\Proyeto\hojas\*.jpg")

# generateDataset(files)

if __name__ == '__main__':
    main()




























    # print homogeneity
    # print "---"+ str (len(homogeneity))
    # print contrast
    # print "---"+ str (len(contrast))
    # print asm
    # print "---"+ str (len(asm))
    # print dissimilarity
    # print "---"+ str(len(dissimilarity))
    # print energy
    # print "---"+ str (len(energy))
    # print correlation
    # print"--"+ str (len(correlation))




    # print greycoprops(res,"contrast")
    # cv2.imshow("result", res)
