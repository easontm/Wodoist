import os.path

token_location = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '.todoist_token'
)

if os.path.exists(token_location):
    with open(token_location) as f:
        token = f.readline().strip()
