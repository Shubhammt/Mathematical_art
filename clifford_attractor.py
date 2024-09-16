import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
from tqdm import tqdm

fig, ax = plt.subplots(figsize=(4, 8))
n = 1000

a=-1.24458046630025
b=-1.25191834103316 
c=-1.81590817030519 
d=-1.90866735205054

a=1.7
b=1.7
c=0.6 
d=1.2

points = 10000000
X = [0]*points
Y = [0]*points
for i in tqdm(range(1, points, 1)):
    X[i] = np.sin(a*Y[i-1])+c*np.cos(a*X[i-1])
    Y[i] = np.sin(b*X[i-1])+d*np.cos(b*Y[i-1])




steps = points//n
print(steps)


ax.axis('off')
ax.set(xlim=[-2, 2], ylim=[-2.2, 2.2])
def update(frame):
    ax.scatter(X[frame*steps:(frame+1)*steps], Y[frame*steps:(frame+1)*steps], cmap='green', marker = '.', s=0.00001)
    return ax

ani = animation.FuncAnimation(fig=fig, func=update, frames=n, interval=30, blit=False)
ani.save(filename="videos/clifford_attractor.mp4", writer="ffmpeg", fps = 60, dpi=300)