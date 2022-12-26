# Import packages
import plotly.express as px
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit
import os

# Read in the data
data = pd.read_csv('AirPassengers.csv')
data['Month'] = pd.to_datetime(data['Month'])

# Split modelling and test
df_model = data.iloc[:-int(len(data) * 0.2)]
df_test = data.iloc[-int(len(data) * 0.2):]


def plot_cross_val(n_splits: int,
                   data: pd.DataFrame,
                   save_file_path: str) -> None:
    """Function to plot time series cross validation splits."""

    tscv = TimeSeriesSplit(n_splits=n_splits)
    split = 1
    plot_data = []

    for train_index, valid_index in tscv.split(data):
        plot_data.append([max(train_index), 'Train', f'{split}'])
        plot_data.append([max(valid_index)-max(train_index), 'Valid', f'{split}'])
        split += 1

    plot_df = pd.DataFrame(plot_data, columns=['Index', 'Dataset', 'Split'])

    fig = px.bar(plot_df, x="Index", y="Split", color='Dataset', orientation='h',
                 color_discrete_map={'Train': 'blue', 'Valid': 'goldenrod'})
    fig.update_layout(template="simple_white", font=dict(size=20), title_text='Time Series Cross-Validation',
                      title_x=0.5, width=750, height=400)
    fig.update_traces(width=0.5)

    if not os.path.exists("../images"):
        os.mkdir("../images")

    fig.write_image("../images/" + str(save_file_path))

    return fig.show()


plot_cross_val(5, df_model, 'crossval.png')

