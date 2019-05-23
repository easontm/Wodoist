from abc import ABC, abstractmethod
from .scanners import ParamScanners as ps
from .todoist_handler import TodoistHandler


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

    @abstractmethod
    def get_payload(self):
        pass

    @abstractmethod
    def gen_json(self):
        pass


class CreateProjectResult(Result):
    def __init__(self, query):
        super().__init__()
        self.parent_project = ps.get_project(query)
        word_list = query.split()
        if self.parent_project:
            word_list.remove('#' + self.parent_project)
        self.name = ' '.join(word_list)

        subtitle_str = 'Create project "%s"' % self.name
        action_params = [self.name]
        if self.parent_project:
            subtitle_str += ' under project #%s' % self.parent_project
            action_params += [self.parent_project]

        self.json = self.json_base
        self.json["SubTitle"] = subtitle_str
        self.json["JsonRPCAction"] = {
            "method": "create_project",
            "parameters": action_params,
            "dontHideAfterAction": False
        }

    def get_payload(self):
        pass

    def gen_json(self):
        self.json_base["SubTitle"] = 'action_descr'
        self.json_base["JsonRPCAction"] = {
            "method": "submit_todoist",
            "parameters": ['action_params'],
            "dontHideAfterAction": False
        }
        return self.json_base
