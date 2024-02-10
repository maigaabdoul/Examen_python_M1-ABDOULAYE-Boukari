#Exercice 1
# Tracer de la courbe f(x) = x⁵
from numpy import linspace
from matplotlib.pyplot import * 

x = linspace(5, 30, 20)
y = x**5
plot(x, y, "r")
show()

# Tracer du carré
import turtle as t1
t = t1.Turtle()
for i in range(4):
    t.fd(200)
    t.lt(90)
t.reset()

# Exercice 2

class Curve:
    def __init__(self, start, stop, nbr_points = 5432):
        self.start = start
        self.stop = stop
        self.nbr_points = nbr_points
    def privee(self, x):
        return x**5
    def trace(self):
        y = x**5
        plot(x, y, "r")
        show()