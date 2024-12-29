from dash import Dash, html, dcc, callback, Input, Output
app = Dash()

app.layout = html.Div([
    html.H6("Upload your image here", 
            style={"color":"blue",
                   "font-size":"50px"}),
    dcc.Upload(id="upload-image",
               children=html.Div(["Drag and drop or ", html.A('Select an image')])),
    html.Div(id="output-value")
])


@callback(
    [Output(component_id='output-image', component_property='children'),
     Output(component_id='output-value', component_property='children')],
    Input(component_id='upload-image', component_property='contents')
)
def display_image(contents):
    return html.Img(src=contents)

if __name__ == '__main__':
    app.run(debug=True)