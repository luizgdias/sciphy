from .ProvenanceObject import ProvenanceObject
from .method_type import MethodType


class TelemetryNetwork(ProvenanceObject):
    """
    This class defines a task performance.

    Attributes:
        - consumption_date
        - consumption_time
        - consumption_value
    """

    def __init__(self, consumption_timestamp="", consumption_value=""):
        ProvenanceObject.__init__(self, "")
        self._consumptionTimestamp = consumption_timestamp
        self._consumptionValue = consumption_value

    @property
    def consumptionTimestamp(self):
        """Get or set the consumption time."""
        return self._consumptionTimestamp

    @consumptionTimestamp.setter
    def consumptionTimestamp(self, consumption_timestamp):
        assert isinstance(consumption_time, str), \
            "The consumption time must be a string."
        self._consumptionTimestamp = consumption_timestamp

    @property
    def consumptionValue(self):
        """Get or set the consumption value."""
        return self._consumptionValue

    @consumptionValue.setter
    def consumptionValue(self, consumption_value):
        assert isinstance(consumption_value, str), \
            "The consumption value must be a string."
        self._consumptionValue = consumption_value        