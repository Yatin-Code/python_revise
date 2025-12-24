import pandas as pd 
import turtle



screen = turtle.Screen()
screen.title("US State GAME")

img = "state_project/blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
df = pd.read_csv("state_project/50_states.csv")
states = df["state"]

while True:
    answer_something = screen.textinput(title="Guess the State" , prompt="What's the state name??")
    if answer_something in states.to_list():
        turtle.penup()
        x = int(df[df.state == answer_something]["x"])
        y = int(df[df.state == answer_something]["y"])
        turtle.goto(x , y)
        turtle.write(answer_something, align="center", font=("Arial", 14, "normal"))