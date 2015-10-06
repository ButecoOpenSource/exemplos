import numpy as np
import matplotlib.pyplot as plt

data = ((30, 40, 80), ('r', 'g', '#00FF33'), (2013, 2014, 2015))
xPositions = np.arange(len(data[0]))
barWidth = 0.50  # Largura da barra

_ax = plt.axes()  # Cria axes

# bar(left, height, width=0.8, bottom=None, hold=None, **kwargs)
_chartBars = plt.bar(xPositions, data[0], barWidth, color=data[1],
                     yerr=5, align='center')  # Gera barras

for bars in _chartBars:
    # text(x, y, s, fontdict=None, withdash=False, **kwargs)
    _ax.text(bars.get_x() + (bars.get_width() / 2.0), bars.get_height() + 5,
             bars.get_height(), ha='center')  # Label acima das barras

_ax.set_xticks(xPositions)
_ax.set_xticklabels(data[2])

plt.xlabel('Years')
plt.ylabel('Rate')
plt.grid(True)
plt.legend(_chartBars, data[2])

plt.show()
