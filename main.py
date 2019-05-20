# -*- coding: utf-8 -*-

from wox import Wox, WoxAPI
from todoist_handler import token, TodoistHandler
from scanners import ParamScanners
from woxqueryparser import WoxQueryParser as wqp

class Wodoist(Wox):

    def query(self, query):
        parse_results = ParamScanners.parse_input(query)
        results = [r.gen_json() for r in parse_results]
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
