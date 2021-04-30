from scour import scour
import matplotlib.pyplot as plt


def autolabel(rects1, rects2, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for x, rect in enumerate(rects1):
        height = rect.get_height() + rects2[x].get_height()
        ax.annotate(height, (rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 5), textcoords="offset points", ha='center')


def plot_bar(xes, data, data2, labels, pth, xlim, width=0.85, lab0=None):
    plt.rcParams['svg.fonttype'] = 'none'
    title, xlabel, ylabel = labels
    fig, ax = plt.subplots(figsize=(13, 9.5))
    p1 = ax.bar(xes, data, width)
    p2 = ax.bar(xes, data2, width, bottom=data)
    autolabel(p1, p2, ax)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.title(title, fontsize=22)
    plt.xticks(xes)
    if lab0:
        xes[0] = lab0
    ax.set_xticklabels(xes)
    plt.xlim(xlim[0], xlim[1])
    plt.subplots_adjust(left=0.07, bottom=0.06, right=0.97, top=0.96)
    plt.savefig(pth)


def optimize_svg(tmp_pth, pth):
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