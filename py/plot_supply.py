"""Python module with supplement functons for matplotlib plots
"""

from scour import scour
import matplotlib.pyplot as plt


def autolabel(rects1, rects2, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for x, rect in enumerate(rects1):
        height = rect.get_height() + rects2[x].get_height()
        ax.annotate(height, (rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 5), textcoords="offset points", ha='center')


def plot_bar(xes, data, data2, labels, pth, xlim, width=0.85, lab0=None):
    # plt.rcParams['svg.fonttype'] = 'none'
    title, xlabel, ylabel = labels
    _fig, ax = plt.subplots(figsize=(16, 9))
    p1 = ax.bar(xes, data, width)
    p2 = ax.bar(xes, data2, width, bottom=data)
    autolabel(p1, p2, ax)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.title(title, fontsize=16)
    plt.xticks(xes)
    if lab0:
        xes[0] = lab0
    # for i, x in enumerate(xes):
    #     xes[i] = str(x) + "0"
    ax.set_xticklabels(xes)
    plt.xlim(xlim[0], xlim[1])
    plt.subplots_adjust(left=0.06, bottom=0.06, right=0.97, top=0.955)
    plt.savefig(pth, dpi=240)


def optimize_svg(tmp_pth, pth):
    """Optimize svg file with scour (use pip to install it)."""
    inputfile = open(tmp_pth, 'rb')
    outputfile = open(pth, 'wb')
    options = scour.generateDefaultOptions()
    options.enable_viewboxing = True
    options.strip_comments = True
    options.strip_ids = True
    options.remove_metadata = True
    options.indent_type = 'none'
    options.shorten_ids = True
    scour.start(options, inputfile, outputfile)
    inputfile.close()
    outputfile.close()
