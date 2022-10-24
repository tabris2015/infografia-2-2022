FROM python:3.10-slim

ENV PORT=8000
RUN apt update
RUN apt install ffmpeg libsm6 libxext6 -y
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY ./ /app
WORKDIR app
CMD uvicorn selfie_server:app --host 0.0.0.0 --port $PORT

