import io
import cv2
import mediapipe as mp
from fastapi import FastAPI, File, UploadFile
from starlette.responses import StreamingResponse
from predictor import SelfiePredictor

mp_drawing = mp.solutions.drawing_utils
mp_selfie = mp.solutions.selfie_segmentation

app = FastAPI(title="Servicio web")


@app.post("/selfie")
def selfie_segmentation(bg_r: int = 0, bg_g: int = 0, bg_b: int = 0, image_file: UploadFile = File(...)):
    predictor = SelfiePredictor(bg_color=(bg_r, bg_g, bg_b))
    output = predictor.predict_file(image_file.file)
    res, img_png = cv2.imencode(".png", output)
    return StreamingResponse(io.BytesIO(img_png.tobytes()), media_type="image/png")
