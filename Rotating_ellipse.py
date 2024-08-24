import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
n = 10000
theta = np.linspace(0, 400 * np.pi, n)
def func(theta):
    x, y = 1*np.cos(theta)+0.5*np.sin(0.04*theta), 4*np.sin(theta)+0.5*np.cos(0.04*theta)
    w = 0.01
    x, y = x*np.cos(w*theta) + y*np.sin(w*theta), -x*np.sin(w*theta)+y*np.cos(w*theta)
    return x, y
X, Y = func(theta)
#line, = ax.plot(X[:2], Y[:2], color='blue', alpha=1)
ax.set(xlim=[-5, 5], ylim=[-5, 5])
ax.axis('off')

def update(frame):
    #line.set_xdata(X[max(0,frame-5):min(n, frame+5)])
    #line.set_ydata(Y[max(0,frame-5):min(n, frame+5)])
    ax.plot(X[max(0,frame-5):min(n, frame+5)], Y[max(0,frame-5):min(n, frame+5)], color='blue', alpha=0.1)
    return ax

ani = animation.FuncAnimation(fig=fig, func=update, frames=n, interval=30)
ani.save(filename="test_2.mp4", writer="ffmpeg", fps = int(60*n/500))
#plt.show()