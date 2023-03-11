import json
from os.path import exists, abspath
from os import getcwd, mkdir
from note import note

class note_manager:
    _serialize_path = ""
    _notes = []
    _next_id: int = 0

    def __init__(self, serialize_path):
        self._serialize_path = serialize_path
        self.load_notes()
    def get_info(self):
        result = ""
        if not self.is_empty():
            for note in self.get_notes():
                result += note.get_info()
        if len(result) == 0:
            result = "Здесь пока нет записей"
        return result 
    def is_empty(self):
        if len(self.get_notes()) == 0:
            return True
        else:
            return False
    
    def _current_max_id(self):
        max_id = 0
        for note in self.get_notes():
            if note.get_id() > max_id:
                max_id = note.get_id()
        return max_id

    def get_notes(self):
        return self._notes
    def get_serialize_path(self):
        return self._serialize_path
    
    def set_serialize_path(self, path):
        self._serialize_path = path
        
    def load_notes(self):
        if exists(self._serialize_path):
            with open(self._serialize_path, 'r') as f:
                self.import_notes(json.load(f))
    def save_notes(self):
        if not exists(self._serialize_path):
            mkdir("data")
        with open(self._serialize_path, 'w+') as f:
            res = []
            for note in self.get_notes():
                res.append(note.to_dict())
            f.write(json.dumps(res))

    def _import_note(self, n_id: int,
                        title: str,
                        body: str,
                        created: str,
                        modified: str):
        if self.check_note_data(title, body, id=n_id):
            self.get_notes().append(
                note(n_id, title, body, created, modified))
            self._next_id = n_id + 1

    def import_notes(self, notes):
        self._notes = []
        self._next_id = 0
        for note in notes:
            self._import_note(
                note["id"], note["title"], note["body"], note["created"], note["modified"])

    def add_note(self, title: str,
                    body: str):
        if self.check_note_data(title, body, self._next_id):
            self.get_notes().append(
                note(self._next_id, title, body))
            self._next_id += 1
            return True
        return False   

    def modify_note(self, id, title = None, body = None):
        for note in self.get_notes():
            if note.get_id() ==  id:
                note.modify(title, body)
    
    def delete_note(self, id: int):
        if self.check_text(id):
            flag = False
            for note in self._notes:
                if note.get_id() == id:
                    self.get_notes().remove(note)
                    flag = True
            for note in self._notes[id:]:
                note.id -= 1
            if not self.is_empty():
                self._next_id = self._current_max_id() + 1
            else:
                self._next_id = 0
            return flag
        return False
    
    def check_text(self, input):
        if (input != None) and (input != ""):
            return True
        return False

    def check_note_data(self, title, body, id=0):
        if self.check_text(title) and self.check_text(body) and id >= 0:
            return True
        return False