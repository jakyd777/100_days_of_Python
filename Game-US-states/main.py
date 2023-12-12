import turtle as t
import pandas as pd


def print_state(name, x, y):
    state = t.Turtle()
    state.hideturtle()
    state.penup()
    state.goto(x, y)
    state.write(name, font=('Arial', 8, 'normal'))


def to_learn():
    """Function which will made csv file with states name you don't remember."""
    # to_learn_list = []
    # for state in list_of_states:
    #     if state not in list_correct_answers:
    #         to_learn_list.append(state)

    # using conditional list comprehension
    to_learn_list = [state for state in list_of_states if state not in list_correct_answers]

    # to_learn_dic = {
    #     "States to learn": to_learn_list
    # }
    data = pd.DataFrame(to_learn_list) # to Dataframe we can change simple list, or whole dictionary
    data.to_csv("to_learn.csv")


all_states = pd.read_csv("50_states.csv")

screen = t.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
t.addshape(image)
t.shape(image)

# def get_mouse_click_coor(x, y):  # will print coordinates when clicked on map
#     print(x, y)
#
# screen.onscreenclick(get_mouse_click_coor)

game_is_on = True
num_correct_answers = 0
list_correct_answers = []
list_of_states = all_states['state'].to_list()
list_of_xcor = all_states['x'].to_list()
list_of_ycor = all_states['y'].to_list()

while game_is_on:
    answer_state = screen.textinput(title=f"{num_correct_answers}/50 states correct.", prompt="What's the next state name?").title()
    if answer_state == "Exit": # using if statement can delete mainloop
        to_learn()
        break
    for one_state in list_of_states:
        if answer_state == one_state:
            if answer_state.lower() not in list_correct_answers:
                state_xcor = list_of_xcor[list_of_states.index(one_state)]
                state_ycor = list_of_ycor[list_of_states.index(one_state)]
                # state_xcor = int(all_states[all_states["state"] == one_state].x)
                # state_ycor = int(all_states[all_states["state"] == one_state].y)
                print_state(one_state, state_xcor, state_ycor)
                num_correct_answers += 1
                list_correct_answers.append(one_state)
    game_is_on = len(list_correct_answers) < 50  # finish game when all states guessed correctly

# t.mainloop()   # keep screen on after finishing code
