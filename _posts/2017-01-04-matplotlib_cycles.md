---
tags: python, open science, visualizations
interactive: False
title: Matplotlib Cyclers are Great
permalink: matplotlib-cycles
category: visualization
date: 2017-01-04
---
Every now and then I come across a nifty feature in Matplotlib that I wish I'd known about earlier. The MPL documentation can be a beast to get through, and as a result you miss some cool stuff sometimes.

This is a quick demo of one such feature: the **cycler**.

Have you ever had to loop through a number of plotting parameters in matplotlib? Say you have two datasets and you'd like to compare them to one another. Maybe something like this:


<div class="input_area" markdown="1">

```python
import matplotlib.pyplot as plt
import numpy as np
import mne
%matplotlib inline

# Create fake data
data1 = np.random.randn(500)
data1 = mne.filter.filter_data(data1, 100, None, 3)
data2 = data1 + np.random.randn(500) * .1

# Plot
linewidths = [6, 1]
colors = ['k', 'r']
alphas = [.3, 1]
fig, ax = plt.subplots()
for i_data, color, lw, alpha in zip([data1, data2], colors, linewidths, alphas):
    ax.plot(i_data[50:450], c=color, lw=lw, alpha=alpha)
```

</div>


![png](images/2017/ntbk/2017-01-04-matplotlib_cycles_2_0.png)


There's really a lot of unnecessary code going on above. We're defining objects that share the same name as the kwarg that they represent. We can't store them as dictionaries, because then we'd have to do some python-fu in order to get them to iterate properly. This is where `cycler` is handy:


<div class="input_area" markdown="1">

```python
# Plot the same thing, but now it's more readable and compact
cycler = plt.cycler(lw=[6, 1], c=['k', 'r'], alpha=[.3, 1])
fig, ax = plt.subplots()
for i_data, kwargs in zip([data1, data2], cycler):
    ax.plot(i_data[50:450], **kwargs)
```

</div>


![png](images/2017/ntbk/2017-01-04-matplotlib_cycles_4_0.png)


You can even cycle through more complex properties like colormaps. Let's create one that cycles through several colormaps for a plot:


<div class="input_area" markdown="1">

```python
cyc = plt.cycler(s=np.linspace(200, 50, 3),
                 cmap=['viridis', 'magma', 'coolwarm'],
                 alpha=[.25, .5, .75],
                 lw=[0, .1, .5])

# You can print the cycler, or use nice jupyter notebook support
print(cyc)
cyc
```

</div>

{:.output_stream}
```
%25252528%25252528%25252528cycler%25252528%25252527lw%25252527%2525252C%25252520%2525255B0%2525252C%252525200.1%2525252C%252525200.5%2525255D%25252529%25252520%2525252B%25252520cycler%25252528%25252527s%25252527%2525252C%25252520%2525255B200.0%2525252C%25252520125.0%2525252C%2525252050.0%2525255D%25252529%25252529%25252520%2525252B%25252520cycler%25252528%25252527alpha%25252527%2525252C%25252520%2525255B0.25%2525252C%252525200.5%2525252C%252525200.75%2525255D%25252529%25252529%25252520%2525252B%25252520cycler%25252528%25252527cmap%25252527%2525252C%25252520%2525255B%25252527viridis%25252527%2525252C%25252520%25252527magma%25252527%2525252C%25252520%25252527coolwarm%25252527%2525255D%25252529%25252529%2525250A
```




<table><th>'alpha'</th><th>'cmap'</th><th>'lw'</th><th>'s'</th><tr><td>0.25</td><td>'viridis'</td><td>0</td><td>200.0</td></tr><tr><td>0.5</td><td>'magma'</td><td>0.1</td><td>125.0</td></tr><tr><td>0.75</td><td>'coolwarm'</td><td>0.5</td><td>50.0</td></tr></table>




<div class="input_area" markdown="1">

```python
fig, ax = plt.subplots()
for args in cyc:
    x, y = np.random.randn(2, 100)
    ax.scatter(x, y, c=x, **args)
```

</div>


![png](images/2017/ntbk/2017-01-04-matplotlib_cycles_7_0.png)


So there you have it - cyclers are pretty neat. Give them a shot, and buy a `matplotlib` dev a beer next time you see them for making such an awesome and often under-appreciated package!

> You can check out the MPL cycler page [here](http://matplotlib.org/cycler/)
