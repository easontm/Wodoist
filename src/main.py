# -*- coding: utf-8 -*-

# from src.wox import Wox
# from scanners import ParamScanners
from .woxqueryparser import WoxQueryParser as wqp
from .todoist_handler import TodoistHandler as th


class Wodoist(Wox):

    def query(self, query):
        parse_results = wqp.parse(query)
        results = [r.json for r in parse_results]

        results.append({
            "Title": "Todoist",
            "SubTitle": "Query: {}".format(query),
            "IcoPath":"Images/app.ico",
            "JsonRPCAction":{
                "method": "submit_todoist",
                "parameters":[query],
                "dontHideAfterAction": False
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


if __name__ == "__main__":
    Wodoist()
