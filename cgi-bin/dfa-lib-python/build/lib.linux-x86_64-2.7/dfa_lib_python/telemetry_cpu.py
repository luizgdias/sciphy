from .ProvenanceObject import ProvenanceObject
from .method_type import MethodType


class TelemetryCPU(ProvenanceObject):
    """
    This class defines a task performance.

    Attributes:
        - consumption_date
        - consumption_time
        - consumption_value
    """

    def __init__(self, consumption_timestamp="", scputimes_user="", scputimes_system="", scputimes_idle="", scputimes_steal=""):
        ProvenanceObject.__init__(self, "")
        self._consumptionTimestamp = consumption_timestamp
        self._scputimesUser = scputimes_user
        self._scputimesSystem = scputimes_system
        self._scputimesIdle = scputimes_idle
        self._scputimesSteal = scputimes_steal

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
    def scputimesUser(self):
        """Get or set the consumption value."""
        return self._scputimesUser

    @scputimesUser.setter
    def scputimesUser(self, scputimes_user):
        assert isinstance(scputimes_user, str), \
            "The consumption value must be a string."
        self._scputimesUser = scputimes_user        

    @property
    def scputimesSystem(self):
        """Get or set the consumption value."""
        return self._scputimesSystem

    @scputimesSystem.setter
    def scputimesSystem(self, scputimes_system):
        assert isinstance(scputimes_system, str), \
            "The consumption value must be a string."
        self._scputimesSystem = scputimes_system        

    @property
    def scputimesIdle(self):
        """Get or set the consumption value."""
        return self._scputimesIdle

    @scputimesIdle.setter
    def scputimesIdle(self, scputimes_idle):
        assert isinstance(scputimes_idle, str), \
            "The consumption value must be a string."
        self._scputimesIdle = scputimes_idle               

    @property
    def scputimesSteal(self):
        """Get or set the consumption value."""
        return self._scputimesSteal

    @scputimesSteal.setter
    def scputimesSteal(self, scputimes_steal):
        assert isinstance(scputimes_steal, str), \
            "The consumption value must be a string."
        self._scputimesSteal = scputimes_steal 