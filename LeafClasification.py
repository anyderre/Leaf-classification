# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pqtDesigner.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import cv2
import numpy as np

from PyQt4.QtGui import QDialog, QPushButton
from skimage.feature import greycomatrix, greycoprops
from weka.classifiers import Evaluation

import os
import errno
import glob
from PyQt4 import QtGui, QtDesigner
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier, PredictionOutput, FilteredClassifier
from weka.core.dataset import Instances
from weka.core.classes import Random
from weka.filters import Filter
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import weka.core.serialization as serialization
from weka.attribute_selection import ASSearch, ASEvaluation, AttributeSelection


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
    filename  = ""
    preprocesed =False
    dataNewPhoto =None

    def setupUi(self, Leaf_Classification):
        jvm.start()
        jvm.start(max_heap_size="512m")

        Leaf_Classification.setObjectName(_fromUtf8("Leaf_Classification"))
        Leaf_Classification.resize(700, 400)
        Leaf_Classification.setMinimumSize(QtCore.QSize(700, 700))
        Leaf_Classification.setMaximumSize(QtCore.QSize(700, 700))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setBold(True)
        font.setWeight(75)
        Leaf_Classification.setFont(font)
        self.label = QtGui.QLabel(Leaf_Classification)
        self.label.setGeometry(QtCore.QRect(180, 0, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lbluploadPhoto = QtGui.QLabel(Leaf_Classification)
        self.lbluploadPhoto.setGeometry(QtCore.QRect(30, 60, 241, 191))
        self.lbluploadPhoto.setAcceptDrops(True)
        self.lbluploadPhoto.setAlignment(QtCore.Qt.AlignCenter)
        self.lbluploadPhoto.setStyleSheet("background-color:#56f9b6")
        self.lbluploadPhoto.setAutoFillBackground(True)
        self.lbluploadPhoto.setObjectName(_fromUtf8("lbluploadPhoto"))

        self.lblResultString = QtGui.QLabel(Leaf_Classification)
        self.lblResultString.setGeometry(QtCore.QRect(30, 490, 620, 150))
        self.lblResultString.setAlignment(QtCore.Qt.AlignLeft)
        self.lblResultString.setStyleSheet("background-color:#efd8fa")
        self.lblResultString.setAutoFillBackground(True)
        self.lblResultString.setObjectName(_fromUtf8("lblResultString"))

        self.scrolllArea = QtGui.QScrollArea(Leaf_Classification)
        self.scrolllArea.setGeometry(QtCore.QRect(30, 490, 620, 150))
        self.scrolllArea.setWidget(self.lblResultString)
        self.lblResultString.setObjectName(_fromUtf8("scrollArea"))

        self.lblShowClassResult = QtGui.QLabel(Leaf_Classification)
        self.lblShowClassResult.setGeometry(QtCore.QRect(30, 440, 200, 50))
        self.lblShowClassResult.setAlignment(QtCore.Qt.AlignCenter)
        self.lblShowClassResult.setStyleSheet("background-color:#38f7f1")
        self.lblShowClassResult.setAutoFillBackground(True)
        self.lblShowClassResult.setObjectName(_fromUtf8("lblShowClassResult"))


        self.btnUploadPhoto = QtGui.QPushButton(Leaf_Classification)
        self.btnUploadPhoto.setGeometry(QtCore.QRect(154, 280, 121, 41))
        self.btnUploadPhoto.setObjectName(_fromUtf8("btnUploadPhoto"))
        self.btnDeletePhoto = QtGui.QPushButton(Leaf_Classification)
        self.btnDeletePhoto.setGeometry(QtCore.QRect(30, 280, 101, 41))
        self.btnDeletePhoto.setObjectName(_fromUtf8("btnDeletePhoto"))
        self.lblResultPhoto = QtGui.QLabel(Leaf_Classification)
        self.lblResultPhoto.setGeometry(QtCore.QRect(370, 60, 280, 260))
        self.lblResultPhoto.setStyleSheet("background-color: #56f9b6")
        self.lblResultPhoto.setAutoFillBackground(True)
        self.lblResultPhoto.setText(_fromUtf8(""))
        self.lblResultPhoto.setObjectName(_fromUtf8("lblResultPhoto"))
        self.lblResultPhoto.setAlignment(QtCore.Qt.AlignCenter)
        self.btnPreprocess = QtGui.QPushButton(Leaf_Classification)
        self.btnPreprocess.setGeometry(QtCore.QRect(30, 350, 241, 41))
        self.btnPreprocess.setObjectName(_fromUtf8("btnPreprocess"))
        self.label_5 = QtGui.QLabel(Leaf_Classification)
        self.label_5.setGeometry(QtCore.QRect(340,20, 350, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setBold(True)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.btnNaivesBayes = QtGui.QPushButton(Leaf_Classification)
        self.btnNaivesBayes.setGeometry(QtCore.QRect(370, 342, 131, 41))
        self.btnNaivesBayes.setObjectName(_fromUtf8("btnNaivesBayes"))
        self.btnrandomForest = QtGui.QPushButton(Leaf_Classification)
        self.btnrandomForest.setGeometry(QtCore.QRect(520, 340, 131, 41))
        self.btnrandomForest.setObjectName(_fromUtf8("pushButton_5"))

        self.btnImprovedNaivesBayes = QtGui.QPushButton(Leaf_Classification)
        self.btnImprovedNaivesBayes.setGeometry(QtCore.QRect(370, 385, 280, 41))
        self.btnImprovedNaivesBayes.setObjectName(_fromUtf8("btnImprovedNaivesBayes"))

        self.retranslateUi(Leaf_Classification)
        QtCore.QMetaObject.connectSlotsByName(Leaf_Classification)

        #Getting button event
        self.btnUploadPhoto.connect(self.btnUploadPhoto, QtCore.SIGNAL("clicked()"), self.getFileName)
        self.btnDeletePhoto.clicked.connect(self.deleteFilename)
        self.btnPreprocess.clicked.connect(self.preprocess)
        self.btnNaivesBayes.clicked.connect(self.generateNaiveBayes)
        self.btnImprovedNaivesBayes.clicked.connect(self.generateImprovedNaiveBayes)

        files = glob.glob("C:\Users\Dany\PycharmProjects\Proyeto\hojas\*.jpg")
        #self.buildModel()
        #self.improvedModel()
        self.btnrandomForest.clicked.connect(self.generateRandomForest)

    def retranslateUi(self, Leaf_Classification):
        Leaf_Classification.setWindowTitle(_translate("Leaf_Classification", "Leaf Classification", None))
        self.label.setText(_translate("Leaf_Classification", "Leaves Classifcation Software", None))
        self.lbluploadPhoto.setText(_translate("Leaf_Classification", "Upload photo here", None))
        self.btnUploadPhoto.setText(_translate("Leaf_Classification", "Upload Photo", None))
        self.btnDeletePhoto.setText(_translate("Leaf_Classification", "Delete", None))
        self.btnPreprocess.setText(_translate("Leaf_Classification", "Preprocess", None))
        self.label_5.setText(_translate("Leaf_Classification", "Classification Result", None))
        self.btnNaivesBayes.setText(_translate("Leaf_Classification", "NaivesBayes", None))
        self.btnrandomForest.setText(_translate("Leaf_Classification", "Random Forest", None))
        self.btnImprovedNaivesBayes.setText(_translate("Leaf_Classification","Improved Naive Bayes" , None))

    #building and savving model
    def buildModel(self):
        loader = Loader(classname="weka.core.converters.ArffLoader")
        data = loader.load_file("LeavesCopy.arff")
        data.class_is_last()
        train, test = data.train_test_split(66.0, Random(1))
        cls = Classifier(classname ="weka.classifiers.trees.RandomForest")
        cls1 = Classifier(classname= "weka.classifiers.bayes.NaiveBayes")
        cls.build_classifier(train)
        cls1.build_classifier(train)
        outFile= "randomForest.model"
        outFile2 = "naiveBayes.model"
        serialization.write(outFile, cls)
        serialization.write(outFile2, cls1)

    def improvedModel(self):
        loader = Loader(classname="weka.core.converters.ArffLoader")
        data = loader.load_file("LeavesCopy.arff")
        data.class_is_last()

        remove = Filter(classname="weka.filters.unsupervised.attribute.Remove", options=["-R", "3,5"])
        remove.inputformat(data)
        data = remove.filter(data)

        train, test = data.train_test_split(66.0, Random(1))

        #search = ASSearch(classname="weka.attributeSelection.Ranker", options=["-T", "-1.7976931348623157E308", "-N", "-1"])
        #evaluator = ASEvaluation(classname="weka.attributeSelection.GainRatioAttributeEval")
        remove = Filter(classname="weka.filters.unsupervised.attribute.Remove", options=["-R","2,5"])
        #attsel = AttributeSelection()
        #attsel.search(search)
        #attsel.evaluator(evaluator)
        #attsel.select_attributes(data)
        #print str(attsel.selected_attributes)
        # print str(attsel.results_string)
        pout = PredictionOutput(classname="weka.classifiers.evaluation.output.prediction.PlainText")
        cls = Classifier(classname="weka.classifiers.trees.RandomForest")
        cls1 = Classifier(classname="weka.classifiers.bayes.NaiveBayes")

        # fc = FilteredClassifier()
        # fc.filter = remove
        # fc.classifier =cls
        # fc.classifier= cls1
        #eval = Evaluation(train)
        #eval.evaluate_train_test_split(cls, data, 66.0, Random(1), pout)

        cls.build_classifier(train)
        cls1.build_classifier(train)
        outFile = "randomForestImproved.model"
        outFile2 = "naiveBayesImproved.model"
        serialization.write(outFile, cls)
        serialization.write(outFile2, cls1)

        # Generate Naive Bayes Classification

    def generateImprovedNaiveBayes(self):
        files = glob.glob("/home/anyderre/Documents/Proyeto/Arboles/*.jpg")
        self.lblResultPhoto.setText("")
        self.lblShowClassResult.setText("")
        self.lblResultString.setText("")
        if self.preprocesed:
            loader = Loader(classname="weka.core.converters.ArffLoader")
            self.dataNewPhoto = loader.load_file("newLeaf.arff")
            self.dataNewPhoto.class_is_last()
            remove = Filter(classname="weka.filters.unsupervised.attribute.Remove", options=["-R", "3,5"])
            remove.inputformat(self.dataNewPhoto)
            self.dataNewPhoto = remove.filter(self.dataNewPhoto)

            model = Classifier(jobject=serialization.read("naiveBayesImproved.model"))
            inst = self.dataNewPhoto.get_instance(0)
            pred = model.classify_instance(self.dataNewPhoto.get_instance(0))
            self.label_5.setText("Class Prediction with Naives Bayes Algorithm")
            if str(inst.class_attribute.value(int(pred))) == "Coralillo":
                self.lblResultPhoto.setPixmap(QPixmap(files[0]).scaled(280, 260))
                self.lblShowClassResult.setText(str(inst.class_attribute.value(int(pred))))
                self.lblResultString.setText(_fromUtf8("Nombre cientifico--> Hamelia patens"
                                                       "\nHamelia -> dedica a un escritor frances de planta"
                                                       "\n Patens -> significa extendido"
                                                       "Genero --> Rubiaceae"
                                                       "\nUso--> Hay patentes de medicamentos cuyos principios activos se obtienen del Coralillo "
                                                       "\n       para estimular el sistema inmunológico."
                                                       "\n       En caso de alguna herida o de mordedura de algun animal ponzoñoso.\n"))
            elif str(inst.class_attribute.value(int(pred))) == "Guayacan":
                self.lblResultPhoto.setPixmap(QPixmap(files[1]).scaled(280, 260))
                self.lblShowClassResult.setText(str(inst.class_attribute.value(int(pred))))
                self.lblResultString.setText(_fromUtf8("Genero --> Handroanthus"
                                                       "\n         Tabebuia"
                                                       "\n         Caesalpinia"
                                                       "\n         Guaiacum"
                                                       "\n         Porlieria."
                                                       "\nOrigen-->es un árbol nativo de América tropical, con amplia distribución en las islas del  "
                                                       "\n         Caribe(especialmente Jamaica, Puerto Rico, Cuba y Republica Dominicana), la costa \n"
                                                       "           Caribe de Colombia, Panamá y Venezuela."))
            elif str(inst.class_attribute.value(int(pred))) == "Aguacate":
                self.lblResultPhoto.setPixmap(QPixmap(files[2]).scaled(280, 260))
                self.lblShowClassResult.setText(str(inst.class_attribute.value(int(pred))))
                self.lblResultString.setText(_fromUtf8("Nombre cientifico --> Persea americana\n"
                                                       "Genero -->  Lauraceae\n"
                                                       "Se cultiva en climas tropicales y mediterráneo en todo el mundo"
                                                       "El Aguacate --> Es un árbol perenne bastante grande que puede medir hasta unos 20-25 metros de\n"
                                                       "                altura. Además es muy corpulento y robusto. Posee hojas verdes oscuras muy \n"
                                                       "                brillantes y unas pequeñas flores de color amarillo."
                                                       ))
            else:
                print "Does not exist"
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("You should preprocessed the loaded Photo First ")
            msg.setWindowTitle("Error!!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()


    #Generate Naive Bayes Classification
    def generateNaiveBayes(self):
        files = glob.glob("/home/anyderre/Documents/Proyeto/Arboles/*.jpg")
        self.lblResultPhoto.setText("")
        self.lblShowClassResult.setText("")
        self.lblResultString.setText("")

        if self.preprocesed:
            loader = Loader(classname="weka.core.converters.ArffLoader")
            self.dataNewPhoto = loader.load_file("newLeaf.arff")
            self.dataNewPhoto.class_is_last()
            model = Classifier(jobject=serialization.read("naiveBayes.model"))
            inst =self.dataNewPhoto.get_instance(0)
            pred = model.classify_instance(self.dataNewPhoto.get_instance(0))
            self.label_5.setText("Class Prediction with Naives Bayes Algorithm")

            if str(inst.class_attribute.value(int(pred))) == "Coralillo":
                self.lblResultPhoto.setPixmap(QPixmap(files[0]).scaled(280, 260))
                self.lblShowClassResult.setText(str(inst.class_attribute.value(int(pred))))
                self.lblResultString.setText(_fromUtf8("Nombre cientifico--> Hamelia patens"
                                                       "\nHamelia -> dedica a un escritor frances de planta"
                                                       "\n Patens -> significa extendido"
                                                       "Genero --> Rubiaceae"
                                                       "\nUso--> Hay patentes de medicamentos cuyos principios activos se obtienen del Coralillo "
                                                       "\n       para estimular el sistema inmunológico."
                                                       "\n       En caso de alguna herida o de mordedura de algun animal ponzoñoso.\n"))
            elif str(inst.class_attribute.value(int(pred))) == "Guayacan":
                self.lblResultPhoto.setPixmap(QPixmap(files[1]).scaled(280, 260))
                self.lblShowClassResult.setText(str(inst.class_attribute.value(int(pred))))
                self.lblResultString.setText(_fromUtf8("Genero --> Handroanthus"
                                                       "\n         Tabebuia"
                                                       "\n         Caesalpinia"
                                                       "\n         Guaiacum"
                                                       "\n         Porlieria."
                                                       "\nOrigen-->es un árbol nativo de América tropical, con amplia distribución en las islas del  "
                                                       "\n         Caribe(especialmente Jamaica, Puerto Rico, Cuba y Republica Dominicana), la costa \n"
                                                       "           Caribe de Colombia, Panamá y Venezuela."))
            elif str(inst.class_attribute.value(int(pred))) == "Aguacate":
                self.lblResultPhoto.setPixmap(QPixmap(files[2]).scaled(280, 260))
                self.lblShowClassResult.setText(str(inst.class_attribute.value(int(pred))))
                self.lblResultString.setText(_fromUtf8("Nombre cientifico --> Persea americana\n"
                                                       "Genero -->  Lauraceae\n"
                                                       "Se cultiva en climas tropicales y mediterráneo en todo el mundo"
                                                       "El Aguacate --> Es un árbol perenne bastante grande que puede medir hasta unos 20-25 metros de\n"
                                                       "                altura. Además es muy corpulento y robusto. Posee hojas verdes oscuras muy \n"
                                                       "                brillantes y unas pequeñas flores de color amarillo."
                                                       ))
            else:
                print "Does not exist"
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("You should preprocessed the loaded Photo First ")
            msg.setWindowTitle("Error!!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()


    #Generate Random Forest Classification
    def generateRandomForest(self):
        files = glob.glob("/home/anyderre/Documents/Proyeto/Arboles/*.jpg")
        self.lblResultPhoto.setText("")
        self.lblShowClassResult.setText("")
        self.lblResultString.setText("")
        if self.preprocesed:
            loader = Loader(classname="weka.core.converters.ArffLoader")
            self.dataNewPhoto = loader.load_file("newLeaf.arff")
            self.dataNewPhoto.class_is_last()
            model = Classifier(jobject=serialization.read("randomForest.model"))
            inst = self.dataNewPhoto.get_instance(0)
            pred = model.classify_instance(self.dataNewPhoto.get_instance(0))

            self.label_5.setText("Class Prediction with Random Forest Algorithm")
            if str(inst.class_attribute.value(int(pred))) == "Coralillo":
                self.lblResultPhoto.setPixmap(QPixmap(files[0]).scaled(280, 260))
                self.lblShowClassResult.setText(str(inst.class_attribute.value(int(pred))))
                self.lblResultString.setText(_fromUtf8("Nombre cientifico--> Hamelia patens"
                                                       "\nHamelia -> dedica a un escritor frances de planta"
                                                       "\n Patens -> significa extendido"
                                                       "Genero --> Rubiaceae"
                                                       "\nUso--> Hay patentes de medicamentos cuyos principios activos se obtienen del Coralillo "
                                                       "\n       para estimular el sistema inmunológico."
                                                       "\n       En caso de alguna herida o de mordedura de algun animal ponzoñoso.\n"))
            elif str(inst.class_attribute.value(int(pred))) == "Guayacan":
                self.lblResultPhoto.setPixmap(QPixmap(files[1]).scaled(280, 260))
                self.lblShowClassResult.setText(str(inst.class_attribute.value(int(pred))))
                self.lblResultString.setText(_fromUtf8("Genero --> Handroanthus"
                                                       "\n         Tabebuia"
                                                       "\n         Caesalpinia"
                                                       "\n         Guaiacum"
                                                       "\n         Porlieria."
                                                       "\nOrigen-->es un árbol nativo de América tropical, con amplia distribución en las islas del  "
                                                       "\n         Caribe(especialmente Jamaica, Puerto Rico, Cuba y Republica Dominicana), la costa \n"
                                                       "           Caribe de Colombia, Panamá y Venezuela."))
            elif str(inst.class_attribute.value(int(pred))) == "Aguacate":
                self.lblResultPhoto.setPixmap(QPixmap(files[2]).scaled(280, 260))
                self.lblShowClassResult.setText(str(inst.class_attribute.value(int(pred))))
                self.lblResultString.setText(_fromUtf8("Nombre cientifico --> Persea americana\n"
                                                       "Genero -->  Lauraceae\n"
                                                       "Se cultiva en climas tropicales y mediterráneo en todo el mundo"
                                                       "El Aguacate --> Es un árbol perenne bastante grande que puede medir hasta unos 20-25 metros de\n"
                                                       "                altura. Además es muy corpulento y robusto. Posee hojas verdes oscuras muy \n"
                                                       "                brillantes y unas pequeñas flores de color amarillo."
                                                       ))
            else:
                print "Does not exist"
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("You should preprocessed the loaded Photo First ")
            msg.setWindowTitle("Error!!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    #get file from computer
    def getFileName(self):
        self.preprocesed = False
        self.filename =""
        self.lblResultPhoto.setText("Result photo")
        self.lblResultString.setText("")
        self.lblShowClassResult.setText("")
        self.label_5.setText("Classification Result")

        fname = QFileDialog.getOpenFileName(None, 'Open File', 'c:\\', "Image files(*.jpg *.png)")
        self.lbluploadPhoto.setPixmap(QPixmap(fname).scaled(256,256))
        self.filename = str (fname)


    # getting image features
    def getFeatures(self, image):
        G = greycomatrix(np.array(image, dtype=np.uint8), [1], [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4], levels=256)
        leaves = []

        leaves.append([str(greycoprops(G, prop="contrast")[0][0]),
                       str(greycoprops(G, prop="homogeneity")[0][0]),
                       str(greycoprops(G, prop="ASM")[0][0]),
                       str(greycoprops(G, prop="dissimilarity")[0][0]),
                       str(greycoprops(G, prop="energy")[0][0])])

        return leaves

    # ARFF Creation
    def generateDataset(self, files, newFile):
        try:
            atrributes = ["Contrast", "Homogeneity", "ASM", "Dissimilarity", "Energy"]

            arff = open(newFile, 'w')
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
                    for l in self.getFeatures(file):
                        for el in l:
                            arff.write(el + ",")
                        print
                        arff.write("Aguacate\n")
                    print "was there Aguacate"
                elif cont < 60:
                    for l in self.getFeatures(file):
                        for el in l:
                            arff.write(el + ",")
                        arff.write("Coralillo\n")
                    print "was there Coralillo"
                else:
                    for l in self.getFeatures(file):
                        for el in l:
                            arff.write(el + ",")
                        arff.write("Guayacan\n")
                    print "was there Guayacan"
                cont += 1
            return True
        except Exception, e:
            raise Exception(e.message)
        return False

    #generating the new photo dataset
    def generateDataSetForNewPhoto(self, image, file):
        try:
            atrributes = ["Contrast", "Homogeneity", "ASM", "Dissimilarity", "Energy"]

            arff = open(file, 'w')
            arff.write('@RELATION Leaf_Classification\n\n')
            for word in atrributes:
                arff.write('@ATTRIBUTE ')
                arff.write(str(word))
                arff.write(' numeric\n')

            arff.write('@ATTRIBUTE class {Aguacate, Guayacan, Coralillo}\n\n')
            arff.write('@DATA\n')

            image = cv2.imread(image)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            for l in self.getFeatures(image):
                for el in l:
                    arff.write(el + ",")
                print
                arff.write("?\n")
            return True
        except Exception, e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(e.message)
            msg.setWindowTitle("Error!!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    # delete recent upload photo
    def deleteFilename(self):
        self.lbluploadPhoto.setText("Upload photo here")
        self.lbluploadPhoto.setAlignment(QtCore.Qt.AlignCenter)

    # preprocessing the photo
    def preprocess(self):
        if self.filename == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("You should upload a photo before the preprocess phase")
            msg.setWindowTitle("Warning!!")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        else:
            fileName = "newLeaf.arff"
            if not self.generateDataSetForNewPhoto(self.filename, fileName):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Image does not processed")
                msg.setWindowTitle("Error!!")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()
                self.preprocesed = False
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Image processed Successfuly")
                msg.setWindowTitle("Information!!")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()
                self.preprocesed = True


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Leaf_Classification = QtGui.QWidget()
    ui = Ui_Leaf_Classification()
    ui.setupUi(Leaf_Classification)
    Leaf_Classification.show()
    sys.exit(app.exec_())

