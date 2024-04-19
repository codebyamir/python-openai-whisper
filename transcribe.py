import whisper

model = whisper.load_model("large")

def transcribe(audio_path):
    result = model.transcribe(audio_path)
    return result['text']

print(transcribe("1462-170142-0000.flac"))