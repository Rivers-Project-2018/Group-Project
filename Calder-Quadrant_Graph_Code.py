import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams["figure.figsize"]=[10,10]
plt.rcParams['axes.edgecolor']='white'
fig, ax = plt.subplots()

#Import the Data
Calder=pd.read_csv('Calder Data.csv')
day = Calder['Day in December']
height = Calder['Height (m)']

#Scale our Data
def scale(x):
    return ((x-min(x))/(max(x)-min(x)))
scaledday = scale(day)
scaledheight = scale(height)

#finding and using ht from the hm.
ht=4.5
HM = []
for i in height:
    if i>=ht:
        HM.append(i)
hm=sum(HM)/len(HM)

#Finding qt and qm.
def Q(x):
    if x<=2.107 and x>=0.342:
        y = (8.459*((x-0.342)**2.239))
    elif x<=3.088 and x>2.107:
        y = (21.5*((x-0.826)**1.37))
    elif x<=max(height) and x>3.088:
        y = (2.086*((x+0.856)**2.515))
    return(y)
qt = Q(ht)
qm = Q(hm)   

#Rating Curve
Flow = []
for i in height:
    if i<=2.107 and i>=0.342:
        Flow.append(8.459*((i-0.342)**2.239))
    elif i<=3.088 and i>2.107:
        Flow.append(21.5*((i-0.826)**1.37))
    elif i<=max(height) and i>3.088:
        Flow.append(2.086*((i+0.856)**2.515))
        
print(max(height))
print(max(Flow))

scaledFlow = []
for i in Flow:
    scaledFlow.append((i-min(Flow))/(max(Flow)-min(Flow)))


#Plot the Rating Curve using Q NOT the Flow Rate.
negheight = -scaledheight
ax.plot(negheight,scaledFlow,'black',linewidth=2)
ax.plot([0,-1],[0,1],'forestgreen',linestyle='--', marker='', linewidth=2)

#Plot the Flow Rate and Height against the Date.
negday = -(scaledday)
ax.plot(scaledday, scaledFlow, 'black', linewidth=2)
ax.plot(negheight, negday, 'black', linewidth=2)

#Plot the lines illustrating ht,hm,qt,qm
#Scaling ht,hm,qt and qm.
scaledht = (ht-min(height))/(max(height)-min(height))
scaledhm = (hm-min(height))/(max(height)-min(height))
scaledqt = (qt-min(Flow))/(max(Flow)-min(Flow))
scaledqm = (qm-min(Flow))/(max(Flow)-min(Flow))
ax.plot([-scaledht,-scaledht],[-1,scaledqt], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledhm,-scaledhm],[-1,scaledqm], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledht,1],[scaledqt,scaledqt], 'black', linestyle='--', linewidth=1)
ax.plot([-scaledhm,1],[scaledqm,scaledqm], 'black', linestyle='--', linewidth=1)

#Fiddly plot to plot the box around the F.E.V. and the Tf line.
ax.plot([67/200,67/200,67/200],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([67/160,67/160,67/160],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([67/200,67/160],[-1/5,-1/5], 'black', linewidth=1)
ax.plot([67/200,67/200],[scaledqm,scaledqt], 'black',linewidth=1.5)
ax.plot([67/200,67/160],[scaledqm,scaledqm], 'black',linewidth=1.5)
ax.plot([67/200,67/160],[scaledqt,scaledqt], 'black',linewidth=1.5)
ax.plot([67/160,67/160],[scaledqm,scaledqt], 'black',linewidth=1.5)

#Formatting the ticks and the Axis.
ticks_x = [-4731/4466,-533/638,-2731/4466,-1731/4466,-731/4466,1/4,2/4,3/4,1]
#This describes the position I want each tick to be on a graph with x axis from -1 to 1.
#done by doing (2-min(height))/(max(height)-min(height)) to find where 2 should be 
#positioned on the axis.
ticks_y = [-1,-3/4,-2/4,-1/4,2413/11593,4643/11593,7143/11593,9643/11593,1.047442422]
ax.set_xticks(ticks_x)
ax.set_yticks(ticks_y)
Ticks_x = [6,5,4,3,2,26,27,28,29]
Ticks_y = [29,28,27,26,50,100,150,200,250]
ax.set_xticklabels(Ticks_x)
ax.set_yticklabels(Ticks_y)
ax.spines['left'].set_position(('center'))
ax.spines['bottom'].set_position(('center'))
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.tick_params(axis='x', colors='black', direction='out', length=10, width=1)
ax.tick_params(axis='y', colors='black', direction='out', length=10, width=1)

#Graph Labels.
plt.text(-0.7, -1,'$h_T$', size=13)
plt.text(-13/15, -1,'$h_m$', size=13)
plt.text(1, scaledqm,'$Q_m$', size=13)
plt.text(1, scaledqt,'$Q_T$', size=13)
plt.text(0.355,-0.19,'$T_f$',size=13)
plt.text(0.331,-0.21,'<')
plt.text(0.4,-0.21,'>')

#Axis Labels.
plt.text(0.01, 1.05,'$Q$ [m$^3$/s]', size=13)
plt.text(0.95, -0.15,'$t$ [day]', size=13)
plt.text(0.01, -1.08,'$t$ [day]', size=13)
plt.text(-1.1, 0.02,'$\overline {h}$ [m]', size=13)

#Text on Graph.
plt.text(0.4,-0.4,'$FEV$ $≈$ 1.65Mm$^3$', size=15)
plt.text(0.4,-0.475,'$T_f$ = 8.25hrs', size=15)
plt.text(0.4,-0.55,'$h_T$ = 4.50m', size=15)
plt.text(0.4,-0.625,'$h_m$ = 5.25m', size=15)
plt.text(0.4,-0.7,'$Q_T$ = 142.00m$^3$/s', size=15)
plt.text(0.4,-0.775,'$Q_m$ = 197.50m$^3$/s', size=15)

#Fill in the F.E.V.
QT=[]
for i in scaledFlow:
    i = scaledqt
    QT.append(i)
#Because I have to make qt into a list otherwise I get an error because I'm comparing
#a list with a float.
a=np.array(scaledFlow)
b=np.array(QT)
#Puts lists into an array as opposed to a list. Means that Python finds it easier to
#compare the 2.
ax.fill_between(scaledday,a,b,where=a>=b,facecolor='forestgreen')

#Find the Tf
idx = np.argwhere(np.diff(np.sign(b - a))).flatten()
print(scaledday[idx])
def unscaleday(x):
    return (((max(day)-min(day))*x)+min(day))
c=unscaleday(0.333)
d=unscaleday(0.419)
Tf=(d-c)*24
#find Tf in seconds
Tfs=Tf*(60**2)

#Find F.E.V
FEV=(qm-qt)*Tfs