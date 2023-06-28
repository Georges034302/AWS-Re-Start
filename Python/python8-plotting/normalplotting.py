from numpy import random 
import seaborn as sns 
import matplotlib.pyplot as plt

sns.displot(random.normal(size=1000))
plt.show()