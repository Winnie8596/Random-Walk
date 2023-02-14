import turtle as t
import random

tim=t.Turtle()

colours=['red','blue','yellow']
direction=[0,90,180,270]
tim.pensize(15)
for _ in range(200):
  tim.color(random.choice(colours))
  tim.forward(30)
  tim.setheading(random.choice(direction))
