import wave
from io import BytesIO
# import pyaudio
from httplib2 import Response
import ffmpeg
import numpy as np
from stt import Model
import queue


def normalize_audio(audio):
    out, err = (
        ffmpeg.input("pipe:0")
        .output(
            "pipe:1",
            f="WAV",
            acodec="pcm_s16le",
            ac=1,
            ar="16k",
            loglevel="error",
            hide_banner=None,
        )
        .run(input=audio, capture_stdout=True, capture_stderr=True)
    )
    if err:
        raise Exception(err)
    return out


class SpeechToTextEngine:
    ''' Class to perform speech-to-text transcription'''
    
    # FORMAT = pyaudio.paInt16
    SAMPLE_RATE = 16000
    CHANNELS = 1
    BLOCKS_PER_SECOND = 50
    
    def __init__(self, model_path, scorer_path):
        self.model = Model(model_path)
        self.model.enableExternalScorer(scorer_path)
        self.sample_rate = self.SAMPLE_RATE
        self.buffer_queue = queue.Queue()

    def run(self, audio):
        audio = normalize_audio(audio)
        audio = BytesIO(audio)
        with wave.Wave_read(audio) as wav:
            audio = np.frombuffer(wav.readframes(wav.getnframes()), np.int16)
        result = self.model.stt(audio)
        return result


class Response:
    def __init__(self, text, time):
        self.text = text
        self.time = time


class Error:
    def __init__(self, message):
        self.message = message
