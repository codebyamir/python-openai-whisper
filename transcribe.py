import whisper
import sys

def transcribe(audio_path):
    result = model.transcribe(audio_path)
    return result['text']

# Check if an audio filename was provided
if len(sys.argv) < 2:
    print("Usage: python transcribe.py <audio_file>")
    sys.exit(1)

model = whisper.load_model("large")

# Get the audio filename from the command line
audio_file = sys.argv[1]

print(transcribe(audio_file))
