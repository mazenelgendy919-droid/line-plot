import matplotlib.pyplot as plt

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperature = [22, 24, 21, 23, 25, 26, 24]


plt.plot(days, temperature, marker='o', color='b', linestyle='-')

plt.title('Temperature Variation Over a Week')
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.show()
