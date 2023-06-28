from numpy import random
import matplotlib.pyplot as plt

n = int(input("Number of CPU: "))

usage = {} # represent cpu usage as: cpu-usage
cpu = "CPU"

for e in range(1,n+1):
    currentCPU = cpu+str(e) # keys to be used as labels
    usage[currentCPU] = random.randint(1,100) # simulating a usage
    
X = range(len(usage))
Y = list(usage.values())
labels = list(usage.keys())

plt.bar(X,Y,tick_label=labels,width=0.4,color='green')
plt.show()