from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
import sys
import os

if __name__ == '__main__':
    # Some code to obtain the form file name, ui_file_name
    ui_file_name = os.path.basename('\\designerGraphics.ui')
    app = QApplication(sys.argv)
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
        sys.exit(-1)
    loader = QUiLoader()
    widget = loader.load(ui_file, None)
    widget = widget.setWindowIcon("Validator_logo.png")
    ui_file.close()
    if not widget:
        print(loader.errorString())
        sys.exit(-1)
    widget.show()
    sys.exit(app.exec_())