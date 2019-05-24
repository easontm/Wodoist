from abc import ABC, abstractmethod
from .scanners import ParamScanners as ps
import json


class Result(ABC):
    json_base = {
        "Title": "Todoist",
        "SubTitle": "Todoist",
        "IcoPath": "Images/app.ico",
        "JsonRPCAction": {
            "method": "submit_wrapper",
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

        title_str = 'Create project "%s"' % self.name
        action_params = {
            'func': 'create_project',
            'name': self.name
        }
        if self.parent_project:
            title_str += ' under project #%s' % self.parent_project
            action_params['parent'] = self.parent_project

        self.json = self.json_base
        self.json["Title"] = title_str
        self.json["JsonRPCAction"]["parameters"] = [json.dumps(action_params)]
