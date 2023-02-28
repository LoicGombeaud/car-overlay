import ffmpeg
import os
import tempfile
from fastapi import BackgroundTasks, FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from ffprobe import FFProbe

app = FastAPI()

origins = ['*'] #TODO restrict!
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

def cleanup(files: [str]):
    for file in files:
        if os.path.exists(file):
            os.remove(file)

@app.post('/upload')
async def upload(file: UploadFile, background_tasks: BackgroundTasks):
    (_, tmp_input) = tempfile.mkstemp()
    (_, tmp_output) = tempfile.mkstemp(suffix='.mp4')

    with open(tmp_input, 'wb') as f:
        f.write(await file.read())

    metadata = FFProbe(tmp_input)
    (width, height) = metadata.streams[0].frame_size()

    overlay_file = ffmpeg.input('overlay.png')
    in_file = ffmpeg.input(tmp_input)
    (
        in_file
        .overlay(
            ffmpeg.input('overlay.png')
                  .filter('scale', width, height)
        )
        .output(in_file.audio, tmp_output)
        .overwrite_output()
        .run()
    )

    background_tasks.add_task(cleanup, [tmp_input, tmp_output])

    return FileResponse(path=tmp_output,
                        media_type='application/octet-stream')
