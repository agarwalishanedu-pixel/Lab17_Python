"""
Program Name: Lab 17
Name: Ishan Agarwal
Purpose: To deepen my understanding of API's
Starter code: NA
Date: May 15, 2026
"""

import requests
import plotly.express as px

#API Call url
url = "https://api.github.com/search/repositories"
url += "?q=language:java+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)

print(f'Status Code: {response.status_code}')