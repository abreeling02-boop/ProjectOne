from PyQt6.QtWidgets import *
from gui import Ui_Grade_Average
import csv

class Logic(QMainWindow, Ui_Grade_Average):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.csv_file = "grades.csv"
        self.hide_scores()
        self.hide_feedback()
        self.button_Submit.setEnabled(False)
        self.line_Student_Name.textChanged.connect(self.identify_scores)
        self.line_Number_Attempts.textChanged.connect(self.identify_scores)
        self.button_Submit.clicked.connect(self.submit_button)

    def hide_feedback(self):
        self.label_Feedback_Submit.setVisible(False)
        self.label_Feedback_Score_One.setVisible(False)
        self.label_Feedback_Score_Two.setVisible(False)
        self.label_Feedback_Score_Three.setVisible(False)
        self.label_Feedback_Score_Four.setVisible(False)

        self.label_Feedback_Submit.setText("")
        self.label_Feedback_Score_One.setText("")
        self.label_Feedback_Score_Two.setText("")
        self.label_Feedback_Score_Three.setText("")
        self.label_Feedback_Score_Four.setText("")

    def hide_scores(self):
        self.label_Score_One.setVisible(False)
        self.label_Score_Two.setVisible(False)
        self.label_Score_Three.setVisible(False)
        self.label_Score_Four.setVisible(False)

        self.line_Score_One.setVisible(False)
        self.line_Score_Two.setVisible(False)
        self.line_Score_Three.setVisible(False)
        self.line_Score_Four.setVisible(False)

        self.line_Score_One.setText("")
        self.line_Score_Two.setText("")
        self.line_Score_Three.setText("")
        self.line_Score_Four.setText("")

    def setup_csv_file(self):
        try:
            with open(self.csv_file, "r", newline="") as file:
                first = file.readline()
                if first != "":
                    return
        except:
            pass

        with open(self.csv_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "attempts", "score1", "score2", "score3", "score4", "average"])

    def identify_scores(self):
        self.hide_feedback()
        self.hide_scores()
        self.button_Submit.setEnabled(False)

        name = self.line_Student_Name.text().strip()
        attempts_text = self.line_Number_Attempts.text().strip()

        if name == "" or attempts_text == "":
            return

        try:
            attempts = int(attempts_text)
        except:
            self.label_Feedback_Submit.setVisible(True)
            self.label_Feedback_Submit.setText("Enter numeric values")
            return

        if attempts < 1 or attempts > 4:
            self.label_Feedback_Submit.setVisible(True)
            self.label_Feedback_Submit.setText("Attempts must be 1-4")
            return

        self.button_Submit.setEnabled(True)

        self.label_Score_One.setVisible(True)
        self.line_Score_One.setVisible(True)

        if attempts >= 2:
            self.label_Score_Two.setVisible(True)
            self.line_Score_Two.setVisible(True)
        if attempts >= 3:
            self.label_Score_Three.setVisible(True)
            self.line_Score_Three.setVisible(True)
        if attempts >= 4:
            self.label_Score_Four.setVisible(True)
            self.line_Score_Four.setVisible(True)

    def submit_button(self):
        self.hide_feedback()

        name = self.line_Student_Name.text().strip()
        attempts_text = self.line_Number_Attempts.text().strip()

        if name == "" or attempts_text == "":
            self.label_Feedback_Submit.setVisible(True)
            self.label_Feedback_Submit.setText("Enter name and attempts")
            return

        try:
            attempts = int(attempts_text)
        except:
            self.label_Feedback_Submit.setVisible(True)
            self.label_Feedback_Submit.setText("Enter numeric values")
            return

        if attempts < 1 or attempts > 4:
            self.label_Feedback_Submit.setVisible(True)
            self.label_Feedback_Submit.setText("Attempts must be 1-4")
            return
        score_lines = [self.line_Score_One, self.line_Score_Two,self.line_Score_Three, self.line_Score_Four]
        feedback_labels = [self.label_Feedback_Score_One, self.label_Feedback_Score_Two, self.label_Feedback_Score_Three, self.label_Feedback_Score_Four]
        scores = []
        has_error = False

        for i in range(attempts):
            text = score_lines[i].text().strip()

            if text == "":
                feedback_labels[i].setVisible(True)
                feedback_labels[i].setText("Required")
                has_error = True
                scores.append(None)
                continue

            try:
                value = int(text)
            except:
                feedback_labels[i].setVisible(True)
                feedback_labels[i].setText("Enter integer")
                has_error = True
                scores.append(None)
                continue

            if value < 0 or value > 100:
                feedback_labels[i].setVisible(True)
                feedback_labels[i].setText("0-100")
                has_error = True
                scores.append(None)
                continue

            scores.append(value)

        if has_error:
            self.label_Feedback_Submit.setVisible(True)
            self.label_Feedback_Submit.setText("Fix highlighted score(s)")
            return

        average = sum(scores) / attempts

        self.label_Feedback_Submit.setVisible(True)
        self.label_Feedback_Submit.setText("Submitted")

        try:
            self.setup_csv_file()

            score_texts = []
            for i in range(4):
                if i < attempts:
                    score_texts.append(score_lines[i].text().strip())
                else:
                    score_texts.append("")

            score1, score2, score3, score4 = score_texts
            row = [name, attempts_text, score1, score2, score3, score4, f"{average:.2f}"]

            with open(self.csv_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(row)
        except:
            pass