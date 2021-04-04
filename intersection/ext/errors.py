# This is a file where all the custom made errors are stored

class Error(Exception):
    """This is the base class for all the exceptions used across the project"""
    pass

class mapNotInTrendingError(Error):
    """An error raised when a map is not in trending but the trending_position() function was ran"""

    def __str__(self):
        return "This map is not in trending and therfore cannot be accessed!"

class mapNotFoundError(Error):
    """An error raised when there's no maps in the requested source. Usually raised when an user has no maps"""

    def __str__(self):
        return "The requested map does not exist!"

class userNotFoundError(Error):
    """An error raised when no users matching the given criteria were found"""

    def __str__(self):
        return "The requested user does not exist!"