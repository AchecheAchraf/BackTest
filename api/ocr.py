from flask import Blueprint, request, jsonify
from PIL import Image
import pytesseract

ocr_route = Blueprint('ocr', __name__)

pytesseract.pytesseract.tesseract_cmd = r'./tesseract/tesseract.exe'

@ocr_route.route('/api/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    image_file = request.files['image']
    try:
        image = Image.open(image_file)
        text = pytesseract.image_to_string(image)
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
