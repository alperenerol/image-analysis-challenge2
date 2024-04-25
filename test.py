import requests
from utils import base64_to_pilimage

# Define the URL of the Flask API
url = "http://localhost:5002/get_images"
# Specify the query parameters
params = {
    'depth_min': 9200.1,
    'depth_max': 9220.0
}
# Send a GET request
response = requests.get(url, params=params)
# Check if the request was successful
if response.status_code == 200:
    print("Success:")
    print(response.json())  # Print the JSON response from the server
else:
    print("Failed to retrieve data:")
    print("Status code:", response.status_code)

img_output = base64_to_pilimage(response.json())
# Display the image
img_output.show()