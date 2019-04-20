import matplotlib.pyplot as plt
import sys
import pandas as pd

df = pd.read_csv('toggl_data.csv', sep=',')
x = df['date']
y = df['time']
print(x)
print(y)

plt.xlabel('date')
plt.ylabel('time(m)')
plt.plot(x, y, marker="o", color = "red", linestyle = "--")
plt.show()