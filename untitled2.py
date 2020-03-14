# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:26:30 2020

@author: Xiaomi
"""



import dash
import dash_core_components as dcc
import dash_html_components as html
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1(
        children='Привет, я Люба',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(
        html.Img(src='https://sun9-22.userapi.com/c845120/v845120775/19c7d8/5VIjhb0oP_Y.jpg', style={
        'width':'65%', 'margin':70, 'textAlign': 'center'})
    ),

    html.Div(children='''
        Я люблю котиков ^^    ''',
                style={
            'textAlign': 'center',
            'color': colors['text']
    }),

])

if __name__ == '__main__':
    app.run_server(debug=True)
