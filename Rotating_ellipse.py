import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots(figsize=(4, 8))
n = 5000
theta = np.linspace(0, 200 * np.pi, n)

centre_radius = 0.5
centre_angular_velocity = 0.04
minor_axis = 1
major_axis = 4
ellipse_angular_velocity = 0.01

def func(theta):
    ellipse_center              = [centre_radius*np.sin(centre_angular_velocity*theta), centre_radius*np.cos(centre_angular_velocity*theta)]
    x_ellipse, y_ellipse        = minor_axis*np.cos(theta), major_axis*np.sin(theta)
    x_wrt_centre, y_wrt_centre  = x_ellipse + ellipse_center[0], y_ellipse + ellipse_center[1]
    x_rot                       = x_wrt_centre*np.cos(ellipse_angular_velocity*theta) + y_wrt_centre*np.sin(ellipse_angular_velocity*theta)
    y_rot                       = -x_wrt_centre*np.sin(ellipse_angular_velocity*theta) + y_wrt_centre*np.cos(ellipse_angular_velocity*theta)
    return x_rot, y_rot


X, Y = func(theta)
ax.set(xlim=[-5, 5], ylim=[-10, 10])
ax.axis('off')

def update(frame):
    ax.plot(X[max(0,frame-5):min(n, frame+5)], Y[max(0,frame-5):min(n, frame+5)], color='blue', alpha=0.1)
    return ax

ani = animation.FuncAnimation(fig=fig, func=update, frames=n, interval=30, blit=False)
ani.save(filename="Rotating_ellipse.mp4", writer="ffmpeg", fps = 60, dpi=300)