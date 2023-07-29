# Stars related statistics

See this links for more stars related [plots](https://github.com/gvard/astrodata/tree/main/plots/stars/), [code](https://github.com/gvard/astrodata/tree/main/src/astrodata/stars/) and [data](https://github.com/gvard/astrodata/tree/main/data/stars/)

[Supernovae and transients stats](../snstats/) page

## Supernovae and other transients observations

* History of supernovae observations by year
![Supernovae observations](https://raw.githubusercontent.com/gvard/astrodata/main/plots/stars/sne_stats_bar_chart.svg "Supernovae observations. Data from the Latest Supernovae Archives")
![Increasing number of supernova discoveries, years 2015-2023](https://raw.githubusercontent.com/gvard/astrodata/main/plots/stars/sne_discoveries_numbers-2015-2023.png "Increasing number of supernova discoveries, years 2015-2023. Data from the Latest Supernovae Archives")
* Cumulative number of supernovae
![Cumulative number of supernovae](https://raw.githubusercontent.com/gvard/astrodata/main/plots/stars/sne_transients_total_number_log_plot.svg "Cumulative number of supernovae")
* History of transient observations by year from Transient Name Server
![Transient observations from Transient Name Server](https://raw.githubusercontent.com/gvard/astrodata/main/plots/stars/transient_stats_bar_chart.svg "Transient observations from Transient Name Server")
[Data as JSON](https://github.com/gvard/astrodata/blob/main/data/stars/sne-stats.json).
Data sources: [David Bishop, Latest Supernovae Archives](https://www.rochesterastronomy.org/snimages/archives.html),
[Transient Name Server stats](https://www.wis-tns.org/stats-maps),
[Central Bureau for Astronomical Telegrams List of SNe](http://www.cbat.eps.harvard.edu/lists/Supernovae.html).
Code: [python script with data for plotting this charts](https://github.com/gvard/astrodata/blob/main/src/astrodata/stars/plot_sne_transients_stats.py)

## Gamma-ray bursts observations

![Number of gamma-ray bursts which have been localized within a few hours to days to less than 1 degree](https://raw.githubusercontent.com/gvard/astrodata/main/plots/stars/grbs_total_number_plot.png "Number of gamma-ray bursts which have been localized within a few hours to days to less than 1 degree")
![Gamma-ray bursts localized within a few hours to days to less than 1 degree: chart with number of optical afterglows](https://raw.githubusercontent.com/gvard/astrodata/main/plots/stars/grbs_stats_bar_chart.svg "Gamma-ray bursts localized within a few hours to days to less than 1 degree: chart with number of optical afterglows")
Data source: [Jochen Greiner; GRBs localized within a few hours to days to less than 1 degree](https://www.mpe.mpg.de/~jcg/grbgen.html), [data as JSON](https://github.com/gvard/astrodata/blob/main/data/stars/grbs-localized-stats.json).
Code: [python script with data for plotting this charts](https://github.com/gvard/astrodata/blob/main/src/astrodata/stars/plot_localized_grbs_stats.py)

Data sources:

* [David Bishop, Latest Supernovae Archives](https://www.rochesterastronomy.org/snimages/archives.html)
* [Transient Name Server](https://www.wis-tns.org/stats-maps)
* [SIMBAD Astronomical Database statistics](https://simbad.u-strasbg.fr/simbad/)
