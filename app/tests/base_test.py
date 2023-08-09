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
    # pylint: disable=C0103
    def setUp(cls):
        # pylint: enable=C0103
        """Default setUp for every switch test

        Returns:
            Any : NotImplemented
        """
        return NotImplemented
