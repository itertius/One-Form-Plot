import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

dot = 50
rho_values = np.linspace(0, 2, dot) # สร้างเวกเตอร์ที่มีค่าจาก 0 ถึง 2 โดยมีจำนวนจุด 50 จุด ซึ่งเป็นค่าระยะทางจากจุดศูนย์กลาง
phi_values = np.linspace(0, np.pi, dot) # สร้างเวกเตอร์ที่มีค่าจาก 0 ถึง π โดยมีจำนวนจุด 50 จุด ซึ่งเป็นมุมระหว่างเวกเตอร์และแกน z
theta_values = np.linspace(0, 2*np.pi, dot) # สร้างเวกเตอร์ที่มีค่าจาก 0 ถึง 2π โดยมีจำนวนจุด 50 จุด ซึ่งเป็นมุมรอบแกน z ในระนาบ x-y
RHO, PHI, THETA = np.meshgrid(rho_values, phi_values, theta_values) # สร้างกริด 3 มิติจากเวกเตอร์ rho_values, phi_values, theta_values ซึ่งจะได้ผลลัพธ์เป็นอาเรย์ 3D ที่ประกอบด้วยพิกัด ρ, φ, θ ที่ใช้ในการคำนวณพิกัดคาร์ทีเซียน

X = RHO * np.sin(PHI) * np.cos(THETA) # แปลงค่าจากพิกัดทรงกลม (ρ, φ, θ) เป็นพิกัดคาร์ทีเซียน (x, y, z)
Y = RHO * np.sin(PHI) * np.sin(THETA) # แปลงค่าจากพิกัดทรงกลม (ρ, φ, θ) เป็นพิกัดคาร์ทีเซียน (x, y, z)
Z = RHO * np.cos(PHI)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# dp
for i in range(dot):
    ax.plot_surface(X[:, :, i], Y[:, :, i], Z[:, :, i], color='blue', alpha=0.5)

# dφ
for i in range(dot):
    ax.plot_surface(X[:, i, :], Y[:, i, :], Z[:, i, :], color='green', alpha=0.5)

# dθ
for i in range(dot):
    ax.plot_surface(X[i, :, :], Y[i, :, :], Z[i, :, :], color='red', alpha=0.5)

ax.set_title('dp dφ dθ sphere')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()