from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("quizzer")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="this is a demo text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="score", background=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.true)
        self.right_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.false)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="there are no more question, end of quiz game")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)





