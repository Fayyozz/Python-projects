import turtle
import pandas

FONT = ("Arial", 10, "normal")

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.bgpic(image)

my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.penup()
my_turtle.speed("fastest")


data = pandas.read_csv("50_states.csv")
states = data.state


correct_guesses = []

while len(correct_guesses) < 50:

    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 STATES CORRECT", prompt="What is a state's name?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missed_states = [state for state in states if state not in correct_guesses]
        df = pandas.DataFrame(missed_states)
        df.to_csv("states_to_learn.csv")
        break

    for state in states:
        if state == answer_state:
            correct_guesses.append(answer_state)
            state_with_coor = data[data["state"] == answer_state]
            x = int(state_with_coor.x)
            y = int(state_with_coor.y)
            my_turtle.setposition(x, y)
            my_turtle.write(arg=answer_state, align="center", font=FONT)


screen.mainloop()
