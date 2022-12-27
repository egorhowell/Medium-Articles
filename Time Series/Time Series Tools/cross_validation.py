# Import packages
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit, KFold
from sklearn.metrics import mean_absolute_percentage_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import os


def plot_time_series(df: pd.DataFrame,
                     save_file_path: str) -> None:
    """General function to plot the passenger data."""

    fig = px.line(df, x='Month', y='#Passengers', labels={'Month': 'Date', '#Passengers': 'Passengers'})
    fig.update_layout(template="simple_white", font=dict(size=18), title_text='Airline Passengers',
                      width=650, title_x=0.5, height=400)

    if not os.path.exists("../images"):
        os.mkdir("../images")

    fig.write_image("../images/" + str(save_file_path))

    return fig.show()


def plot_cross_val(n_splits: int,
                   splitter_func,
                   df: pd.DataFrame,
                   title_text: str,
                   save_path: str) -> None:
    """Function to plot the cross validation of various
    sklearn splitter objects."""

    split = 1
    plot_data = []

    for train_index, valid_index in splitter_func(n_splits=n_splits).split(df):
        plot_data.append([train_index, 'Train', f'{split}'])
        plot_data.append([valid_index, 'Test', f'{split}'])
        split += 1

    plot_df = pd.DataFrame(plot_data, columns=['Index', 'Dataset', 'Split']).explode('Index')

    fig = go.Figure()
    for _, group in plot_df.groupby('Split'):
        fig.add_trace(go.Scatter(x=group['Index'].loc[group['Dataset'] == 'Train'],
                                 y=group['Split'].loc[group['Dataset'] == 'Train'],
                                 name='Train',
                                 line=dict(color="blue", width=10)
                                 ))
        fig.add_trace(go.Scatter(x=group['Index'].loc[group['Dataset'] == 'Test'],
                                 y=group['Split'].loc[group['Dataset'] == 'Test'],
                                 name='Test',
                                 line=dict(color="goldenrod", width=10)
                                 ))

    fig.update_layout(template="simple_white", font=dict(size=20), title_text=title_text,
                      title_x=0.5, width=850, height=450, xaxis_title='Index', yaxis_title='Split')

    names = set()
    fig.for_each_trace(
        lambda trace:
        trace.update(showlegend=False)
        if (trace.name in names) else names.add(trace.name))

    if not os.path.exists("../images"):
        os.mkdir("../images")

    fig.write_image("../images/" + str(save_path))

    return fig.show()


def hyperparameter_tuning_season_cv(n_splits: int,
                                    gammas: list[float],
                                    df: pd.DataFrame) -> pd.DataFrame:
    """Function to carry out cross-validation hyperparameter tuning
    for the seasonal parameter in a Holt Winters' model. """

    tscv = TimeSeriesSplit(n_splits=n_splits)
    error_list = []

    for gamma in gammas:
        errors = []
        for train_index, valid_index in tscv.split(df):
            train, valid = df.iloc[train_index], df.iloc[valid_index]

            model = ExponentialSmoothing(train['#Passengers'], trend='mul',
                                         seasonal='mul', seasonal_periods=12) \
                .fit(smoothing_seasonal=gamma)

            forecasts = model.forecast(len(valid))
            errors.append(mean_absolute_percentage_error(valid['#Passengers'], forecasts))

        error_list.append([gamma, sum(errors) / len(errors)])

    return pd.DataFrame(error_list, columns=['Gamma', 'MAPE'])


def plot_error_cv(df: pd.DataFrame,
                  title: str,
                  save_path: str) -> None:
    """Bar chart to plot the errors from the different
    hyperparameters."""

    fig = px.bar(df, x='Gamma', y='MAPE')
    fig.update_layout(template="simple_white", font=dict(size=18), title_text=title,
                      width=800, title_x=0.5, height=400)

    if not os.path.exists("../images"):
        os.mkdir("../images")

    fig.write_image("../images/" + str(save_path))

    return fig.show()


if __name__ == "__main__":

    # Read in the data
    data = pd.read_csv('AirPassengers.csv')
    data['Month'] = pd.to_datetime(data['Month'])

    # Plot the time series
    plot_time_series(df=data, save_file_path='timeseries.png')

    # Plot the two type of cv splits
    plot_cross_val(n_splits=5, splitter_func=KFold, df=data,
                   title_text='Cross-Validation', save_path='kfold.png')

    plot_cross_val(n_splits=5, splitter_func=TimeSeriesSplit, df=data,
                   title_text='Time Series Cross-Validation', save_path='time_series.png')

    # Carry out cv for hyperparameter tuning for the seasonal parameter
    error_df = hyperparameter_tuning_season_cv(df=data,
                                               n_splits=4,
                                               gammas=list(np.arange(0, 1.1, 0.1)))

    # Plot the tuning results
    plot_error_cv(df=error_df, title='Hyperparameter Results', save_path='results.png')