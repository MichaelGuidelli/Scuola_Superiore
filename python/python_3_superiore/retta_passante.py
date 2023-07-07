from matplotlib import pyplot as plt
from os import system

system("cls")

x = []
y = []

for i in range(10):
    x.append(i)
    y.append(i)

plt.xlabel('X')
plt.ylabel('Y')
plt.title("Retta di equazione")
plt.plot(x,y)
plt.tight_layout()
plt.show()