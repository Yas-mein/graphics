from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation , writers
import numpy as np

fig = plt.figure(figsize=(7,5))
axes = fig.add_subplot(1,1,1)
axes.set_ylim(0,300)
collist = ['blue','red','green']

y1,y2,y3 ,y4,y5,y6= [],[],[],[],[],[]

def animation_func(i):

    y1= i
    y2=i*2
    y3=i*3
    y4=i*4
    y5=i*9
    y6=i*10

    plt.xlabel('x')
    plt.ylabel('y')

    plt.bar(['initial','squer','truble','toot','beeb','raaa'] ,
            [y1,y2,y3,y4,y5,y6] , color=collist)


animation= FuncAnimation(fig , animation_func , interval= 50)

plt.show()