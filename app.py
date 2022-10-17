from pyexpat import model
from fastapi import FastAPI, File, UploadFile
from engine import SpeechToTextEngine,Response,Error
import json,shutil
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from time import perf_counter
from pyhocon import ConfigFactory
from sanic import Sanic, response
from sanic.log import logger
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conf = ConfigFactory.parse_file("application.conf")
model = SpeechToTextEngine(
    model_path=Path(conf["stt.model"]).absolute().as_posix(),
    scorer_path=Path(conf["stt.scorer"]).absolute().as_posix(),
    )

@app.route('/')
async def heathcheck():
    return {"Health Check": "Translation api is working"} 
    

@app.post("/stt_api/")
async def create_upload_file(file: UploadFile = File(...)):
    results = {}
    try:
        fname = "audio.wav"
        with open(f'{fname}','wb') as buffer:
            shutil.copyfileobj(file.file,buffer)
        path = Path(fname).absolute().as_posix()
        with open(path,mode="rb") as wavfile:
            audio = wavfile.read()

        inference_start = perf_counter()
        text = model.run(audio)
        inference_end = perf_counter()-inference_start
        results['time'] =inference_end
        results['text'] = text
         
    except Exception as e:
        raise str(e)

    return results
