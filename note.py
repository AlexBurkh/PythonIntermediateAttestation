from datetime import datetime

class note:
    _id = None
    _title = None
    _body = None
    _created = None
    _modified = None

    def __init__(self, id, title, body, created = None, modified = None):
        self._id = id
        self._title = title
        self._body = body
        if created is not None:
            self._created = created
        else:
            self._created = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        if modified is not None:
            self._modified = modified
        else:
            self._modified = self._created
    

    
    def get_info(self):
        return f"id: {self.get_id()} title: {self.get_title()} body: {self.get_body()} created: {self.get_created()} modified: {self.get_modified()}\n"

    def get_id(self):
        return self._id
    def get_title(self):
        return self._title
    def get_body(self):
        return self._body
    def get_created(self):
        return self._created
    def get_modified(self):
        return self._modified
    
    def set_title(self, title):
        self._title = title
    def set_body(self, body):
        self._body = body

    def to_dict(self):
        return {"id":self.get_id(), "title":self.get_title(), "body":self.get_body(), "created":self.get_created(), "modified":self.get_modified()}

    def modify(self, title = None, body = None):
        if title != None:
            self._title = title
        if body != None:
            self._body = body
        self._modified = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")