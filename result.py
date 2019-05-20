from abc import ABC, abstractmethod


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

    def __init__(self, name):
        self.name = name
        super().__init__()

    @abstractmethod
    def gen_json(self):
        pass


class CreateProjectResult(Result):
    def gen_json(self):
        self.json_template["SubTitle"] = 'action_descr'
        self.json_template["JsonRPCAction"] = {
            "method": "submit_todoist",
            "parameters": ['action_params'],
            "dontHideAfterAction": False
        }
        return self.json_template
