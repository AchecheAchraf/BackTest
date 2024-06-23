from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__)

# Read CORS origins from environment variable
cors_allowed_origins = os.getenv('CORS_ALLOWED_ORIGINS', 'http://localhost:3000').split(',')

CORS(app, resources={r"/api/*": {"origins": cors_allowed_origins}})

# Register your blueprints
from ocr import ocr_route
from text_to_speech import tts_route

app.register_blueprint(ocr_route)
app.register_blueprint(tts_route)

if __name__ == '__main__':
    app.run(debug=True)
