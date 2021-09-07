from intersection.ext import url
from intersection import map

class User:
    """A class representing an IC user.
    """

    def __init__(self, objectId, gameVersion, lastLogin, maps, name, followers):
        self.objectId = objectId
        self.gameVersion = gameVersion
        self.lastLogin = lastLogin
        self.maps = maps
        self.name = name
        self.followers = followers

    def get_user_maps(self, **kwargs):
        """A method user to create a list of `Map` objects with some of the maps the user has created.

        Usage::
        >>> import intersection
        >>> user = intersection.user.get_details_for_user(userId=2452411)
        >>> maps = user.get_user_maps()
        >>> for map in maps: print(map.name)
        """
        maps = map.list_maps_by_user(userId=self.objectId, **kwargs)
        return maps

def search_for_users(**kwargs):
    """A function used to used to create a list of `User` objects matching a given name.

    `result` - Number of results to return on a page.

    `page` - Index of page of results to return, starting at page 0.

    `query` - Text to search for, looks at the username.

    Usage::

    >>> import intersection
    >>> maps = intersection.user.search_for_user(result=5, query="Feeeeddmmmeee")
    >>> for user in users: print(user.name)
    """

    data = url.search_for_users(**kwargs)
    users = []
    for userdata in data:
        users.append(User(
            userdata['objectId'],
            userdata['gameVersion'],
            userdata['lastLogin'],
            userdata['maps'],
            userdata['name'],
            userdata['followers'],
        ))

    return users

def get_details_for_user(**kwargs):
    """A function used to create a `User` object with a given ID.

    `userId` - ID of user to get info about.

    Usage::

    >>> import intersection
    >>> user = intersection.user.get_details_for_user(userId=2452411)
    >>> print(user.name)
    """

    data = url.get_details_for_user(**kwargs)
    user = User(
        data['objectId'],
        data['gameVersion'],
        data['lastLogin'],
        data['maps'],
        data['name'],
        data['followers'],
    )

    return user