import numpy as np
import matplotlib.pyplot as plt

x = np.load('C:/Users/Tango/Documents/GitHub/Jamming/test_data/train_x0.npy') # reality
a = np.load('C:/Users/Tango/Documents/GitHub/Jamming/test_data/train_y0.npy') # ideality
print(x)
# n = x.size
n = 2000
x = x[:n]
a = a[:n]
y = np.arange(0, n)
b = np.arange(0, n)
fig = plt.figure()
ax = fig.add_subplot(211)
ax.scatter(y, x, s=1, marker='.')
bx = fig.add_subplot(212)
bx.scatter(b, a, s=1, marker='.')
plt.show()