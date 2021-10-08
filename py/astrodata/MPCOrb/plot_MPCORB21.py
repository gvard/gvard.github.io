import numpy as np
import matplotlib.pyplot as plt

from plot_supply import plot_vert_pla


DATA = np.genfromtxt('data/MPCORB.DAT.gz', usecols=10, skip_header=43)
ind = np.argsort(DATA)
data_sorted = DATA[ind]
a1, a2, b1, b2 = 0, 68.5, 0, 1800
cut = int(min(np.argwhere(data_sorted >= a2)))

fig, ax = plt.subplots(figsize=(16, 9))
fig.subplots_adjust(0.048, 0.06, 0.99, 0.97)
plt.hist(data_sorted[:cut], bins=3050)

plot_vert_pla(b1, b2)
plt.ylim(b1, b2)
plt.xlim(a1, a2)
plt.title('Распределение ' + str(len(data_sorted[:cut])) + \
          ' малых планет по большой полуоси: октябрь 2021 г.')
plt.xlabel('Большая полуось орбиты, а.е.', fontsize=14)
plt.ylabel('Количество объектов', fontsize=14)
plt.savefig('graph/hist-a68-1800m.png', dpi=120)