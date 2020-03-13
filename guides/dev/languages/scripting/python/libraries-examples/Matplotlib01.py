import matplotlib.pyplot as plt
plt.plot([1,2,3,4]) #Plot X, effected by python ranges start from 0.
plt.plot([1,2,3,4], [9,8,7,6]) #Plot x by y
plt.plot([1,2,3,4], [1,4,9,16], 'ro') #3rd argument deals with colour and line type of the plot.
plt.plot([1,2,3,4], [1,4,9,16], 'ro',[2,76,5,4], [3,2,6,5],"bs",[5,8,3,6], [54,6,11,6], "g^")
plt.ylabel("Numbers") # y axis name
plt.title() #Change graph title
plt.axis([0, 6, 0, 20]) #xmin, xmax, ymin, ymax.
plt.show() #Show graph


lines = plt.plot(x1, y1, x2, y2)
plt.setp(lines, color='r', linewidth=2.0) #edit properties
#or
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)


###WORKING WITH TWO FIGURES AND AXES
# Have to change focus to the other axis.
## One figure two subplots
import numpy as np #Imports numpy to generate lists
import matplotlib.pyplot as plt 

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1) # (start, stop, step) Generates values inbetween.
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1) #This is the thing holding the graph. We have to specify what is normally dealt with by default. Default figure() and subplot(111)
plt.subplot(211) #The graph itself.
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212) #Focus changed to new plot.
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

## Two figures
import matplotlib.pyplot as plt
plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)             # the second subplot in the first figure
plt.plot([4, 5, 6])


plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title

plt.clf() #Clears the figure
plt.cla #Clears the axes
plt.close() #Wipes out the figure hence freeing it's memory.

###Adding text.
plt.text(60, .025, "ThisIs","Very cool.") #Inputs text at location relative to scale of axis
plt.grid(True) #Shows grid.

#Format text by using setp() or passing keyword arguments

##Using mathmatical expressions in text
plt.title(r'$\sigma_i=15$') #Accepts any TeX expression, the "r" proceeding the text signifys that the string is raw and hence to ignore backslash python escapes.

##Annotate function
import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5), #An arrow and text, the first coordinate is for the arrow.
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.ylim(-2,2)
plt.show()


###Logarithmic and other nonlinear axis
plt.xscale("log") #Manage the scale of an axis.


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

