import os
import xml.dom.minidom
import xml.etree.ElementTree as ET
import shutil

def changeVOCpath(xmlpath, imgpath):
    filelist = os.listdir(xmlpath)
    imgfilelist = os.listdir(imgpath)
    for i, xmlfile in enumerate(filelist):

        doc = ET.parse(xmlpath + xmlfile)
        root = doc.getroot()
        sub1 = root.find('folder')
        sub1.text = "MAFA"
        sub2 = root.find('path')
        sub2.text = imgpath + imgfilelist[i]

        doc.write(xmlpath + xmlfile)
        print("done ", i)

def extractFiles(path):
    dirlist = os.listdir(path)
    n = 0
    for directory in dirlist:
        filelist = os.path.join(path, directory)
        for files in os.listdir(filelist):
            src = os.path.join(filelist, files)
            tar = "D:\pytorch_ssd\data\VOCdevkit\WIDER\JPEGImages\\" + files
            shutil.copyfile(src, tar)
            n = n+ 1
            print(n)

def removeNotMatch(imgpath, xmlpath):
    imglist = os.listdir(imgpath)
    xmllist = os.listdir(xmlpath)
    for img in imglist:
        imgname = os.path.splitext(img)
        isMatch = False
        for xml in xmllist:
            xmlname = os.path.splitext(xml)

            if(imgname[0] == xmlname[0]):
                isMatch = True
        if not isMatch:
            os.remove(os.path.join(imgpath, img))

if __name__ == '__main__':
    extractFiles("D:\WIDER_train\images")
    removeNotMatch("D:\pytorch_ssd\data\VOCdevkit\WIDER\JPEGImages", "D:\pytorch_ssd\data\VOCdevkit\WIDER\Annotations")
    '''extractFiles("D:\WIDER_train\images")'''
