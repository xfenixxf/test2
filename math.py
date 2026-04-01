import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Мини приложение")
window.setGeometry(300, 300, 200, 150)

layout = QVBoxLayout()

label = QLabel("Нажми на кнопку")
layout.addWidget(label)

button = QPushButton("Жми!")
button.clicked.connect(lambda: label.setText("Привет!"))
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())