import requests
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()


# Set search parameters
doi = "10.1145/2939672.2939778"


# Set up request
url = f"http://api.elsevier.com/content/search/scopus?query=DOI({doi})"

headers = {
  'X-ELS-APIKey': f"{os.getenv('scopus_api_key')}"
}


# Send request
response = requests.request("GET", url, headers=headers)


# Handle response
print(response.status_code)
print(response.json())