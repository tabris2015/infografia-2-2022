import io
import cv2
from fastapi import FastAPI, File, UploadFile
from starlette.responses import StreamingResponse
from predictor import SelfiePredictor

app = FastAPI(title="Servicio web de eliminacion de fondo")


@app.post("/selfie")
def selfie_segmentation(
    bg_r: int = 0, 
    bg_g: int = 0, 
    bg_b: int = 0, 
    image_file: UploadFile = File(...)
    ):
    predictor = SelfiePredictor(bg_color=(bg_r, bg_g, bg_b))
    output = predictor.predict_file(image_file.file)
    res, img_png = cv2.imencode(".png", output)
    return StreamingResponse(io.BytesIO(img_png.tobytes()), media_type="image/png")

@app.get("/saludo")
def saludo(nombre: str, edad: int):
    return {"mensaje": f"Buenas! soy {nombre} y tengo {edad} años"}

@app.post("/esqueleto")
def esqueleto(image_file: UploadFile = File(...)):
    predictor = SelfiePredictor()
    output = predictor.predict_skeleton(image_file.file)
    res, img_png = cv2.imencode(".png", output)
    return StreamingResponse(io.BytesIO(img_png.tobytes()), media_type="image/png")
