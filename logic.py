from PyQt6.QtWidgets import *
from gui import *
from gui import Ui_Grade_Average
import csv

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def best_score(self):
        return max(self.scores)

    def attempts(self):
        return len(self.scores)

class Logic(QMainWindow):
    def __init__(self):
            QMainWindow.__init__(self)
            self.ui = Ui_Grade_Average()
            self.ui.setupUi(self)
            self.setFixedSize(self.size())
            self.students = []
            self.awaiting_scores = False
            self.current_name = ""
            self.max_attempts = 4
            self.hide_scores()
            self.clear_score_feedback()
            self.ui.label_Feedback_Submit.setText("")
            self.ui.button_Submit.clicked.connect(self.submit_clicked)


    def submit_clicked(self):
        pass

    def get_name(self):
        pass

    def get_attempts(self):
        pass

    def get_scores(self, attempts):
        pass

    def hide_scores(self):
        pass

    def show_scores(self, attempts):
        pass

    def clear_inputs(self):
        pass

    def clear_score_feedback(self):
        pass

    def set_status(self, message):
        pass

    def show_error(self, message):
        pass

    def save_to_csv(self):
        pass