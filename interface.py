from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,QVBoxLayout,QHBoxLayout,QSizePolicy
)
from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()
window.resize(320, 400)
window.setWindowTitle("Калькулятор") 

app.setStyleSheet("""
                  QWidget {background-color: #e4d9fe;}
                  QPushButton {background-color: #80d6a6; border-radius:10px;font-size:25px; border-style: outset;}
                  QPushButton:pressed {background-color: #53ac83 ;border-style: inset}
                  QLabel {font-size:35px}
                  """)



result = QLabel("0")

b1 = QPushButton("1")
b2 = QPushButton("2")
b3 = QPushButton("3")
b4 = QPushButton("4")
b5 = QPushButton("5")
b6 = QPushButton("6")
b7 = QPushButton("7")
b8 = QPushButton("8")
b9 = QPushButton("9")
b0 = QPushButton("0")

b_plus = QPushButton("+")
b_minus = QPushButton("-")
b_multiplu = QPushButton("*")
b_divine = QPushButton("/")
b_point = QPushButton(".")
b_equals = QPushButton("=")
b_bacspace = QPushButton("<-")
b_clear = QPushButton("C")
b_power = QPushButton("x^y")
b_percent = QPushButton("%")

b1.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b2.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b3.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b4.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b5.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b6.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b7.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b8.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b9.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b0.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_plus.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_minus.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_multiplu.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_divine.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_equals.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_power.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_point.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_percent.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_bacspace.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
b_clear.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

layout1 = QHBoxLayout()
layout1.addWidget(b_percent)
layout1.addWidget(b0)
layout1.addWidget(b_point)
layout1.addWidget(b_equals)

layout2 = QHBoxLayout()
layout2.addWidget(b1)
layout2.addWidget(b2)
layout2.addWidget(b3)
layout2.addWidget(b_plus)

layout3 = QHBoxLayout()
layout3.addWidget(b4)
layout3.addWidget(b5)
layout3.addWidget(b6)
layout3.addWidget(b_minus)

layout4 = QHBoxLayout()
layout4.addWidget(b7)
layout4.addWidget(b8)
layout4.addWidget(b9)
layout4.addWidget(b_multiplu)

layout5 = QHBoxLayout()
layout5.addWidget(b_divine)
layout5.addWidget(b_power)
layout5.addWidget(b_clear)
layout5.addWidget(b_bacspace)

main_layout = QVBoxLayout()
main_layout.addWidget(result, alignment= Qt.AlignRight)
main_layout.addLayout(layout5)
main_layout.addLayout(layout4)
main_layout.addLayout(layout3)
main_layout.addLayout(layout2)
main_layout.addLayout(layout1)

window.setLayout(main_layout)

window.show()
