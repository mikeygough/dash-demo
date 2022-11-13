# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


# note that layout is a tree of components
app.layout = html.Div(children=[
    # this is the same as: <h1>Hello Dash</h1>
    html.H1(children='Hello, world!'),
    # can also be written since 'children' is always the first attribute:
    # html.H1('Hello Dash')

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    # higher level components that aren't just javascript:
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
