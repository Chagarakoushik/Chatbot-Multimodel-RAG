import easyocr
import numpy as np
from PIL import Image
import io

# Load once
reader = easyocr.Reader(['en'])

def extract_text_from_image(image_bytes):
    try:
        image = Image.open(io.BytesIO(image_bytes))
        image_np = np.array(image)

        results = reader.readtext(image_np)

        text = " ".join([res[1] for res in results])

        if not text.strip():
            return "No readable text found in image"

        return text

    except Exception as e:
        return f"Error processing image: {str(e)}"