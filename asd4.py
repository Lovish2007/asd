import pandas as pd
import plotly.figure_factory as ff
import csv

df = pd.read_csv("asd_data1.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["rating"], show_hist = False)
fig.show()