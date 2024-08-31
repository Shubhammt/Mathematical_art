import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

"""
modified from 
https://www.clcoding.com/2024/04/plant-leaf-using-python.html
"""

fig, ax = plt.subplots(figsize=(4, 8))
n = 2000
r = 0.2
t = np.linspace(0, 39*np.pi/2, n)

X_1 = t * np.cos(t)**3 + r*np.sin(10*t)
X_2 = t * np.cos(t)**3 + r*np.sin(10*t+np.pi/2)
Y = 9*t * np.sqrt(np.abs(np.cos(t))) + t * np.sin(0.2*t) * np.cos(4*t) 

ax.axis('off')
cmap = plt.cm.spring
colours = ['brown', 'red', 'blue']
colour_idx = [0]
def update(frame):
    ax.plot(X_1[max(0,frame-5):min(n, frame+5)], Y[max(0,frame-5):min(n, frame+5)], color='green', alpha=0.1)
    ax.plot(X_2[max(0,frame-5):min(n, frame+5)], Y[max(0,frame-5):min(n, frame+5)], color='green', alpha=0.1)
    if frame%int(n*0.5/(80*10))==0:
        ax.plot([X_1[frame],X_2[frame]], [Y[frame],Y[frame]], color='green')
    colour_idx[0]+=1
    if frame>n/100:
        ax.set(xlim=[-5-(frame-n/100)*55/n, 5+(frame-n/100)*55/n], ylim=[0, 5+(frame-n/100)*555/n])
    else:
        ax.set(xlim=[-5, 5], ylim=[0, 5])
    return ax

ani = animation.FuncAnimation(fig=fig, func=update, frames=n, interval=30, blit=False)
ani.save(filename="videos/leaf_funtion.mp4", writer="ffmpeg", fps = 60, dpi=300)