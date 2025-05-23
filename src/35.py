import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-5.0, -2.0, 2.0, 5.0])
y = sigmoid(x)
plt.plot(x, y)
plt.show()
