from abc import ABC, abstractmethod
from .scanners import ParamScanners as ps
from .todoist_handler import TodoistHandler as th


class Result(ABC):
    json_base = {
        "Title": "Todoist",
        "SubTitle": "Query: {}",
        "IcoPath": "Images/app.ico",
        "JsonRPCAction": {
            "method": "submit_todoist",
            "parameters": [],
            "dontHideAfterAction": False
        },
        "ContextData": "ctxData"
    }

    def __init__(self):
        super().__init__()


class CreateProjectResult(Result):
    def __init__(self, query):
        super().__init__()
        self.parent_project = ps.get_project(query)
        word_list = query.split()
        if self.parent_project:
            word_list.remove('#' + self.parent_project)
        self.name = ' '.join(word_list)

        subtitle_str = 'Create project "%s"' % self.name
        # action_params = [th.create_project, self.name]
        action_params = {
            'func': th.create_project,
            'name': self.name
        }
        if self.parent_project:
            subtitle_str += ' under project #%s' % self.parent_project
            # action_params += [self.parent_project]
            action_params['parent'] = [self.parent_project]

        self.json = self.json_base
        self.json["SubTitle"] = subtitle_str
        self.json["JsonRPCAction"] = {
            "method": "create_project",
            "parameters": [action_params],
            "dontHideAfterAction": False
        }
