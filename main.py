import json
from Jira import get_jira_story

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def main():
    # Load config
    # config = load_json("config/config.json")["Jira_config"]
    # details = load_json("Resources/Details.json")["jira_resource"]

    # jira_url = details["url"]  # Base URL for API, not browse URL
    # issue_key = details["ticket_id"]
    # email = config["user_email"]
    # api_key = config["API_token"]

    # jira_url =  "https://rently.atlassian.net" 
    # issue_key = "GEMS-2270"
    # email = "manojkumar.s@rently.com"
    # api_key = "ATATT3xFfGF0_F1G0BqnbK1woC3dDUJVig9tRXjhBYFqz3-OiwdgTm9puhSiYSsg4N9c-y66e2S94BD7cjAt6tLyvn3jNop-62vGExgkcPvhGw1K2BHtTTNiQ5C_cxvejV3suFvpOx63n1SWjGpKEd0Ml-0zz9FBAKxUpVRC5Iy6yvGL-U9vRQE=E364F9D8"  
    # summary, description = get_jira_story(issue_key, jira_url, email, api_key)
    print("Summary:", summary)
    print("Description:", description)

if __name__ == "__main__":
    main()