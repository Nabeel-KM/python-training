import requests

response = requests.get("https://api.github.com/users/Nabeel-KM/repos")

my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}, Project URL: {project['html_url']}")
