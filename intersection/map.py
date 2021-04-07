import intersection.url
from intersection import user

class Map:
    """A class representing an IC map

    You can use the provided functions to get the ``Map`` object from either their author (It's a function inside the ``User`` class) or their author's ``ID``
    The required __init__ arguments are: ``name, desc, gameModeGroup, fileName, fileExt, author, created, updated, gameVersion, votesUp, votesDown, highScore, highScoreUser, fullyUploaded, mapVersion, targetScore, favorites, deleted, objectId, authorName``

    ``created``, ``updated`` are represented in milliseconds

    ``gameModeGroup`` is an integer

    ``fullyUploaded``, ``deleted`` are boolean values, usually ``fullUploaded = True`` and ``deleted = False``

    Example code
    -----------
    ```py
    import map

    example_map_object = Map("name", "desc", 0, "2452411_1605695684744", "trzmap", 2452411, 0, 0, 1, 0, 0, 0, 1, True, 1, 0, 0, False, 1, "Feeeeddmmmeee")

    print(example_map_object.name)
    ```

    Output
    -----------
    name
    """
    def __init__(self, name, desc, gameModeGroup, fileName, fileExt, author, created, updated, gameVersion, votesUp, votesDown, highScore, highScoreUser, fullyUploaded, mapVersion, targetScore, favorites, deleted, objectId, authorName):
        self.name = name
        self.desc = desc
        self.gameModeGroup = gameModeGroup
        self.fileName = fileName
        self.fileExt = fileExt
        self.author = author
        self.created = created
        self.updated = updated
        self.gameVersion = gameVersion
        self.votesUp = votesUp
        self.votesDown = votesDown
        self.highScore = highScore
        self.highScoreUser = highScoreUser
        self.fullyUploaded = fullyUploaded
        self.mapVersion = mapVersion
        self.targetScore = targetScore
        self.favorites = favorites
        self.deleted = deleted
        self.objectId = objectId
        self.authorName = authorName

    def get_author(self):
        """A function creating a `User` object from the `author`
        """
        return intersection.user.get_user(self.author)

    def get_highscore_user(self):
        """A function returning a User` object from the `highScoreUser`
        
        May raise the `userNotFoundError` error if there's no highScoreUser or if it's not in the traffic controller category.
        """
        return intersection.user.get_user(self.highScoreUser)

    def is_in_trending(self, time, trendsystem):
        """A function used to check if the given ``Map`` object is currently in the trending category

        returns a boolean value
        """

        api = get_top_maps(self.gameModeGroup, time, trendsystem)

        for item in api:
            if vars(self) == vars(item):
                return True

        return False

    def get_trending_position(self, time, trendsystem):
        """A function used to get the position of a given `Map` object in trending. the mapNotInTrendingError error will be raised if it's not in trending.

        returns an integer
        """
        if self.is_in_trending(time, trendsystem):
            api = get_top_maps(self.gameModeGroup, time, trendsystem)
            position = 0

            for item in api:
                if vars(self) == vars(item):
                    return position
                position = position + 1
        else:
            raise intersection.errors.errors.mapNotInTrendingError

def get_maps(user_id, resultsPerPage, page):
    """A function allowing you to create a list of ``Map`` objects.

    For creating a ``Map`` object from the ``User`` object look for: ``user.get_user_maps()``

    Example code
    -----------
    ```py
    import map

    example_map_object_list = map.get_maps(2452411, 1, 0)

    print(example_map_object_list[0].authorName)
    ```

    Output
    -----------
    Feeeeddmmmeee

    Note
    -----------
    Maps are sorted by the upload date. 0 is the newest one.
    """

    maps = []

    api = intersection.url.url.map_user(user_id, resultsPerPage, page)

    for i in range(len(api)):

        temp = Map(
            api[i]["name"],
            api[i]["desc"],
            int(api[i]["gameModeGroup"]),
            api[i]["fileName"],
            api[i]["fileExt"],
            int(api[i]["author"]),
            int(api[i]["created"]),
            int(api[i]["updated"]),
            int(api[i]["gameVersion"]),
            int(api[i]["votesUp"]),
            int(api[i]["votesDown"]),
            int(api[i]["highScore"]),
            int(api[i]["highScoreUser"]),
            bool(api[i]["fullyUploaded"]),
            int(api[i]["mapVersion"]),
            int(api[i]["targetScore"]),
            int(api[i]["favorites"]),
            bool(api[i]["deleted"]),
            int(api[i]["objectId"]),
            api[i]["authorName"]
        )

        maps.append(temp)

    return maps

def get_top_maps(mode, time, trendsystem):
    """A function allowing you to create a list of ``Map`` objects that are currently in one of the "top" categories in the game

    mode is an integer

    time is a string, can be one of the following: "day", "week", "month"

    trendsystem is an integer

    Example code
    -----------
    ```py
    import map

    example_map_object_list = map.get_top_maps(2, "day", 1)

    print(example_map_object_list[0].authorName)
    ```

    Output
    -----------
    Feeeeddmmmeee
    """

    maps = []

    api = intersection.url.url.map_top(mode, time, trendsystem)

    for i in range(len(api)):

        temp = Map(
            api[i]["name"],
            api[i]["desc"],
            int(api[i]["gameModeGroup"]),
            api[i]["fileName"],
            api[i]["fileExt"],
            int(api[i]["author"]),
            int(api[i]["created"]),
            int(api[i]["updated"]),
            int(api[i]["gameVersion"]),
            int(api[i]["votesUp"]),
            int(api[i]["votesDown"]),
            int(api[i]["highScore"]),
            int(api[i]["highScoreUser"]),
            bool(api[i]["fullyUploaded"]),
            int(api[i]["mapVersion"]),
            int(api[i]["targetScore"]),
            int(api[i]["favorites"]),
            bool(api[i]["deleted"]),
            int(api[i]["objectId"]),
            api[i]["authorName"]
        )

        maps.append(temp)

    return maps