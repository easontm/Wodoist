# from .scanners import ParamScanners
from . import result

keywords = {
    "np": result.CreateProjectResult,
    "new project": result.CreateProjectResult,
    "create project": result.CreateProjectResult,
}


class WoxQueryParser(object):
    @staticmethod
    def parse(query):
        results = []
        for key in keywords.keys():
            if query.lower().find(key) == 0:
                results.append(keywords[key](query[len(key):]))
            else:
                # TODO generate tasks based on input
                word_arr = query.split()
                continue
        return results
