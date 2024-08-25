import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots(figsize=(4, 8))

"source https://matplotlib.org/stable/gallery/mplot3d/lorenz_attractor.html"
s=10
r=28
b=2.667
def lorenz(xyz):
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])


dt = 0.01
n = 5000

xyzs = np.empty((n + 1, 3))
xyzs[0] = (0.1, 0., 0)
for i in range(n):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt

X, Y = xyzs[:,0], xyzs[:,2]
ax.set(xlim=[-20, 25], ylim=[-10, 60])
ax.axis('off')
cmap = plt.cm.winter
def update(frame):
    ax.plot(X[max(0,frame-5):min(n, frame+5)], Y[max(0,frame-5):min(n, frame+5)], color=cmap(frame/n), alpha=1, lw=0.5)
    return ax

ani = animation.FuncAnimation(fig=fig, func=update, frames=n, interval=30, blit=False)
ani.save(filename="videos/Chaotic_butterfly.mp4", writer="ffmpeg", fps = 60, dpi=300)