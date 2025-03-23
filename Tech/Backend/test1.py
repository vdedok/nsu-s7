import os

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchaudio
from transformers import AutoConfig, AutoModel, Wav2Vec2FeatureExtractor

import librosa
import numpy as np
from pydub import AudioSegment

def speech_file_to_array_fn(path, sampling_rate):
    speech_array, _sampling_rate = torchaudio.load(path)
    resampler = torchaudio.transforms.Resample(_sampling_rate)
    speech = resampler(speech_array).squeeze().numpy()
    return speech


def predict(path, sampling_rate):
    speech = speech_file_to_array_fn(path, sampling_rate)
    inputs = feature_extractor(speech, sampling_rate=sampling_rate, return_tensors="pt", padding=True)
    inputs = {key: inputs[key].to(device) for key in inputs}

    with torch.no_grad():
        logits = model_(**inputs).logits

    scores = F.softmax(logits, dim=1).detach().cpu().numpy()[0]
    outputs = [{"Emotion": config.id2label[i], "Score": f"{round(score * 100, 3):.1f}%"} for i, score in enumerate(scores)]
    return outputs


TRUST = True
config = AutoConfig.from_pretrained('Aniemore/wav2vec2-xlsr-53-russian-emotion-recognition', trust_remote_code=TRUST)
model_ = AutoModel.from_pretrained("Aniemore/wav2vec2-xlsr-53-russian-emotion-recognition", trust_remote_code=TRUST)
feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained("Aniemore/wav2vec2-xlsr-53-russian-emotion-recognition")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_.to(device)


def process_speech(wav_file_name, fragment_duration = 20):
    
    result = []

    newAudio = AudioSegment.from_wav(wav_file_name)
    duration = newAudio.duration_seconds // fragment_duration
    i = 0

    while i <= duration:
        t1 = i * fragment_duration * 1000
        t2 = (i+1) * fragment_duration * 1000
        i += 1
        fragment = newAudio[t1:t2]
        fragment.export(f'{i}.wav', format="wav")
        predicted = predict(f'{i}.wav', 16000)
        for elem in predicted:
            elem['Score'] = elem['Score'][:-1]
        result.append(predicted)
        os.remove(f'{i}.wav')

    return result

if __name__ == '__main__':
    print(process_speech("4_mp3.wav"))
