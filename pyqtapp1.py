##scope of this project is split the email using PYQT6
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QLineEdit,QLabel
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyAPP")
        # self.setGeometry(100,100,200,200)

        l1=QLabel("Email Splitter App")
        self.search_box = QLineEdit(self,
            placeholderText='Enter a email id for split...',
            clearButtonEnabled=True
        )
        l2=QLabel("Result is :")
        self.username=QLineEdit()
          # Initially disabled
        self.username.setDisabled(True)

        self.domain=QLineEdit()
        self.domain.setDisabled(True)


        button=QPushButton("Click Me")
        button.clicked.connect(self.on_click)


        #we need to place the label on window
        layout=QVBoxLayout()
        layout.addWidget(l1)
        layout.addWidget(self.search_box)
        layout.addWidget(button)
        layout.addWidget(l2)
        layout.addWidget(self.username)
        layout.addWidget(self.domain)
        self.setLayout(layout)
        self.show()


    def on_click(self):
        user_input = self.search_box.text()
        check_1=user_input.count("@")

        if check_1 !=1 :
            self.username.setText("Invalid email")
            self.domain.setText("Invalid email")
        else:
            email = user_input.split("@")
            self.username.setText(email[0])  # Set username
            self.domain.setText(email[1])  # Set domain

        self.username.setDisabled(False)
        self.domain.setDisabled(False)

app=QApplication(sys.argv)
window=MainWindow()
app.exec()

