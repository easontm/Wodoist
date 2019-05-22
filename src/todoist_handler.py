import os.path
from todoist.api import TodoistAPI
import logging

logger = logging.getLogger(__name__)

'''
def get_api():
  global GLOBAL_API:
  
  ...
  return GLOBAL_API
'''

token_location = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '.todoist_token'
)
logger.info('Token location: %s' % token_location)

if os.path.exists(token_location):
    with open(token_location) as f:
        token = f.readline().strip()
logger.info('Token: %s' % token)


class TodoistHandler(object):

    def __init__(self):
        self.api = None

    def get_api(self):
        """
        Syncs the API call instance if it exists, otherwise creates one
        :return:
        API instance
        """
        if self.api:
            return self.api
        self.api = TodoistAPI(token)
        self.api.sync()
        return self.api

    def submit_todoist(self, action):
        api = self.get_api()
        project1 = api.projects.add(action)
        api.commit()
        # task1 = api.items.add('Task1', project_id=project1['id'])

    def get_project_by_name(self, name, api=None):
        """
        Returns the first found project matching name
        ~~ If there are duplicates it can't tell! ~~
        :param name: str - project name search
        :param api: an api instance
        :return: project object
        """
        if api is None:
            api = self.get_api()
        for p in api.state['projects']:
            if p['name'] == name:
                return p

    def create_project(self, name, parent=None):
        """
        Creates a project and commits the change
        :param name: str name of the project you want to make
        :param parent: optional - str name of the parent project
        :return:
        """
        api = self.get_api()
        parent_id = None
        if parent is not None:
            parent_id = self.get_project_by_name(parent, api)['id']
        api.projects.add(name, parent_id=parent_id)
        api.commit()
