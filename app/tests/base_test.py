"""
    Base Abstract test object
"""
import abc


class BaseTest(abc.ABC):
    """
    BaseTest Python module is an abstract class for every test case
    have the same struchture of object
    """

    @abc.abstractclassmethod
    def set_up(cls):
        """Default setUp for every switch test

        Returns:
            Any : NotImplemented
        """
        return NotImplemented

    @abc.abstractclassmethod
    def __init__(cls) -> None:
        super().__init__()
