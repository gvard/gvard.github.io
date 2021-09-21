'use strict';
function mkChart() {
  const NEO_SIZE_URL = 'https://cneos.jpl.nasa.gov/stats/size_bin.json';
  const URL = 'https://json2jsonp.com/?url=' + NEO_SIZE_URL + '&callback=mkNEASizeBinChart';
  const s = document.createElement("script");
  s.src = URL;
  document.head.appendChild(s);
}
function mkNEASizeBinChart(jdata) {
  const options = {
  chart: {
    type: 'column',
    renderTo: 'nea_size_bin_chart'
  },
  title: { text: 'Near-Earth Asteroids Discovered' },
  subtitle: { text: 'Total per Size Bin' },
  xAxis: {
    categories: ['0-30', '30-100', '100-300', '300-1000', '1000+'],
    title: { text: 'Estimated Diameter (m)' },
    gridLineWidth: 0,
    minorGridLineWidth: 0
  },
  yAxis: {
    title: { text: 'Total Discovered' },
    labels: { format: "{value:,.0f}" },
    gridLineWidth: 0,
    minorGridLineWidth: 0
  },
  plotOptions: {
    series: {
      animation: {
        enabled: true,
        duration: 100
      }
    },
    column: {
      pointPadding: 0,
      groupPadding: 0.1,
      dataLabels: {
        enabled: true,
        inside: false,
        crop: false,
        overflow: 'none',
        // textShadow: '' is needed to avoid duplicate label on export
        style: { textShadow: '', textStyle: 'bold' }
      }
    }
  },
  series: [{
    showInLegend: false,
    enableMouseTracking: false,
    data: []
  }],
  credits: { enabled: false },
  exporting: {
    filename: "nea_size_bin_chart",
    chartOptions: {
      labels: {
        style: { 'font-size': '10px', color: '#666' },
        items: [
          {
            html: "https://cneos.jpl.nasa.gov/stats/",
            style: { left: '-60px', top: '315px' }
          },
          {
            html: "Alan Chamberlin (JPL/Caltech)",
            style: { 'text-align': 'right', left: '350px', top: '315px' }
          }
        ]
      }
    }
  }
  };
  options.subtitle.text = 'Total per Size Bin (as of <b>' + jdata.dataDate + '</b>)';
  options.series[0].data = jdata.data;
  const chart = new Highcharts.Chart(options);
}