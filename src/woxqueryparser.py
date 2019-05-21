from .scanners import ParamScanners
from . import result

keywords = {
    "np": result.CreateProjectResult,
    "new project": result.CreateProjectResult
}


class WoxQueryParser(object):
    @staticmethod
    def parse(query):
        results = []
        word_arr = query.split()
        if word_arr[0] in keywords.keys():
            results.append(keywords[word_arr[0]](query))
        return results
