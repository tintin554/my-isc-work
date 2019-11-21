#Matplotlib introduction exercise

import matplotlib.pyplot as plt

x = range(10)

plt.plot(x) 
plt.show()

#plot some chemistry data

x = [(range(7))]
y = [250, 265, 272, 260, 300, 320, 389]

plt.title("CO2 concentration vs time")
plt.xlabel("time / decade")
plt.ylabel("CO2 concentration / ppm")
plt.plot(x,y,'b--')
plt.show()

#Now add temperature to plot (extra line)

z = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]

plt.title("CO2 concentration vs time")
plt.xlabel("Time / decade")
plt.ylabel("CO2 concentration / ppm")
plt.plot(x,y,'b--',x,z,'r')
plt.savefig("my_plot.pdf")

