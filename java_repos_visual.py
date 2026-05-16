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

#response in dictionary 
response_dict = response.json()
repo_dicts = response_dict['items']

print(f"Repositories returned: {len(response_dict)}")

repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']

    repo_link = f"<a href = '{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']

    hover_text = f"{owner}<br>{description}"
    hover_texts.append(hover_text)

    title = "Most Starred Java Repos on GitHub"

labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x = repo_links, y = stars, hover_name = hover_texts,title = title, labels = labels)

#save file
fig.write_html("java_repos.html")
fig.show()