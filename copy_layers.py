#!/usr/bin/env python3
import sys
import os.path

from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
    QFileDialog, QApplication, QMessageBox, QDesktopWidget)

from Ui import GetCaffeFormUi
from Ui import CopyWindowUi

class GetCaffeForm(QMainWindow, GetCaffeFormUi.Ui_GetCaffeForm):
    """docstring for GetCaffeForm"""
    def __init__(self, win):
        super(GetCaffeForm, self).__init__()
        self.setupUi(self)
        self.initUI()
        self.win = win
    
    def initUI(self):
        self.OKpushButton.clicked.connect(self.click)
        self.CaffelineEdit.clicked.connect(self.pressed)
        self.center()

    def click(self):
        if self.valid_path():
            sys.path.append(self.CaffelineEdit.text() + '/python/')
            self.win.show()
            self.close()

    def pressed(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks

        sender = self.sender()
        fname = QFileDialog.getExistingDirectory(self, 'Choose path', "", options=options)
        sender.setText(fname)

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def valid_path(self):
        caffe_path = self.CaffelineEdit.text()

        if os.path.exists(caffe_path + '/python/'):
            return True
        else:
            QMessageBox.about(self, "Error!", 
                "Caffe Python implementation not found. \nPlease, correct path to Caffe.")
            return False


class Window(QMainWindow, CopyWindowUi.Ui_CopyWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.initUI()


    def initUI(self):
        self.ImageProtolineEdit.clicked.connect(self.pressed)
        self.ImageModellineEdit.clicked.connect(self.pressed)

        self.GoturnProtolineEdit.clicked.connect(self.pressed)
        self.GoturnModellineEdit.clicked.connect(self.pressed)
        
        self.goLineEdit.clicked.connect(self.pressed)

        self.copyButton.clicked.connect(self.click)

        self.center()


    def pressed(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog

        sender = self.sender()
        fname = QFileDialog.getOpenFileName(self, 'Choose file', "",
            "Caffe Files (*.caffemodel *.prototxt)", options=options)[0]
        sender.setText(fname)

    def click(self):
        if self.valid_str():
            copy_layers(self.ImageProtolineEdit.text(), self.ImageModellineEdit.text(), 
                self.GoturnProtolineEdit.text(), self.GoturnModellineEdit.text(),
                self.goLineEdit.text())
            QMessageBox.about(self, "Copy", "Copy layers successfully!!!")

    def valid_str(self):
        imagenet_model  = self.ImageModellineEdit.text()
        imagenet_proto  = self.ImageProtolineEdit.text()

        goturn_model  = self.GoturnModellineEdit.text()
        goturn_proto  = self.GoturnProtolineEdit.text()

        goturn      = self.goLineEdit.text()

        def message(msg, ext):
            if len(msg) == 1:
                QMessageBox.about(self, "Error!", "Choose {} {}!!!".format(*msg, ext))
                return False

            if len(msg) == 2:
                msg.append('and') 
                QMessageBox.about(self, "Error!", "Choose {0} {2} {1} {3}!!!".format(*msg, ext))
                return False
            return True

        msg = list()
        if '.caffemodel' not in imagenet_model:
            msg.append('ImageNet')
        if '.caffemodel' not in goturn_model:
            msg.append('GOTURN')
        flag_m = message(msg, 'caffemodel')
        msg = list()
        
        if '.prototxt' not in imagenet_proto:
            msg.append('ImageNet')
        if '.prototxt' not in goturn_proto:
            msg.append('GOTURN')
        flag_p = message(msg, 'prototxt')
        
        return flag_p and flag_m

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

def copy_layers(img_proto, img_model, goturn_proto, goturn_model, path_go):
    import caffe
    
    imagenet    = caffe.Net(img_proto, img_model, caffe.TEST)
    goturn      = caffe.Net(goturn_proto, goturn_model, caffe.TEST)

    layers = ['conv' + str(n) for n in range(1,3)]
    # layers += ['fc' + str(n) for n in xrange(6,9)]

    for layer in layers:
        w = imagenet.params[layer][0].data[...]
        b = imagenet.params[layer][1].data[...]
        goturn.params[layer + '_gray_reduce'][0].data[...]     = w
        goturn.params[layer + '_gray_reduce_p'][0].data[...]   = w 
        goturn.params[layer + '_gray_reduce'][1].data[...]     = b
        goturn.params[layer + '_gray_reduce_p'][1].data[...]   = b 

    layers = ['conv' + str(n) for n in range(5,6)]
    # layers += ['fc' + str(n) for n in xrange(6,9)]

    for layer in layers:
        w = imagenet.params[layer][0].data[...]
        b = imagenet.params[layer][1].data[...]
        goturn.params[layer + '_gray_reduce'][0].data[...]     = w
        goturn.params[layer + '_gray_reduce_p'][0].data[...]   = w 
        goturn.params[layer + '_gray_reduce'][1].data[...]     = b
        goturn.params[layer + '_gray_reduce_p'][1].data[...]   = b 

    goturn.save(path_go)

def main():
    app = QApplication(sys.argv)
    
    win = Window()

    win_caffe = GetCaffeForm(win)
    win_caffe.show()

    # win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
