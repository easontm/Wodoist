# -*- coding: utf-8 -*-

from wox import Wox, WoxAPI
from src.woxqueryparser import WoxQueryParser as wqp
from src.todoist_handler import TodoistHandler
import logging
import json

logging.basicConfig(level=logging.DEBUG, filename='wodoist.log',  format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


"""
import sys
import pkgutil
logging.basicConfig(level=logging.DEBUG, filename='wodoist.log',  format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.warning('path: %s' % sys.path)
logger.handlers[0].flush()

search_path = ['.'] # set to None to see all modules importable from sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print(all_modules)
"""


class Wodoist(Wox):

    def query(self, query):
        parse_results = wqp.parse(query)
        results = [r.json for r in parse_results]

        # results.append({
        #     "Title": "Todoist",
        #     "SubTitle": "Query: {}".format(query),
        #     "IcoPath":"Images/app.ico",
        #     "JsonRPCAction": {
        #         "method": "submit_wrapper",
        #         "parameters": [query],
        #         "dontHideAfterAction": False
        #     },
        #     "ContextData": "ctxData"
        # })
        # logger.debug(results)
        return results

    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath":"Images/app.ico"
        })
        return results

    def submit_wrapper(self, params):
        """
        Passes contents of Json parameters to TodoistHandler class
        :param params: should contain a value for 'func' representing the function to execute
               from the TodoistHandler class
        :return: no
        """
        params = json.loads(params)
        handler = TodoistHandler()
        func = getattr(TodoistHandler, params.pop('func'))
        logger.debug('submit now: %s' % params)
        func(handler, **params)


if __name__ == "__main__":
    Wodoist()
