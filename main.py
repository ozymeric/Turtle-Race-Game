from turtle import Turtle, Screen
import random
colors = ["red", "orange", "black", "green", "turquoise", "purple"]

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "make your bet!", prompt = "Which turtle will win! Enter a color: : ")
turtles = []


num = -100
for i in range(6):
  ozy = Turtle(shape = 'turtle')
  ozy.color(colors[i])
  turtles.append(ozy)
  ozy.penup()
  ozy.speed("slowest")
  ozy.goto(x = -220, y = num )
  num += 40


race_not_over = True
while race_not_over:
  tur = turtles[random.randint(0,5)]
  tur.forward(random.randint(0,11))
  if tur.xcor() >= 230:
    race_not_over = False
    """
    a = list(tur.color())
    if user_bet in a:
      print("You won")
    else: 
      print(f"You lost. The winner is: {a[0]}")
    """
# The reason why we get a tuple autput with 2 same colors when we call tur.color() is; 
# when we set the color of a turtle by color() method by inputting one color name, it sets this color for both the pencolor,  and the  fillcolor
# So, the 2 colors we get are the pencolor and the fill color. 
# we can call one of them by calling tur.pencolor() or tur.fillcolor() if we want. 
    # SO:
    if user_bet == tur.pencolor():
      print("You won! Congrats...")
    else: 
      print(f"You lost. The winner is: {tur.pencolor()}.")
   
screen.exitonclick()