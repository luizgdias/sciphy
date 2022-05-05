from .ProvenanceObject import ProvenanceObject
from .method_type import MethodType


class TelemetryMemory(ProvenanceObject):
    """
    This class defines a task performance.

    Attributes:
        - consumption_date
        - consumption_time
        - consumption_value
    """

    def __init__(self, consumption_timestamp="", svmem_total="", svmem_available="", svmem_used=""):
        ProvenanceObject.__init__(self, "")
        self._consumptionTimestamp = consumption_timestamp
        self._svmemTotal = svmem_total
        self._svmemAvailable = svmem_available
        self._svmemUsed= svmem_used
        
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
    def svmemTotal(self):
        """Get or set the consumption value."""
        return self._svmemTotal

    @svmemTotal.setter
    def svmemTotal(self, svmem_total):
        assert isinstance(svmem_total, str), \
            "The consumption value must be a string."
        self._svmemTotal = svmem_total        

    @property
    def svmemAvailable(self):
        """Get or set the consumption value."""
        return self._svmemAvailable

    @svmemAvailable.setter
    def svmemAvailable(self, svmem_available):
        assert isinstance(svmem_available, str), \
            "The consumption value must be a string."
        self._svmemAvailable = svmem_available      

    @property
    def svmemUsed(self):
        """Get or set the consumption value."""
        return self._svmemUsed

    @svmemUsed.setter
    def svmemUsed(self, svmem_used):
        assert isinstance(svmem_used, str), \
            "The consumption value must be a string."
        self._svmemUsed = svmem_used   