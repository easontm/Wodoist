class ToxParse(object):
    @staticmethod
    # Returns the first project tag it finds
    def get_project(input):
        list = input.split()
        for i in list:
            if i[0] == '#':
                return i[1:]

    @staticmethod
    def get_labels(input):
        list = input.split()
        labels = [i[1:] for i in list if i[0] == '@']
        return labels

    @staticmethod
    def get_due_date(input):
        due_date = ''
        return due_date

    @staticmethod
    # Returns the first valid priority found.
    def get_priority(input):
        p_dict = {
            'p1': 4,
            'p2': 3,
            'p3': 2,
            'p4': 1
        }
        list = input.split()
        for i in list:
            if i.lower() in p_dict.keys():
                return p_dict[i]
        return p
