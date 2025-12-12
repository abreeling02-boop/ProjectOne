from PyQt6.QtWidgets import *
from gui import Ui_Grade_Average
import csv

class Logic(QMainWindow, Ui_Grade_Average):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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

        scores = []
        try:
            s1_text = self.line_Score_One.text().strip()
            if s1_text == "":
                raise ValueError
            s1 = int(s1_text)
            scores.append(s1)

            if attempts >= 2:
                s2_text = self.line_Score_Two.text().strip()
                if s2_text == "":
                    raise ValueError
                s2 = int(s2_text)
                scores.append(s2)

            if attempts >= 3:
                s3_text = self.line_Score_Three.text().strip()
                if s3_text == "":
                    raise ValueError
                s3 = int(s3_text)
                scores.append(s3)

            if attempts >= 4:
                s4_text = self.line_Score_Four.text().strip()
                if s4_text == "":
                    raise ValueError
                s4 = int(s4_text)
                scores.append(s4)
        except:
            self.label_Feedback_Submit.setVisible(True)
            self.label_Feedback_Submit.setText("Enter numeric values")
            if attempts >= 1:
                self.label_Feedback_Score_One.setVisible(True)
                self.label_Feedback_Score_One.setText("Required")
            if attempts >= 2:
                self.label_Feedback_Score_Two.setVisible(True)
                self.label_Feedback_Score_Two.setText("Required")
            if attempts >= 3:
                self.label_Feedback_Score_Three.setVisible(True)
                self.label_Feedback_Score_Three.setText("Required")
            if attempts >= 4:
                self.label_Feedback_Score_Four.setVisible(True)
                self.label_Feedback_Score_Four.setText("Required")
            return

        for i in range(len(scores)):
            if scores[i] < 0 or scores[i] > 100:
                self.label_Feedback_Submit.setVisible(True)
                self.label_Feedback_Submit.setText("Scores must be 0-100")
                if attempts >= 1:
                    self.label_Feedback_Score_One.setVisible(True)
                    self.label_Feedback_Score_One.setText("0-100")
                if attempts >= 2:
                    self.label_Feedback_Score_Two.setVisible(True)
                    self.label_Feedback_Score_Two.setText("0-100")
                if attempts >= 3:
                    self.label_Feedback_Score_Three.setVisible(True)
                    self.label_Feedback_Score_Three.setText("0-100")
                if attempts >= 4:
                    self.label_Feedback_Score_Four.setVisible(True)
                    self.label_Feedback_Score_Four.setText("0-100")
                return

        total = 0
        for score in scores:
            total += score
        average = total / attempts

        self.label_Feedback_Submit.setVisible(True)
        self.label_Feedback_Submit.setText(f"{name} avg: {average:.2f}")

        try:
            self.setup_csv_file()
            score1 = self.line_Score_One.text().strip()
            score2 = ""
            score3 = ""
            score4 = ""

            if attempts >= 2:
                score2 = self.line_Score_Two.text().strip()
            if attempts >= 3:
                score3 = self.line_Score_Three.text().strip()
            if attempts >= 4:
                score4 = self.line_Score_Four.text().strip()

            row = [name, attempts_text, score1, score2, score3, score4, f"{average:.2f}"]

            file = open(self.csv_file, "a", newline="")
            writer = csv.writer(file)
            writer.writerow(row)
            file.close()
        except:
            return
