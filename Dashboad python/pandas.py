import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('D:\Data Analytics\Data Visualization with Power BI\Financial Sample.csv')
fig = plt.figure()

plt.bar(df['x'], df['y'])
plt.title('Bar Chart')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.subplot(2, 2, 1)
plt.bar(df['x'], df['y'])
plt.title('Bar Chart 1')

plt.subplot(2, 2, 2)
plt.line(df['x'], df['y'])
plt.title('Line Chart 1')

plt.subplot(2, 2, 3)
plt.pie(df['y'])
plt.title('Pie Chart 1')

plt.show()