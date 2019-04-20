import matplotlib.pyplot as plt
import sys
import pandas as pd


def create_graph():
  df = pd.read_csv('toggl_data.csv', sep=',')
  x = df['date']
  y = df['time']

  plt.title(sys.argv[1])
  plt.xlabel('date')
  plt.ylabel('time(m)')
  plt.plot(x, y, marker="o", color = "red", linestyle = "--")
  plt.show()