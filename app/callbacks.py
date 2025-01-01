import requests, base64
from dash import html
from app.config import PREDICT_API_URL

def display_image(contents):
    if contents is None:
        return "No image detected", "No value availiable"
    try:
        content_type, content_string = contents.split(",")
        decoded_data = base64.b64decode(content_string)
    except Exception as e:
        return "No output availiable.", f"Error: {str(e)}"
    predict_result = requests.post(
        PREDICT_API_URL, 
        files={'file': ("image.png", decoded_data)}).text
    return html.Img(src=contents), predict_result