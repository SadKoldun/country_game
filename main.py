import turtle
import pandas

screen = turtle.Screen()
screen.title = 'New Game'
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
list_states = []
missing_states = []
all_states = data.state.to_list()


while len(list_states) < 50:
    answer_user = screen.textinput(title=f'state? u guess {len(list_states)}/50', prompt='write pls?').title()
    if answer_user.capitalize() == 'Exit':
        for state in all_states:
            if state not in list_states:
                missing_states.append(state)
        exit_csv = pandas.DataFrame(missing_states)
        exit_csv.to_csv('Missing_states.csv')
        break

    if answer_user in all_states and answer_user not in list_states:
        list_states.append(answer_user)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        new_coord = data[data.state == answer_user]
        t.goto(int(new_coord.x), int(new_coord.y))
        t.write(answer_user)



