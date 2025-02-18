from AttoSourceFigClass import AttoSourcePlot
from adjustText import adjust_text

atto = AttoSourcePlot(source_type='HHG', pulse_type='IAP', x_axis='PhotonEng', y_axis='PulseEng')
atto.plot(plot_labels='a', plot_markers='bo', x_scale='log', y_scale='log')

atto.pulse_type = 'APT'
atto.plot(plot_labels='aa', plot_markers='bv')

atto.pulse_type = 'IAP'
atto.set_source('FEL')
atto.plot(plot_labels='A', plot_markers='ro')

atto.pulse_type = 'APT'
atto.set_source('FEL')
atto.plot(plot_labels='AA', plot_markers='rv')

adjust_text(atto.texts, only_move={'points':'x', 'texts':'x'}, force_points=1, autoalarrowprops=dict(arrowstyle="->", color='r', lw=0.5))
atto.fig.legend(bbox_to_anchor=(1.5, 1), loc='outside upper right')
atto.ax.grid()
atto.ax.set(xlabel='Photon Energy (eV)', ylabel='Pulse Energy (J)')

atto.emblish()
