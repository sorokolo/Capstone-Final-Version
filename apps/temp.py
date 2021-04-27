import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import dash_core_components as dcc
import dash_html_components as html

logout = html.Div([dcc.Location(id='temp', refresh=True)
                      , html.Br(),
                   # html.Div(id='graph_img'),
                   # html.Div(id='graph_img2'),
                   # html.Div(id='graph_img3'),
                   # html.Div(id='graph_img4'),
                   # html.Div(id='graph_img5'),
                   # html.Div(id='graph_img6'),
                   ])  # end div
