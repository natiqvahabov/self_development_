# jupyter notebook for running jupyter
%matplotlib notebook

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
plt.plot(np.random.randn(50).cumsum(), 'k--')

# 2x2 hist diagrams
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(300), bins=30, color="k", alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)

# setting labels and change ranges
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
   ....:                             rotation=30, fontsize='small')
ax.set_title('My first matplotlib plot')
Text(0.5,1,'My first matplotlib plot')
ax.set_xlabel('Stages')

# alternatively
props = {
    'title': 'My first matplotlib plot',
    'xlabel': 'Stages'
}
ax.set(**props)

# legends
'k', label='one'
'k--', label='two'
'k.', label='three'
ax.legend(loc='best')


# Panda and Seaborn
import pandas as pd
s = pd.Series(np.random.randn(10), index=np.arange(0, 100, 10))
s.plot()

# With data that requires aggregation or summarization before making a plot, using the seaborn package can make things much simpler
import seaborn as sns
tips = pd.read_csv('examples/tips.csv')
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])
sns.barplot(x='tip_pct', y='day', data=tips, orient='h')

