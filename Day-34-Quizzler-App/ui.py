import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # telling what datatype it will be (must be imported)
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # creating Score Label
        self.label = tk.Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR, font=FONT)
        self.label.grid(row=0, column=1,)

        # creating canvas
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        # creating buttons
        true_img = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_img, highlightthickness=0, borderwidth=0, command=self.true_answ)
        self.true_button.config(padx=20)
        self.true_button.grid(row=2, column=0)

        false_img = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_img, highlightthickness=0, borderwidth=0, command=self.false_answ)
        self.false_button.config(padx=20)
        self.false_button.grid(row=2, column=1)

        self.get_nex_question()

        self.window.mainloop()

    def get_nex_question(self):
        """method which will fetch text from question passed from next_question function and show it on canvas screen"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="This is end of the QUIZ")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true_answ(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_answ(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_nex_question)

    def get_summary(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(
            self.question_text,
            text=f"End of the Quiz\n\nYou final score is {self.quiz.score}/10."
        )
