class AddInfo:

    def __init__(self):
        self.id = None
        self.data = None

    def add_query_id(self, id):
        self.id = id

    def add_addinfo(self, form_data):
        self.data = form_data

    def clear(self):
        self.id = None
        self.data = None