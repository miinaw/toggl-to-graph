import matplotlib.pyplot as plt
import sys
import pandas as pd


def create_graph():
  df = pd.read_csv('toggl_data.csv', sep=',')
  df_s = df.sort_values('date', ascending=True)
  print(df_s)
  x = df_s['date']
  y = df_s['time']

  plt.title(sys.argv[1])
  plt.xlabel('date')
  plt.ylabel('time(m)')
  plt.bar(x, y, color = "blue") # 一日の工数
  plt.plot(x, y, marker="o", color = "red", linestyle = "None") # 一日の工数の回数
  plt.show()