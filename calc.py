from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import sys

class CustomCalc(QMainWindow):
    def __init__(self):
        super(CustomCalc, self).__init__()
        
        loadUi('calc.ui',self)

        self.add.clicked.connect(self.add_num)
        self.sub.clicked.connect(self.sub_num)
        self.mult.clicked.connect(self.mult_num)
        self.div.clicked.connect(self.div_num)

    def add_num(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())   
            self.result.setText(f"Ответ: {num1 + num2}")
        except:
            self.result.setText("Numbers")

    def sub_num(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.result.setText(f"Ответ: {num1 - num2}")
        except:
             self.result.setText("Numbers")

    def mult_num(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.result.setText(f"Ответ: {num1 * num2}")
        except:
             self.result.setText("Numbers")

    def div_num(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.result.setText(f"Ответ: {num1 / num2}")
        except:
             self.result.setText("Numbers")
        # if num2 == 0:
            
            


app = QApplication(sys.argv)
calc = CustomCalc()
calc.show()
app.exec_()