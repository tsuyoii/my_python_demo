import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

# app.layout = html.H1('hello itachi')
app.layout = html.Div(children=[
    html.H1(children='hello Dash'),
    html.Div(children='''
            Dash:Python网络应用框架'''),
    dcc.Graph(
        id="example-graph",
        figure={
            'data': [
                {'x':[1,2,3],'y':[4,1,2],'type':'bar','name':'北京'},
                {'x':[1,2,3],'y':[2,4,5],'type':'line','name':'天津'},
            ],
            'layout':{
                'title':'数据'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)