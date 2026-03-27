import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# open the csv
states = pandas.read_csv("./50_states.csv")

score = 0
correct_guesses = []
state_ls = states.state.to_list()
prompt_title = "Guess the State"
# TODO 4: Use a loop to allow the user to keep guessing
while score < 50:
    answer_state = screen.textinput(title=prompt_title, prompt="What's the next State name?")
    if answer_state.title() == "Exit":
        break
    for st in state_ls:
          # TODO 1: Convert guess to title case
          # TODO 2: Check if guess is among the 50 states
        if answer_state.title() == st:
          # TODO 3: Write correct guesses onto map
            writer = turtle.Turtle()
            writer.hideturtle()
            writer.penup()
            st_x = states[states.state == st]["x"].to_list()
            st_y = states[states.state == st]["y"].to_list()
            writer.goto(st_x[0],st_y[0])
            writer.pendown()
            writer.write(st)
          # TODO 5: Record the correct guesses in a list
            correct_guesses.append(st)
          # TODO 6: Keep track of the score
            score = len(correct_guesses)
            prompt_title = str(score)+"/50 States Correct"


# turtle.mainloop()

# print(f"Correct ({score}/50): {correct_guesses}")

# states_left = states

# for guess in correct_guesses:
#     states_left = states_left[states_left["state"].str.contains(guess) == False]

states_left = pandas.DataFrame([state for state in state_ls if state not in correct_guesses])

states_left.to_csv("states_to_learn.csv")