import numpy as np # lib
import matplotlib.pyplot as plt # lib
from mpl_toolkits.mplot3d import Axes3D # lib

dot = 10 # ความละเอียด
x = np.linspace(-2, 2, dot) # สร้างเวคเตอร์ความละเอียด dot จุด
y = np.linspace(-2, 2, dot) # สร้างเวคเตอร์ความละเอียด dot จุด
z = np.linspace(-2, 2, dot) # สร้างเวคเตอร์ความละเอียด dot จุด
X, Y, Z = np.meshgrid(x, y, z) # สร้างกริด 3 มิติจากเวกเตอร์ x, y, z ซึ่งจะได้ผลลัพธ์เป็นอาเรย์ 3D ที่ประกอบด้วยพิกัด x, y, z ที่ใช้ในการสร้างกราฟ

fig = plt.figure() # สร้าง figure
ax = fig.add_subplot(111, projection='3d') # สร้าง Axes สำหรับ 3D

# x
for i in range(dot):
    ax.plot_surface(X[:, i, :], Y[:, i, :], Z[:, i, :], color='red', alpha=0.5) # พิกัด x สร้าง 3d โดยใช้ X[:, i, :], Y[:, i, :], Z[:, i, :] และ alpha = 0.5 เพื่อให้เห็นการซ้อนทับกัน

# y
for i in range(dot):
    ax.plot_surface(X[i, :, :], Y[i, :, :], Z[i, :, :], color='green', alpha=0.5) # พิกัด y สร้าง 3d โดยใช้ X[i, :, :], Y[i, :, :], Z[i, :, :] และ alpha = 0.5 เพื่อให้เห็นการซ้อนทับกัน

# z
for i in range(dot):
    ax.plot_surface(X[:, :, i], Y[:, :, i], Z[:, :, i], color='blue', alpha=0.5) # พิกัด z สร้าง 3d โดยใช้ X[:, :, i], Y[:, :, i], Z[:, :, i] และ alpha = 0.5 เพื่อให้เห็นการซ้อนทับกัน

ax.set_title('x y z plane') # ตั้งชื่อ
ax.set_xlabel('x') # ตั้งชื่อ
ax.set_ylabel('y') # ตั้งชื่อ
ax.set_zlabel('z') # ตั้งชื่อ

plt.show() # แสดงกราฟ