import requests
from requests.auth import HTTPBasicAuth

def get_jira_story(issue_key, jira_url, email, api_key):
    url = f"{jira_url}/rest/api/latest/issue/{issue_key}"
    auth = HTTPBasicAuth(email, api_key)
    headers = {
        "Accept": "application/json",
        "User-Agent": "python-requests/2.31.0"
    }
    print(f"Requesting URL: {url}")
    print(f"Headers: {headers}")
    print(f"Auth email: {email}")
    response = requests.get(url, headers=headers, auth=auth)
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print(f"Response: {response.text}")
        raise Exception("Failed to fetch Jira issue.")
    data = response.json()
    if 'fields' not in data:
        print(f"Unexpected response format: {data}")
        raise KeyError("'fields' not found in Jira response.")
    return data['fields'].get('summary', ''), data['fields'].get('description', '')
