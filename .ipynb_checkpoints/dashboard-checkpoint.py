import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load Provider Summary
df = pd.read_csv("provider_summary.csv")

app = Dash(__name__)

fig1 = px.bar(df, x="Provider_Name", y="TotalVisits",
             title="Total Visits per Provider", text="TotalVisits")
fig1.update_traces(textposition="outside")

fig2 = px.bar(df, x="Provider_Name", y="ComplianceRate",
             title="Compliance Rate per Provider",
             text=df["ComplianceRate"].apply(lambda x: f"{x:.1%}"))
fig2.update_traces(textposition="outside")

app.layout = html.Div(children=[
    html.H1(children="Primary Care Performance Dashboard"),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2)
])

if __name__ == "__main__)":
    app.run_server(debug=True)