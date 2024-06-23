from flask import Blueprint, request, jsonify, send_file
from gtts import gTTS
from io import BytesIO
from langdetect import detect

tts_route = Blueprint('text_to_speech', __name__)

@tts_route.route('/api/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']

    try:
        lang = detect(text)  # Detect language of the text
        tts = gTTS(text, lang=lang)
        audio = BytesIO()
        tts.write_to_fp(audio)
        audio.seek(0)  # Move to the beginning of the audio data

        return send_file(audio, as_attachment=True, download_name='speech.mp3', mimetype='audio/mpeg')
    except Exception as e:
        return jsonify({'error': str(e)}), 500
