# from .scanners import ParamScanners
from .result import CreateProjectResult
import logging

logging.basicConfig(level=logging.DEBUG, filename='wqp.log',  format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('wqp')


keywords = {
    "np": CreateProjectResult,
    "new project": CreateProjectResult,
    "create project": CreateProjectResult,
}


class WoxQueryParser(object):
    @staticmethod
    def parse(query):
        # logger.debug('query: %s' % query)
        results = []
        for key in keywords.keys():
            if query.lower().find(key) == 0:
                # logger.debug('found keyword: %s' % key)
                results.append(keywords[key](query[len(key):]))
            else:
                # TODO generate tasks based on input
                word_arr = query.split()
                continue
        return results
