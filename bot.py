import requests

# Replace 'YOUR_API_KEY' with the actual API key you obtained
api_key = '40b06e5a0ad7f9474d9dff9e378a9759c1ae96ac'

# URL for the SauceNAO API
url = 'https://saucenao.com/search.php'

# Define the parameters for the search
params = {
    'output_type': 2,  # JSON output
    'api_key': api_key,
    'url': 'https://telegra.ph/file/e2faf7495d6faaa703933.jpg',  # Replace with the URL of your image
}

# Make a GET request to the SauceNAO API
response = requests.get(url, params=params)

# Process the response
if response.status_code == 200:
    data = response.json()
    # Handle the data as needed
else:
    print(f"Error: {response.status_code}")
    print(response.text)
  
