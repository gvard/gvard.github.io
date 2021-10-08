"""Plot parameters of solar system bodies as vertical lines
https://matplotlib.org/stable/gallery/color/named_colors.html
"""

import matplotlib.pyplot as plt


PL = {
    'me': {'a': 0.387, 'e': 0.206, 'i': 7},
    've': {'a': 0.723, 'e': 0.007, 'i': 3.4},
    'ea': {'a': 1, 'e': 0.016, 'i': 0},
    'ma': {'a': 1.524, 'e': 0.093, 'i': 1.85},
    'ju': {'a': 5.204, 'e': 0.049, 'i': 1.3},
    'sa': {'a': 9.583, 'e': 0.057, 'i': 2.49},
    'ur': {'a': 19.219, 'e': 0.046, 'i': 0.77},
    'ne': {'a': 30.07, 'e': 0.01, 'i': 1.77},
    'ce': {'a': 2.77, 'e': 0.076, 'i': 10.6},
    'pl': {'a': 39.48, 'e': 0.249, 'i': 17.16},
    'ha': {'a': 43.12, 'e': 0.196, 'i': 28.2},
    'mk': {'a': 45.43, 'e': 0.161, 'i': 29},
    'er': {'a': 67.86, 'e': 0.436, 'i': 44.04},
    'go': {'a': 67.485, 'e': 0.499, 'i': 30.6},
    'se': {'a': 491.5, 'e': 0.845, 'i': 11.93},
    }

def plot_vert_pla(b1, b2):
    plt.plot([PL['ve']['a'], PL['ve']['a']], [b1, b2], '--c')
    plt.plot([PL['ea']['a'], PL['ea']['a']], [b1, b2], '--b')
    plt.plot([PL['ma']['a'], PL['ma']['a']], [b1, b2], '--r')
    plt.plot([PL['ce']['a'], PL['ce']['a']], [b1, b2], '--m')
    plt.plot([PL['ju']['a'], PL['ju']['a']], [b1, b2], '--', color='brown')
    plt.plot([PL['sa']['a'], PL['sa']['a']], [b1, b2], '--y',)
    plt.plot([PL['ur']['a'], PL['ur']['a']], [b1, b2], '--c',)
    plt.plot([PL['ne']['a'], PL['ne']['a']], [b1, b2], '--b',)
    plt.plot([PL['pl']['a'], PL['pl']['a']], [b1, b2], '--m')
    plt.plot([PL['er']['a'], PL['er']['a']], [b1, b2], '--m')
    plt.plot([PL['ha']['a'], PL['ha']['a']], [b1, b2], '--m')
    plt.plot([PL['mk']['a'], PL['mk']['a']], [b1, b2], '--m')
    plt.plot([PL['go']['a'], PL['go']['a']], [b1, b2], '--', color='grey')
    plt.plot([PL['se']['a'], PL['se']['a']], [b1, b2], '--', color='grey')


def plot_vert_res(b1, b2):
    plt.plot([36.5, 36.5], [b1, b2], '--k', lw=0.75)
    plt.plot([43.92, 43.92], [b1, b2], '--k', lw=0.75)
    plt.plot([47.8, 47.8], [b1, b2], '--k', lw=0.75)
    plt.plot([55.4, 55.4], [b1, b2], '--k', lw=0.75)


def plot_vert_kirkwood(b1, b2, lw=0.7):
    plt.plot([1.78, 1.78], [b1, b2], '--k', lw=lw)
    plt.plot([2.065, 2.065], [b1, b2], '--k', lw=lw)
    plt.plot([2.502, 2.502], [b1, b2], '--k', lw=lw)
    plt.plot([2.825, 2.825], [b1, b2], '--k', lw=lw)
    plt.plot([2.958, 2.958], [b1, b2], '--k', lw=lw)
    plt.plot([3.279, 3.279], [b1, b2], '--k', lw=lw)
    plt.plot([3.972, 3.972], [b1, b2], '--k', lw=lw)

def planets_ae(mode='e'):
    plt.plot(0, 0, 'oy', ms=12)
    plt.plot(PL['me']['a'], PL['me'][mode], 'o', color='orange', ms=6)
    plt.plot(PL['ve']['a'], PL['ve'][mode], 'oc', ms=6)
    plt.plot(1, PL['ea'][mode], 'ob', ms=6)
    plt.plot(PL['ma']['a'], PL['ma'][mode], 'or', ms=6)
    plt.plot(PL['ju']['a'], PL['ju'][mode], 'o', color='brown', ms=6)
    plt.plot(PL['sa']['a'], PL['sa'][mode], 'oy', ms=6)
    plt.plot(PL['ur']['a'], PL['ur'][mode], 'oc', ms=6)
    plt.plot(PL['ne']['a'], PL['ne'][mode], 'ob', ms=6)
    plt.plot(PL['ce']['a'], PL['ce'][mode], 'om', ms=6)
    plt.plot(PL['pl']['a'], PL['pl'][mode], 'om', ms=6)
    plt.plot(PL['ha']['a'], PL['ha'][mode], 'om', ms=6)
    plt.plot(PL['mk']['a'], PL['mk'][mode], 'om', ms=6)
    plt.plot(PL['er']['a'], PL['er'][mode], 'om', ms=6)
    plt.plot(PL['go']['a'], PL['go'][mode], 'o', color='grey', ms=6)