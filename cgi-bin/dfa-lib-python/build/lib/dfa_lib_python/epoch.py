from .ProvenanceObject import ProvenanceObject


class Epoch(ProvenanceObject):
    """
    This class defines a task performance.

    Attributes:
        - value (:obj: str):
        - elaspsed_time (:obj:`str`): time that the epoch has lasted
    """
    def __init__(self, value="", elapsed_time="", loss="", acc=""):
        ProvenanceObject.__init__(self, "")
        self._value = value
        self._elapsedTime = elapsed_time
        self._loss = loss
        self._acc = acc

    @property
    def elapsedTime(self):
        """Get or set the elapsed time."""
        return self._elapsedTime

    @elapsedTime.setter
    def elapsedTime(self, elapsed_time):
        assert isinstance(elapsed_time, float), \
            "The start time must be a float."
        self._elapsedTime = elapsed_time

    @property
    def value(self):
        """Get or set the value."""
        return self._value

    @value.setter
    def value(self, value):
        assert isinstance(value, int), \
            "The end time must be a integer."
        self._value = value

    @property
    def loss(self):
        """Get or set the loss."""
        return self._loss

    @loss.setter
    def loss(self, loss):
        assert isinstance(loss, float), \
            "The performance method must be a float."
        self._loss = loss

    @property
    def acc(self):
        """Get or set the accuracy."""
        return self._acc

    @acc.setter
    def acc(self, acc):
        assert isinstance(acc, float), \
            "The performance description must be a floar."
        self._acc = acc
