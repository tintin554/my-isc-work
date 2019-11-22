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

#Drawing 3 graphs side by side on a single page

#Using "subplot function to select plots" below is wrong, look at booklet

p1 = plt.subplot(1, 3, 1)

p1.plot(range(0,10,1))

p2 = plt.subplot(1, 3, 2)

p2.plot(range(10,0,-1) 

p3 = plt.subplot(1, 3, 3)

p3.plt([4]*10)

plt.show()


