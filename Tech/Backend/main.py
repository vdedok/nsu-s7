import os
import aiofiles

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import test1

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://192.168.1.62:9000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    if not file.filename.endswith(".wav"):
        return {"error": "File must be a .wav file"}

    async with aiofiles.open(file.filename, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    print('if file = ', os.path.isfile(file.filename))
    print('size = ', os.path.getsize(file.filename))
    
    os.system("ffmpeg -i recording.wav -y -c:a pcm_s24le output.wav") 
    return test1.process_speech('output.wav', 4)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
