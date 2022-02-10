import numpy as np
import matplotlib.pyplot as plt

x, y = [], []

with open("Densidade.xvg") as f:
    for line in f:
        cols = line.split()

        if len(cols) == 2:
            x.append(float(cols[0]))
            y.append(float(cols[1]))


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("Plot title...")    
ax1.set_xlabel('your x label..')
ax1.set_ylabel('your y label...')
ax1.plot(x,y, c='r', label='the data')
leg = ax1.legend()
plt.show() 