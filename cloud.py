import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
import numpy.random as r
m_file = open('python.txt','r',encoding = 'utf-8')
m_read = m_file.read()
m_file.close()
m_read = m_read.lower()
tokens = word_tokenize(m_read)
tokens = [t for t in tokens if t.isalpha()]
fdist = FreqDist(tokens)
word_dict = fdist.most_common(50)
word_dict = dict(word_dict)

df = pd.read_csv('titanic.csv',sep=';')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Hello Dash'),
    html.Div('This is an example paragraph', style = {'color':'blue'}),
    dcc.RadioItems(
        id = 'radio',
        options = [
            {'label': 'Male', 'value':'male'},
            {'label': 'Female','value':'female'},
            ],
        value = 'male',
        labelStyle={'display': 'inline-block'}
        ),
    dcc.Graph(
        id = 'graph',
        figure=go.Figure(
           ))
    
    ],
    style = {'text-align':'center'})

@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('radio', 'value')])
def update_output(value):
    y_array_dict = {
        'male': [len(df[(df['Sex']=='male') & (df['Survived']==1)]),len(df[(df['Sex']=='male') & (df['Survived']==0)])],
        'female': [len(df[(df['Sex']=='female') & (df['Survived']==1)]),len(df[(df['Sex']=='female') & (df['Survived']==0)])] 
    }
    return {
        'data': [{
            'type':'scatter',
            'width':150,
            'height':150,
            'y': [r.random() for y in range(len(list(word_dict.keys())))],
            'x': [r.random() for y in range(len(list(word_dict.keys())))],
            'mode': 'text',
            'text' : list(word_dict.keys()),
            'textfont':{'size': [ w*4 for w in list(word_dict.values()) ],
                           'color': ['red','blue']}
        }],
        'layout': {
            #'title': value,
            'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
            'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
            
        }
    }


if __name__ == '__main__':
    app.run_server(debug=True)
