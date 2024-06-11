import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.dates import DateFormatter

# Cargar el archivo CSV
url = "./datos/datalogger.csv"
df = pd.read_csv(url)

df.columns = ['Time', 'Voltage', 'ADC']

df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')

fig, ax = plt.subplots(figsize=(13, 4))
line, = ax.plot([], [], color='b')
ax.set_xlabel("Tiempo", size=10)
ax.set_ylabel("Voltage", size=10)
ax.set_xlim(df['Time'].min(), df['Time'].max())
ax.set_ylim(min(df["Voltage"]), max(df["Voltage"]))

# Configurar el formato de fecha en el eje x
ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))

def init():
    line.set_data([], [])
    return line,
def update(frame):
    x = df["Time"][:frame]
    y = df["Voltage"][:frame]
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(df), init_func=init, blit=True, interval=200, repeat=False)

plt.show()