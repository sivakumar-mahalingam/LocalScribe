import os
import json
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment  # <-- Import pydub

# --- CONFIGURATION ---
MODEL_PATH = "model"
if not os.path.exists(MODEL_PATH):
    print(f"Model folder '{MODEL_PATH}' not found. Please download the Vosk model and place it there.")
    print("Download from: https://alphacephei.com/vosk/models")
    exit(1)

# --- FLASK APP INITIALIZATION ---
app = Flask(__name__)
CORS(app)

# --- VOSK MODEL LOADING ---
try:
    model = Model(MODEL_PATH)
    print("Vosk model loaded successfully.")
except Exception as e:
    print(f"Error loading Vosk model: {e}")
    exit(1)


# --- ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio_data' not in request.files:
        return jsonify({'error': 'No audio file found'}), 400

    audio_file = request.files['audio_data']

    try:
        # --- Use pydub to handle audio conversion ---
        # Load the audio file from memory
        sound = AudioSegment.from_file(audio_file)

        # Ensure the audio is mono, has the correct sample rate, and is 16-bit
        sound = sound.set_channels(1)
        sound = sound.set_frame_rate(16000)
        sound = sound.set_sample_width(2)  # <-- CRITICAL FIX: Force 16-bit (2 bytes) samples

        # The recognizer needs raw audio data in bytes
        audio_data = sound.raw_data
        print(f"Successfully processed audio data: {len(audio_data)} bytes")


    except Exception as e:
        # This will catch errors if FFmpeg is not installed or the file is corrupt
        print(f"Error processing audio: {e}")
        return jsonify({'error': f'Could not process audio file: {e}. Is FFmpeg installed?'}), 400

    # Create a KaldiRecognizer with the correct sample rate
    rec = KaldiRecognizer(model, 16000)
    rec.SetWords(True)

    # Process the audio data
    rec.AcceptWaveform(audio_data)

    # Get the final result using FinalResult() for a complete transcription
    result = json.loads(rec.FinalResult())
    text = result.get('text', '')

    print(f"Transcription result: '{text}'")
    return jsonify({'text': text})


# --- MAIN EXECUTION ---
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)


