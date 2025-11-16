import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def plot_backtest(data, ticker):
    """
    Plots the backtesting results and returns a base64 encoded image.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)

    data['Close'].plot(label=ticker)
    ax.plot(data.loc[data['signals'] == 1].index, data['Close'][data['signals'] == 1], label='LONG', lw=0, marker='^', c='g')
    ax.plot(data.loc[data['signals'] == -1].index, data['Close'][data['signals'] == -1], label='SHORT', lw=0, marker='v', c='r')

    plt.legend(loc='best')
    plt.grid(True)
    plt.title('Positions')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    encoded_string = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)

    return encoded_string
