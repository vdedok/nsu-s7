# Import system modules
import os
import soundfile as sf
from transformers import pipeline

pipe = pipeline("audio-classification", model="Aniemore/wav2vec2-xlsr-53-russian-emotion-recognition", trust_remote_code=True)

def decode_file(fname):
    speech, sr = sf.read(fname)
    result = pipe(speech)
    return "RU", result

directories = ["wavs-10-1", "wavs-10-2", "wavs-10-3", "wavs-10-4", "wavs-10-5"]

for directory in directories:
    files = os.listdir(directory)
    files.sort()
    for file in files:
        print("Process file: ", directory + "/" + file)
        lang, emo = decode_file(directory + "/" + file)
        print("Lang: ", lang)
        print("Emo: ", emo)
