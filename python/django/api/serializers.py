from json import JSONEncoder


class TodoSerializer(JSONEncoder):
    def default(self, o):
        return o.__dict__
