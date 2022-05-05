from .ProvenanceObject import ProvenanceObject


class File(ProvenanceObject):
    def __init__(self, name):
        ProvenanceObject.__init__(self, name)
        self._name = name
