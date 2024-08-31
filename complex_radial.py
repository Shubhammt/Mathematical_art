import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots(figsize=(4, 8))
n = 3000
theta = np.linspace(0, 10 * np.pi, n)

def func(theta):
    r = (np.sin(1.2*theta))+(np.cos(6*theta))**2
    return r*np.cos(theta), r*np.sin(theta)



X, Y = func(theta)
ax.set(xlim=[-3, 3], ylim=[-2, 2])
ax.axis('off')
cmap = plt.cm.spring
def update(frame):
    ax.plot(X[max(0,frame-5):min(n, frame+5)], Y[max(0,frame-5):min(n, frame+5)], color=cmap(frame/n), alpha=0.1)
    return ax

ani = animation.FuncAnimation(fig=fig, func=update, frames=n, interval=30, blit=False)
ani.save(filename="videos/complex_radial.mp4", writer="ffmpeg", fps = 60, dpi=300)