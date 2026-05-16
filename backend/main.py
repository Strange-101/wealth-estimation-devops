from fastapi import FastAPI, UploadFile, File
import shutil
from backend.model import predict

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "Wealth Estimation API Running"
    }

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):

    file_path = file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = predict(file_path)

    return result