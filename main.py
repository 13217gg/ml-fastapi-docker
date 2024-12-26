from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

app = FastAPI()

# Load model
model = load_model("mnist_model.h5")

class PredictionResponse(BaseModel):
    predicted_number: int

def preprocess_image(image: Image.Image) -> np.ndarray:
    image = image.convert("L").resize((28, 28))  
    image_array = np.array(image) / 255.0  
    image_array = image_array.reshape(1, 28, 28, 1)
    return image_array

@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    """make predictions"""
    image = Image.open(file.file)
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    predicted_number = np.argmax(prediction)
    return PredictionResponse(predicted_number=predicted_number)
