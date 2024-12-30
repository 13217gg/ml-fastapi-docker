from dash import Dash, html, dcc, callback, Input, Output
import requests, base64
app = Dash()

app.layout = html.Div([
    html.H6("Upload your image here", 
            style={"color":"blue",
                   "font-size":"20px"}),
    dcc.Upload(id="upload-image",
               children=html.Div(["Drag and drop or ", html.A('Select an image')])),
    html.Div(id="output-image"),
    html.Div(id="output-value")
])


@callback(
    [Output(component_id='output-image', component_property='children'),
     Output(component_id='output-value', component_property='children')],
    Input(component_id='upload-image', component_property='contents')
)
def display_image(contents):
    if contents is None:
        return "No image detected", "No value availiable"
    try:
        content_type, content_string = contents.split(",")
        decoded_data = base64.b64decode(content_string)
    except Exception as e:
        return "No output availiable.", f"Error: {str(e)}"
    predict_result = requests.post(
        "http://localhost:12347/predict", 
        files={'file': ("image.png", decoded_data)}).text
    return html.Img(src=contents), predict_result

if __name__ == '__main__':
    app.run(debug=True)