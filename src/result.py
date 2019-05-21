from abc import ABC, abstractmethod
from .scanners import ParamScanners as ps


class Result(ABC):
    json_template = {
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
        # TODO: maybe this shouldn't use get_project, because then
        #  to make a project "test project" you'd need to type "np #'test project'"
        #  There's no reason for someone invoking 'np' to type anything other than the name
        self.name = ps.get_project(query)

    def get_payload(self):
        pass

    def gen_json(self):
        self.json_template["SubTitle"] = 'action_descr'
        self.json_template["JsonRPCAction"] = {
            "method": "submit_todoist",
            "parameters": ['action_params'],
            "dontHideAfterAction": False
        }
        return self.json_template
