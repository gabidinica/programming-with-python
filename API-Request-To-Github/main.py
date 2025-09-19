import requests

response = requests.get('https://api.github.com/users/gabidinica/repos')
my_repos = response.json()

for repo in my_repos:
    print(f"Repo name: {repo['name']} \n  Project URL: {repo['html_url']}")


