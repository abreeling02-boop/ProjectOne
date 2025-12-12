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

            def identify_scores(self):
                self.hide_feedback()
                self.hide_scores()
                self.button_Submit.setEnabled(False)