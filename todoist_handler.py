import os.path
from todoist.api import TodoistAPI

token_location = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '.todoist_token'
)

if os.path.exists(token_location):
    with open(token_location) as f:
        token = f.readline().strip()


class TodoistHandler(object):
    @staticmethod
    def get_api():
        """
        Syncs the API call instance if it exists, otherwise creates one
        :return:
        API instance
        """
        api_conn = TodoistAPI(token)
        api_conn.sync()
        return api_conn

    @staticmethod
    def submit_todoist(action):
        api = get_api()
        project1 = api.projects.add(action)
        api.commit()
        # task1 = api.items.add('Task1', project_id=project1['id'])