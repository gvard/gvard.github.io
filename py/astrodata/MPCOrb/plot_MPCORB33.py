import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

from plot_supply import plot_vert_pla, plot_vert_res


DATA = np.genfromtxt('data/MPCORB.DAT.gz', usecols=(8, 10), skip_header=43,
    delimiter=(7, 6, 7, 5, 10,
        11, 11, 11, 11, 12,
        14, 2, 10, 6, 4,
        10, 5, 4, 4, 11,
        5, 28, 9),
    dtype=[('Names', 'U7'), ('H', 'f8'), ('G', 'f8'), ('Ep', 'U5'), ('M', 'f8'),
        ('Peri', 'f8'), ('Node', 'f8'), ('i', 'f8'), ('e', 'f8'), ('n', 'f8'),
        ('a', 'f8'), ('U', 'U1'), ('Ref', 'U10'), ('Obs', 'int'), ('Opp', 'int'),
        ('Arc', 'U9'), ('rms', 'f8'), ('p1', 'U3'), ('p2', 'U3'), ('Com', 'U10'),
        ('Flags', 'U4'), ('Desig', 'U27'), ('Last', 'int')])

a1, a2, b1, b2, bins = 29, 70, 0, 90, 900
Filtered = DATA[DATA['a'] >= a1]
Filtered = Filtered[Filtered['a'] <= a2]
fig, ax = plt.subplots(figsize=(16, 9))
fig.subplots_adjust(0.048, 0.06, 0.99, 0.97)
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(AutoMinorLocator())
plt.hist(Filtered['a'], bins=bins)
plot_vert_pla(b1, b2)
plot_vert_res(b1, b2)
plt.ylim(b1, b2)
plt.xlim(a1, a2)
plt.title('Распределение ' + str(len(Filtered)) + \
          ' малых планет по большой полуоси: октябрь 2021 г.')
plt.xlabel('Большая полуось орбиты, а.е.', fontsize=14)
plt.ylabel('Количество объектов', fontsize=14)
plt.savefig('graph/hist-a28-71-700ml-filt.png', dpi=120)