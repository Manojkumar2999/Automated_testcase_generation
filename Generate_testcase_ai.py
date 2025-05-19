import openai

def generate_test_case(summary, description, openai_api_key):
    prompt = f"""
Convert the following JIRA user story into a structured TestLink test case:
Summary: {summary}
Description: {description}

Use this format:
- Test Case Title:
- Summary:
- Preconditions:
- Test Steps:
- Expected Results:
"""
    openai.api_key = openai_api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
