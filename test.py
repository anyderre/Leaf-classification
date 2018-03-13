import cv2
import numpy as np
from PIL import Image
from scipy import misc
from skimage import feature, data
from skimage.feature import greycomatrix, greycoprops
import os
import errno

import glob


def build_filters():
    filters = []
    tethaArray =[22,44,66,88,110,132,154,176]
    sigmaArray =[2,4,8,16]
    ksize = 31
    for theta in tethaArray:
        for sigma in sigmaArray:
            kern = cv2.getGaborKernel((ksize, ksize), sigma, theta, 1.0, 0.5, 0, ktype=cv2.CV_32F)
            kern /= 1.5 * kern.sum()
            filters.append(kern)
    return filters


def process(image, filters):
    images=[]
    cont =0
    gray =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    accum = np.zeros_like(gray)

    for kern in filters:
        fimg = cv2.filter2D(gray, cv2.CV_8UC3, kern)
        images.append(fimg)
        #cv2.imwrite("img" + str(cont) + ".png", fimg)
        cont+=1
    #np.maximum(accum, fimg, accum)

    #return accum
    return images

def getFeatures (images):
    graco = []
    for image in images:
        graco.append(
            greycomatrix(np.array(image, dtype=np.uint8), [1], [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4], levels=256))

    leaves =[]
    for G in graco:
        leaves.append([str(greycoprops(G, prop="contrast")[0][0]),
                       str(greycoprops(G, prop="homogeneity")[0][0]),
                       str(greycoprops(G, prop="ASM")[0][0]),
                       str(greycoprops(G, prop="dissimilarity")[0][0]),
                       str(greycoprops(G, prop="energy")[0][0])
                       ])
    return leaves


# ARFF Creation
def generateDataset(files):
    try:
        atrributes = ["Contrast", "Homogeneity", "ASM", "Dissimilarity", "Energy"]

        arff = open('Leaves.arff', 'w')
        arff.write('@RELATION Leaf_Classification\n\n')
        for word in atrributes:
            arff.write('@ATTRIBUTE ')
            arff.write(str(word))
            arff.write(' numeric\n')

        arff.write('@ATTRIBUTE class {Aguacate,Guayacan,Coralillo}\n\n')
        arff.write('@DATA\n')
        # Counting word frequencies for each verse
        cont = 0
        for file in files:
            file = cv2.imread(file)
            if cont < 30:
                for leaf in getFeatures(process(file, build_filters())):
                    for l in leaf:
                        arff.write(l+",")
                    arff.write("Aguacate\n")
                print "was there Aguacate"
            elif cont < 60:
                for leaf in getFeatures(process(file, build_filters())):
                    for l in leaf:
                        arff.write(l + ",")
                    arff.write("Coralillo\n")
                print "was there Coralillo"
            else:
                for leaf in getFeatures(process(file, build_filters())):
                    for l in leaf:
                        arff.write(l + ",")
                    arff.write("Guayacan\n")
                print "was there Guayacan"
            cont += 1
        return True
    except Exception, e:
        raise Exception(e.message)
    return False




img = cv2.imread("C:\Users\Dany\Desktop\leaf.jpg")

process(img, build_filters())

files = glob.glob("C:\Users\Dany\PycharmProjects\Proyeto\hojas\*.jpg")


generateDataset(files)

print len(files)

























#print homogeneity
#print "---"+ str (len(homogeneity))
#print contrast
#print "---"+ str (len(contrast))
#print asm
#print "---"+ str (len(asm))
#print dissimilarity
#print "---"+ str(len(dissimilarity))
#print energy
#print "---"+ str (len(energy))
#print correlation
#print"--"+ str (len(correlation))




#print greycoprops(res,"contrast")
#cv2.imshow("result", res)