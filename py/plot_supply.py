import matplotlib.pyplot as plt


def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')


def plot_bar(xes, data, labels, pth, xlim, width=0.8, dpi=60):
    plt.rcParams['svg.fonttype'] = 'none'
    title, xlabel, ylabel = labels
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=dpi)
    p1 = ax.bar(xes, data, width)
    autolabel(p1, ax)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.title(title, fontsize=22)
    plt.xticks(xes)
    plt.xlim(xlim[0], xlim[1])
    plt.subplots_adjust(left=0.07, bottom=0.06, right=0.97, top=0.96)
    plt.savefig(pth)
