import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

dados_conceitos = dict(
    java =       {'variáveis': 3, 'condicionais': 6, 'loops': 2, 'poo': 1, 'funções': 1 },
    python =     {'variáveis': 9, 'condicionais': 6, 'loops': 5, 'poo': 3, 'funções': 3 },
    sql  =       {'variáveis': 7, 'condicionais': 4, 'loops': 5, 'poo': 3, 'funções': 3 },
    golang =     {'variáveis': 8, 'condicionais': 5, 'loops': 4, 'poo': 1, 'funções': 1 },
    javascript = {'variáveis': 8, 'condicionais': 6, 'loops': 3, 'poo': 2, 'funções': 1 }
)
 
color_map = dict(
    java = 'red',
    python = 'blue',
    sql = 'green',
    golang = 'orange',
    javascript = 'yellow'
)

app  = dash.Dash(__name__)  #app passa a ser um objeto da classe dash

# __________________________Layout_____________________________

app.layout = html.Div([
    html.H1('Keilla Nazima',style={'text-align':'center'}),

    html.Div(
        dcc.Dropdown(
            id='dropdown_linguagens',
            options = [
                {'label': 'Java', 'value': 'java'},
                {'label': 'Python', 'value': 'python'},
                {'label': 'SQL', 'value': 'sql'},
                {'label': 'GOLang', 'value': 'golang'},
                {'label': 'JavaScript', 'value': 'javascript'}               
            ], 
            value=['java'],
            multi=True,
            style={'width': '70%', 'margin': '0 auto'} 
        )

    ),
    dcc.Graph(
        id='scatter_plot'
    )

])




#___________________________Callbacks___________________________

@app.callback(
    Output('scatter_plot', 'figure'),
    [Input('dropdown_linguagens','value')]

)
def atualizar_scatter(linguagens_selecionadas):

    scatter_trace = []

    for linguagem in linguagens_selecionadas:
        dados_linguagem = dados_conceitos[linguagem]
        for conceito, conhecimento in dados_linguagem.items():
            scatter_trace.append(
                go.Scatter(
                    x=[conceito],
                    y=[conhecimento],
                    mode='markers',
                    name=linguagem.title(),
                    marker = dict(
                        size=20, 
                        color=color_map[linguagem]
                    ),
                    showlegend=False
                )
            )
    
    scatter_layout = go.Layout(
        title='Minhas linguagens',
        xaxis=dict(title='Conceitos',showgrid=False),
        yaxis=dict(title='Nível de conhecimento', showgrid=False)
    )

    return {'data': scatter_trace, 'layout': scatter_layout}




if __name__ == '__main__':
    app.run_server(debug=True)





