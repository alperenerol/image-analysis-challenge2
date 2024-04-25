# Flask Image Analysis App - Challenge 2

## Description
This project is a Flask-based application designed to analyse images.

## Installation
Clone the repository and build the Docker image:

git clone https://github.com/alperenerol/image-analysis-challenge2

cd image-analysis-challenge2

docker build -t flask-img .      

## Running the Application
Run the Docker container using:
docker run -p 5002:5002 flask-img

## Usage
Submit depth_min, depth_max processing:

curl "http://localhost:5002/get_images?depth_min=9300.1&depth_max=9301.0"

Outputs: base64 string for generated frame, saves image to disk

# Utils functions for encoding and decoding
pil_image_to_b64_str
base64_to_pilimage

# Example Generated Frame Display
python test.py 