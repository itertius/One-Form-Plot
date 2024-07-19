import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

dot = 10
r_values = np.linspace(0, 2, dot) # สร้างเวกเตอร์ที่มีค่าจาก 0 ถึง 2 โดยมีจำนวนจุด 10 จุด ซึ่งเป็นค่ารัศมีจากแกน z
theta_values = np.linspace(0, 2*np.pi, dot) # สร้างเวกเตอร์ที่มีค่าจาก 0 ถึง 2π โดยมีจำนวนจุด 10 จุด ซึ่งเป็นมุมในระนาบ x-y 
z_values = np.linspace(-2, 2, dot) # สร้างเวกเตอร์ที่มีค่าจาก -2 ถึง 2 โดยมีจำนวนจุด 10 จุด ซึ่งเป็นค่าพิกัดในแกน z
R, THETA, Z = np.meshgrid(r_values, theta_values, z_values) # สร้างกริด 3 มิติจากเวกเตอร์ r_values, theta_values, z_values ซึ่งจะได้ผลลัพธ์เป็นอาเรย์ 3D ที่ประกอบด้วยพิกัด r, θ, z ที่ใช้ในการคำนวณพิกัดคาร์ทีเซียน

X = R * np.cos(THETA) # แปลงค่าจากพิกัดทรงกระบอก (r, θ, z) เป็นพิกัดคาร์ทีเซียน (x, y, z)
Y = R * np.sin(THETA) # แปลงค่าจากพิกัดทรงกระบอก (r, θ, z) เป็นพิกัดคาร์ทีเซียน (x, y, z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# dr
for i in range(dot):
    ax.plot_surface(X[:, i, :], Y[:, i, :], Z[:, i, :], color='red', alpha=0.5)

# dtheta
for i in range(dot):
    ax.plot_surface(X[i, :, :], Y[i, :, :], Z[i, :, :], color='green', alpha=0.5)

# dz
for i in range(dot):
    ax.plot_surface(X[:, :, i], Y[:, :, i], Z[:, :, i], color='blue', alpha=0.5)

ax.set_title('dr dtheta dz cylinder')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()