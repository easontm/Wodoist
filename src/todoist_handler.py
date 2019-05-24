import os.path
from todoist.api import TodoistAPI
import logging

logging.basicConfig(level=logging.DEBUG, filename='handler.log',  format='%(name)s - %(levelname)s - %(message)s')
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
# logger.info('Token location: %s' % token_location)

if os.path.exists(token_location):
    with open(token_location) as f:
        token = f.readline().strip()
# logger.info('Token: %s' % token)


class TodoistHandler(object):
    __instance = None

    def __new__(cls):
        if TodoistHandler.__instance is None:
            TodoistHandler.__instance = object.__new__(cls)
        return TodoistHandler.__instance

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

    '''
    @staticmethod
    def submit_todoist(action, *args):
        action(*args)
    '''

    @staticmethod
    def func_dispatcher(**kwargs):
        """
        Receives execution data from the Wodoist click events
        > kwargs['func'] should be a method in this class to execute
        > Rest of the payload should be parameters
        :param kwargs:
        :return:
        """
        # func = kwargs.pop('func')
        # func(**kwargs)

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
            if self.cleaner(p['name']) == self.cleaner(name):
                return p

    def create_project(self, name=None, parent=None, **kwargs):
        """
        Creates a project and commits the change
        :param name: str name of the project you want to make
        :param parent: optional - str name of the parent project
        :return:
        """
        if not name:
            name = kwargs.pop('name')
        if not parent:
            parent = kwargs.pop('parent', None)
        # logger.debug('create project invoked -- name: {0} -- parent: {1}'.format(name, parent))
        api = self.get_api()
        parent_id = None
        if parent is not None:
            parent_id = self.get_project_by_name(parent, api)['id']
        api.projects.add(name, parent_id=parent_id)
        api.commit()

    @staticmethod
    def cleaner(str_in):
        return str_in.lower().replace('-', ' ')
