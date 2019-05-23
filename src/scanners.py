import re


class ParamScanners(object):
    @staticmethod
    def parse_query(query):
        return query.split()

    @staticmethod
    def get_project(query):
        """
         Returns the first project tag it finds. Multi-word projects
         can be identified if they are enclosed in quotes after the #,
         e.g. #"project name"
        :param query: the entire query
        :return: the string representing the project name
        """
        # supports one word projects for now
        query = query.replace("'", '"')
        word_list = re.findall(r'(?:[^\s,"]|"(?:\\.|[^"])*")+', query)
        for i in word_list:
            if i[0] == '#':
                return i[1:].strip("'").strip('"')
        return None

    @staticmethod
    def get_labels(query):
        word_list = query.split()
        labels = [i[1:] for i in word_list if i[0] == '@']
        return labels

    @staticmethod
    def get_due_date(query):
        due_date = ''
        return due_date

    @staticmethod
    # Returns the first valid priority found.
    def get_priority(query):
        p_dict = {
            'p1': 4,
            'p2': 3,
            'p3': 2,
            'p4': 1
        }
        word_list = query.split()
        for i in word_list:
            if i.lower() in p_dict.keys():
                return p_dict[i]
        return p
