import turtle as t
import random
pig= t.Turtle()

directions = [0, 90, 180, 270]

t.colormode(255)

def random_color():
  r= random.randint(0,255)
  g= random.randint(0,255)
  b= random.randint(0,255)
  random_color=(r,g,b)
  return random_color
pig.speed("fastest")
def draw_spiral(size_of_gap):
  for i in range(int(360/size_of_gap)):
    pig.color(random_color())
    pig.circle(100)
    head=pig.heading()
    pig.setheading(head + size_of_gap)
    pig.circle(100)
draw_spiral(5)
screen = t.Screen()
screen.exitonclick()
