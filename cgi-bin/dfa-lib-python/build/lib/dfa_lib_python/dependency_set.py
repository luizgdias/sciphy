from .ProvenanceObject import ProvenanceObject
from .set_type import SetType

class DependencySet(ProvenanceObject):
    """
    This class represents a dependency of a task.
    
    Attributes:
        - tags (list): Tags of the dependent tasks.
        - ids (list): Ids of the dependent tasks.
    """

    def __init__(self, dependency="", tag="", type="", dep_bool=False):
        ProvenanceObject.__init__(self, "")
        self.dependency = dependency
        self.tag = tag
        self.type = type

    @property
    def dependency(self):
        """Get or set the dependency tags."""
        return self._dependency

    @dependency.setter
    def dependency(self, dependency):
        assert isinstance(dependency, str), \
            "The tags must be a string."
        self._dependency = dependency

    @property
    def tag(self):
        """Get or set the dependency tags."""
        return self._tag

    @tag.setter
    def tag(self, tag):
        assert isinstance(tag, str), \
            "The tags must be a string."
        self._tag = tag        

    @property
    def type(self):
        """Get or set the dependency ids."""
        return self._type

    @type.setter
    def type(self, type):
        assert isinstance(type, str), \
            "The type must be a str."
        self._type = type