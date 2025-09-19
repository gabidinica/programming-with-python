# Demo Project: API Request to GitLab

## Technologies Used
- Python
- GitLab
- IntelliJ
- Git

## Project Description
This project involves writing an application that interacts with the GitLab API. The application retrieves and lists all public GitLab repositories for a specified user.

---

## Installing Dependencies
To make external API requests in Python, we will use the `requests` module from PyPI. Install it with:
[Requests](https://pypi.org/project/requests/)
```bash
pip install requests
```

The [GitHub REST API](https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28) allows you to interact programmatically with GitHub's resources. This guide provides an introduction to making API requests using various tools and understanding the components of a request.
This project involves writing an application that interacts with an external API to fetch information:
- Connects to GitLab (or GitHub) API
- Retrieves all public repositories for a specified user
- Lists the repositories in a readable format

## Searching for User Projects
You can use the GitHub search bar and type **"list user projects"** to find relevant results.

### Example Endpoint
```http
GET /users/{username}/projects
```

> Base URL for GitHub API: `https://api.github.com`

In my case I will use: `users/{username}/repos`, because to access the projects is needed a token.  
The output of `print(type(response.text))` is a string.
> To have a list we’re gonna use a json:
`print(response.json())`
