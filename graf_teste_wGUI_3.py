import matplotlib.pyplot as pltfrom numpy import arrayfrom numpy import arangefrom numpy import randomplt.plot([1,2,3,4]) plt.plot([5,6,7,8]) plt.plot([1,2,3,4], [1,4,9,16]) plt.figure(1)plt.subplot(221)plt.plot([1,2,3,4], [1,4,9,16], 'ro') plt.axis([0, 6, 0, 20])plt.title('Earnings', fontsize = 9)plt.xlabel('Days', fontsize = 9) plt.ylabel('Dollars', fontsize = 9) plt.subplot(222) plt.xAxis = array([1,2,3,4]) print plt.xAxistest = arange(1,5) print test print test == plt.xAxis yAxis = plt.xAxis**3 plt.plot(plt.xAxis,yAxis, 'ro')plt.subplot(223)vals = [] dieVals = [1,2,3,4,5,6] for i in range(10000):  vals.append(random.choice(dieVals)+random.choice(dieVals)) plt.hist(vals, bins=11) plt.show() # Show plots  