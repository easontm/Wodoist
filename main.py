# -*- coding: utf-8 -*-

from wox import Wox, WoxAPI
from todoist.api import TodoistAPI
from todoist_handler import token
from parse import ToxParse

class Wodoist(Wox):

    def query(self, query):
        results = []
        results.append({
            "Title": "Todoist",
            "SubTitle": "Query: {}".format(query),
            "IcoPath":"Images/app.ico",
            "JsonRPCAction":{
                "method": "submit_todoist",
                "parameters":[query],
                "dontHideAfterAction":True
            },
            "ContextData": "ctxData"
        })
        return results

    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath":"Images/app.ico"
        })
        return results

    def submit_todoist(self, input):
        api = TodoistAPI(token)
        api.sync()
        project1 = api.projects.add(input)
        api.commit()
        # task1 = api.items.add('Task1', project_id=project1['id'])

if __name__ == "__main__":
    Wodoist()
