"""
Practicing with matplotlib.
Temperatures during the day in Lviv and Odessa in March.
"""

import matplotlib.pyplot as plt 

#Hours
x = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00','11:00',
 '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']

#Lviv
y1 = [11, 10, 10, 10, 9, 10, 10, 10, 10, 11, 11, 12, 13, 13, 14, 15, 14, 14, 13, 12, 11, 11, 10, 10]

#Odessa
y2 = [5, 5, 5, 5, 5, 6, 5, 5, 6, 7, 8, 10, 11, 11, 11, 11, 11, 10, 10, 9, 8, 8, 7, 6]

plt.figure(figsize=(18,5))

plt.plot(x, y1, 'o-', c= '#FFDC00', label='Lviv', lw=3, ms=10)
plt.fill_between(x, y1, color='#F8FF00', alpha=0.5)

plt.plot(x, y2, '^-', c='#FF7000', label='Odessa', lw=3, ms=10)
plt.fill_between(x, y2, color='#FF5100', alpha=0.3)

plt.title('Temperatures during the day in Lviv and Odessa in March', fontsize=18)

plt.xlabel('Hour', fontsize=12)
plt.ylabel('Temperature, °C', fontsize=12)

plt.grid()

plt.tick_params(axis='both', labelsize=9, grid_color='#ECA36E')
plt.legend(loc='upper left')

plt.savefig('Temperatures.png', bbox_inches='tight')
plt.show()