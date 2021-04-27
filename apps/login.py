import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
plt.style.use('fivethirtyeight')
import dash_core_components as dcc
import dash_html_components as html
login = html.Div([dcc.Location(id='url_login', refresh=True)
                     , html.H2('''Please log in to continue:''', id='h1'),
                  html.Div(
                     dcc.Input(placeholder='Enter your username',
                                 type='text',
                                 id='uname-box')
                      , style={"padding": "1%","color":"black"})

                     , html.Br(),
                  html.Div(
                     dcc.Input(placeholder='Enter your password',
                                 type='password',
                                 id='pwd-box')
                     , style = {"padding": "1%", "color":"black"})

                , html.Br(),
                  html.Div(
                     html.Button(children='Login',
                                   n_clicks=0,
                                   type='submit',
                                   id='login-button')
                     , style = {"padding": "1%"})

                    , html.Br()
                     , html.Br()

                  ],style={"background-color":"#1C202D", "width":"60%","padding":"5%", "margin-left":"20%", "margin-top":"5%", "color":"white"})  # end div


# end div
