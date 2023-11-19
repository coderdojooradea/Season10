from geometric import GeometriFigures
import time

g= GeometriFigures()
turns = 8
for n in range(turns):
    g.draw_polygon(6,100)
    g.turn_right(360/turns)


time.sleep(10)