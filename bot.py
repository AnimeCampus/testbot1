import requests
import os

# Replace 'YOUR_API_KEY' with your actual API key
api_key = '40b06e5a0ad7f9474d9dff9e378a9759c1ae96ac'

# URL for the SauceNAO API
url = 'https://saucenao.com/search.php'

# URL of the image you want to search
image_url = 'https://telegra.ph/file/e2faf7495d6faaa703933.jpg'

# Download the image and save it as a local file
response = requests.get(image_url)

if response.status_code == 200:
    with open('local_image.jpg', 'wb') as image_file:
        image_file.write(response.content)
else:
    print(f"Failed to download the image: {response.status_code}")

# Define the parameters for the search
params = {
    'output_type': 2,  # JSON output
    'api_key': api_key,
}

# Open and read the local image file
with open('local_image.jpg', 'rb') as image_file:
    files = {'file': image_file}

# Make a POST request to the SauceNAO API
response = requests.post(url, data=params, files=files)

# Process the response
if response.status_code == 200:
    data = response.json()
    # Handle the data as needed
else:
    print(f"Error: {response.status_code}")
    print(response.text)

# Clean up: Delete the local image file
os.remove('local_image.jpg')
