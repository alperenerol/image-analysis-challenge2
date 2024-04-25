from flask import Flask, request, jsonify
import sqlite3
import numpy as np
import uuid
import os
from PIL import Image
from matplotlib import cm
from utils import pil_image_to_b64_str

app = Flask(__name__)

GENERATE_FOLDER = 'generated_images'
app.config['GENERATE_FOLDER'] = GENERATE_FOLDER
os.makedirs(GENERATE_FOLDER, exist_ok=True)

@app.route('/get_images', methods=['GET'])
def get_images():
    depth_min = request.args.get('depth_min', type=float)
    depth_max = request.args.get('depth_max', type=float)
    conn = sqlite3.connect('images.db')
    c = conn.cursor()
    c.execute("SELECT * FROM images WHERE depth BETWEEN ? AND ?", (depth_min, depth_max))
    rows = c.fetchall()
    image_data = np.array([row[1:] for row in rows])
    # Close the connection
    conn.close()

    # Apply a color map
    color_map = cm.inferno  # You can choose any colormap that Matplotlib supports
    colored_image = color_map(image_data / 255)  # Normalize data to 0-1 range
    # Convert the RGBA image to RGB by discarding the Alpha channel
    colored_image_rgb = (colored_image[..., :3] * 255).astype(np.uint8)
    # Convert numpy array to PIL Image (in RGB format)
    image_pil = Image.fromarray(colored_image_rgb)

    # Save the RGB image to a temporary file
    temp_filename = str(uuid.uuid4()) + '.png'
    temp_filepath = os.path.join(app.config['GENERATE_FOLDER'], temp_filename)
    image_pil.save(temp_filepath)
    print(f"Image saved at {temp_filepath}")

    # Convert the image to a base64 string
    img_b64_str = pil_image_to_b64_str(image_pil, 'PNG')

    return jsonify(img_b64_str)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)