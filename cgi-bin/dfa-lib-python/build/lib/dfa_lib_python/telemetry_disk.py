from .ProvenanceObject import ProvenanceObject
from .method_type import MethodType


class TelemetryDisk(ProvenanceObject):
    """
    This class defines a task performance.

    Attributes:
        - consumption_date
        - consumption_time
        - consumption_value
    """

    def __init__(self, consumption_timestamp="", sdiskio_read_bytes="", sdiskio_write_bytes="", sdiskio_busy_time="", sswap_total="", sswap_used=""):
        ProvenanceObject.__init__(self, "")
        self._consumptionTimestamp = consumption_timestamp
        self._sdiskioReadBytes = sdiskio_read_bytes
        self._sdiskioWriteBytes = sdiskio_write_bytes
        self._sdiskioBusyTime = sdiskio_busy_time
        self._sswapTotal = sswap_total
        self._sswapUsed = sswap_used

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
    def sdiskioReadBytes(self):
        """Get or set the consumption value."""
        return self._sdiskioReadBytes

    @sdiskioReadBytes.setter
    def sdiskioReadBytes(self, sdiskio_read_bytes):
        assert isinstance(sdiskio_read_bytes, str), \
            "The consumption value must be a string."
        self._sdiskioReadBytes = sdiskio_read_bytes        

    @property
    def sdiskioWriteBytes(self):
        """Get or set the consumption value."""
        return self._sdiskioWriteBytes

    @sdiskioWriteBytes.setter
    def sdiskioWriteBytes(self, sdiskio_write_bytes):
        assert isinstance(sdiskio_write_bytes, str), \
            "The consumption value must be a string."
        self._sdiskioWriteBytes = sdiskio_write_bytes          

    @property
    def sdiskioBusyTime(self):
        """Get or set the consumption value."""
        return self._sdiskioBusyTime

    @sdiskioBusyTime.setter
    def sdiskioBusyTime(self, sdiskio_busy_time):
        assert isinstance(sdiskio_busy_time, str), \
            "The consumption value must be a string."
        self._sdiskioBusyTime = sdiskio_busy_time          

    @property
    def sswapTotal(self):
        """Get or set the consumption value."""
        return self._sswapTotal

    @sswapTotal.setter
    def sswapTotal(self, sswap_total):
        assert isinstance(sswap_total, str), \
            "The consumption value must be a string."
        self._sswapTotal = sswap_total     

    @property
    def sswapUsed(self):
        """Get or set the consumption value."""
        return self._sswapUsed

    @sswapUsed.setter
    def sswapUsed(self, sswap_used):
        assert isinstance(sswap_used, str), \
            "The consumption value must be a string."
        self._sswapUsed = sswap_used         
                 