import logging
from flask import Blueprint, request, jsonify
import pytesseract
from PIL import Image
import io

ocr_route = Blueprint('ocr_route', __name__)

pytesseract.pytesseract.tesseract_cmd = r'../tesseract/tesseract.exe'

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@ocr_route.route('/api/ocr', methods=['POST'])
def ocr_image():
    try:
        if 'image' not in request.files:
            logging.error("No image file found in the request.")
            return jsonify({'error': 'No image file found in the request.'}), 400

        image_file = request.files['image']

        if image_file.filename == '':
            logging.error("No image file selected.")
            return jsonify({'error': 'No image file selected.'}), 400

        # Read the image file
        image = Image.open(io.BytesIO(image_file.read()))

        # Perform OCR on the image
        text = pytesseract.image_to_string(image)

        logging.info("OCR extraction successful.")
        return jsonify({'text': text}), 200

    except Exception as e:
        logging.error(f"Error processing image for OCR: {str(e)}")
        return jsonify({'error': 'Error processing image for OCR', 'message': str(e)}), 500
