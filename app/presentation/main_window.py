import sys


from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTextEdit, QWidget


class MainWindow(QMainWindow):
    def __init__(self, func):
        super().__init__()
        self.func = func

        self.setWindowTitle("Output")
        self.setGeometry(100, 100, 400, 300)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        self.show_result_button = QPushButton("Show Result")
        self.clear_button = QPushButton("Clear")

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.show_result_button)
        layout.addWidget(self.clear_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show_result_button.clicked.connect(self.show_result)
        self.clear_button.clicked.connect(self.clear_text)

    def show_result(self):
        output_text = self.func()
        self.text_edit.setPlainText(output_text)

    def clear_text(self):
        self.text_edit.clear()


def run_application(func):
    app = QApplication(sys.argv)
    main_window = MainWindow(func)
    main_window.show()
    sys.exit(app.exec())
