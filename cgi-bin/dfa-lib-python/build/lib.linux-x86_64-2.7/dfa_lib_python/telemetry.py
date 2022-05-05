from .ProvenanceObject import ProvenanceObject
from .method_type import MethodType


class Telemetry(ProvenanceObject):
    """
    This class defines a task performance.

    Attributes:
        - start_time (:obj:`str`): time when the task has started
        - end_time (:obj:`str`): time when the task has ended
        - method (:obj:`MethodType`, optional): method use to measure
        - description (:obj:`str`, optional): description of the performance measure
    """

    def __init__(self, captured_timestamp="", captured_interval="", epoch_id=""):
        ProvenanceObject.__init__(self, "")
        self._capturedTimestamp = captured_timestamp
        self._capturedInterval = captured_interval
        self._epochID = epoch_id

    @property
    def capturedTimestamp(self):
        """Get or set the captured time."""
        return self._capturedTimestamp

    @capturedTimestamp.setter
    def capturedTimestamp(self, captured_timestamp):
        assert isinstance(captured_timestamp, str), \
            "The captured time must be a string."
        self._capturedTimestamp = captured_timestamp

    @property
    def capturedInterval(self):
        """Get or set the captured interval."""
        return self._capturedInterval

    @capturedInterval.setter
    def capturedInterval(self, captured_interval):
        assert isinstance(captured_interval, str), \
            "The captured interval must be a string."
        self._capturedInterval = captured_interval       

    @property
    def epochID(self):
        """Get or set the captured interval."""
        return self._epochID

    @epochID.setter
    def epochID(self, epoch_id):
        assert isinstance(epoch_id, str), \
            "The epoch must be a string."
        self._epochID = epoch_id          