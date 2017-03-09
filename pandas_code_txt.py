# Рисовать графики сразу же
#%matplotlib inline
#ipython notebook --matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (5, 5)  # Размер картинок

fixed_df = pd.read_csv('bikes.txt', 
                       sep=';', encoding='latin1',
                       parse_dates=['Date'], dayfirst=True,
                       index_col='Date')
fixed_df[:3]
fixed_df['Berri 1'].plot()

fixed_df.plot(kind='line') # Figure 2
plt.show() # Figure 1
