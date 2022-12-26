# Import packages
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit, KFold
import os

# Read in the data
data = pd.read_csv('AirPassengers.csv')
data['Month'] = pd.to_datetime(data['Month'])

# Split modelling and test
df_model = data.iloc[:-int(len(data) * 0.2)]
df_test = data.iloc[-int(len(data) * 0.2):]


def plot_cross_val(n_splits: int,
                   splitter_func,
                   df: pd.DataFrame,
                   title_text: str,
                   save_path: str) -> None:
    split = 1
    plot_data = []

    for train_index, valid_index in splitter_func(n_splits=n_splits).split(df):
        plot_data.append([train_index, 'Train', f'{split}'])
        plot_data.append([valid_index, 'Valid', f'{split}'])
        split += 1

    plot_df = pd.DataFrame(plot_data, columns=['Index', 'Dataset', 'Split'])
    plot_df = plot_df.explode('Index')

    fig = go.Figure()
    for _, group in plot_df.groupby('Split'):
        fig.add_trace(go.Scatter(x=group['Index'].loc[group['Dataset'] == 'Train'],
                                 y=group['Split'].loc[group['Dataset'] == 'Train'],
                                 name='Train',
                                 line=dict(color="blue", width=10)
                                 ))
        fig.add_trace(go.Scatter(x=group['Index'].loc[group['Dataset'] == 'Valid'],
                                 y=group['Split'].loc[group['Dataset'] == 'Valid'],
                                 name='Valid',
                                 line=dict(color="goldenrod", width=10)
                                 ))

    fig.update_layout(template="simple_white", font=dict(size=20), title_text=title_text,
                      title_x=0.5, width=900, height=600, xaxis_title='Index', yaxis_title='Split')

    names = set()
    fig.for_each_trace(
        lambda trace:
        trace.update(showlegend=False)
        if (trace.name in names) else names.add(trace.name))

    if not os.path.exists("../images"):
        os.mkdir("../images")

    fig.write_image("../images/" + str(save_path))

    return fig.show()


plot_cross_val(n_splits=5, splitter_func=TimeSeriesSplit, df=df_model, title_text='cross-val', save_path='image.png')
