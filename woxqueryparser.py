from scanners import ParamScanners
import result

keywords = {
    "np": result.CreateProjectResult,
    "new project": result.CreateProjectResult
}


class WoxQueryParser(object):
    @staticmethod
    def parse(query):
        word_arr = query.split()
        if word_arr[0] in keywords.keys():
            result = keywords[word_arr[0]]