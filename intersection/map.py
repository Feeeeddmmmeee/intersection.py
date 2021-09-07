from intersection.ext import url
from intersection import user, comment, highscore

class Map:
    """A class representing an IC map.
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
        """A method used to used to create a `User` object of the map author.

        Usage::

        >>> import intersection
        >>> map = intersection.map.get_map_details(mapId=413915)
        >>> author = map.get_author()
        >>> print(author.name)
        """
        return user.get_details_for_user(userId=self.objectId)

    def get_highscore_user(self):
        """A method used to used to create a `User` object of the person who achieved the highest score on the map.

        Usage::

        >>> import intersection
        >>> map = intersection.map.get_map_details(mapId=413915)
        >>> highscore_user = map.get_highscore_user()
        >>> print(highscore_user.name)
        """
        return user.get_details_for_user(userId=self.highScoreUser)
    
    def is_in_trending(self, **kwargs):
        """A method used to used to get the trending position of a map.

        `time` - alltime / month / week / day

        `maxversion` - The requester's game version, so if you have version 130 of the app you will not get maps that were made using 140 and might not be possible to play. Setting something very high such as 999 will just search for everything. If not added to the request then only maps made before beta will be searched for.

        `result` - Number of results to return on a page.

        `page` - Index of page of results to return, starting at page 0.

        `trendsystem` - 0 or 1, should always be set to 1 as that is the current version used ingame.

        Usage::

        >>> import intersection
        >>> map = intersection.map.get_map_details(mapId=413915)
        >>> is_in_trending = map.is_in_trending(time="alltime", result=5)
        >>> print(is_in_trending)
        """
        data = find_top_maps(**kwargs)

        for mapdata in data:
            if vars(self) == vars(mapdata):
                return True

        return False

    def get_trending_position(self, **kwargs):
        """A method used to used to get the trending position of a map.

        `time` - alltime / month / week / day

        `maxversion` - The requester's game version, so if you have version 130 of the app you will not get maps that were made using 140 and might not be possible to play. Setting something very high such as 999 will just search for everything. If not added to the request then only maps made before beta will be searched for.

        `result` - Number of results to return on a page.

        `page` - Index of page of results to return, starting at page 0.

        `trendsystem` - 0 or 1, should always be set to 1 as that is the current version used ingame.

        Usage::

        >>> import intersection
        >>> map = intersection.map.get_map_details(mapId=413915)
        >>> position = map.get_trending_position(time="alltime", result=5)
        >>> print(position)
        """
        data = find_top_maps(gameMode=self.gameModeGroup, **kwargs)
        position = 0

        for mapdata in data:
            if vars(self) == vars(mapdata):
                return position
            position = position + 1

    def get_comments(self, **kwargs):
        """A method used to used to create a list of `Comment` objects under a certain map.

        `before` - ID of comment to fetch results after, in order to not get duplicates.

        `limit` - Number of comments to return.

        Usage::

        >>> import intersection
        >>> map = intersection.map.get_map_details(mapId=413915)
        >>> comments = map.get_comments(limit=5)
        >>> for comment in comments: print(comment.comment)
        """
        return comment.list_comments_on_map(mapId=self.objectId, **kwargs)
    
    def get_thumbnail_url(self):
        """A method returning the url of the thumbnail image of a map.

        Usage::

        >>> import intersection
        >>> map = intersection.map.get_map_details(mapId=413915)
        >>> thumbnail_url = map.get_thumbnail_url()
        >>> print(thumbnail_url)
        """
        return get_map_thumbnail_url(mapId=self.objectId)

    def get_highscores(self, **kwargs):
        """A method used to used to create a list of `Highscore` objects on a certain map.

        `count` - Number of high scores to get.

        Usage::

        >>> import intersection
        >>> map = intersection.map.get_map_details(mapId=413915)
        >>> highscores = map.get_highscores(count=5)
        >>> for highscore in highscores: print(comment.comment)
        """
        return highscore.list_high_scores_on_map(mapId=self.objectId, **kwargs)

def search_for_maps(**kwargs):
    """A function used to used to create a list of `Map` objects matching a given name.

    `gameMode` - 1 = Simulation, 2 = Traffic Controller, 3 = Miscellaneous

    `maxversion` - The requester's game version, so if you have version 130 of the app you will not get maps that were made using 140 and might not be possible to play. Setting something very high such as 999 will just search for everything. If not added to the request then only maps made before beta will be searched for.

    `result` - Number of results to return on a page.

    `page` - Index of page of results to return, starting at page 0.

    `query` - Text to search for, will look at author name, map name and map description.

    Usage::

    >>> import intersection
    >>> maps = intersection.map.search_for_maps(gameMode=1, result=5, query="Feeeeddmmmeee")
    >>> for map in maps: print(map.name)
    """
    data = url.search_for_maps(**kwargs)
    maps = []
    for mapdata in data:
        maps.append(Map(
            mapdata['name'], 
            mapdata['desc'], 
            mapdata['gameModeGroup'], 
            mapdata['fileName'], 
            mapdata['fileExt'], 
            mapdata['author'], 
            mapdata['created'], 
            mapdata['updated'], 
            mapdata['gameVersion'], 
            mapdata['votesUp'], 
            mapdata['votesDown'],
            mapdata['highScore'],
            mapdata['highScoreUser'],
            mapdata['fullyUploaded'],
            mapdata['mapVersion'],
            mapdata['targetScore'],
            mapdata['favorites'],
            mapdata['deleted'],
            mapdata['objectId'],
            mapdata['authorName'],
        ))

    return maps

def find_top_maps(**kwargs):
    """A function used to used to create a list of `Map` objects in one of the top categories.

    `gameMode` - 1 = Simulation, 2 = Traffic Controller, 3 = Miscellaneous

    `time` - alltime / month / week / day

    `maxversion` - The requester's game version, so if you have version 130 of the app you will not get maps that were made using 140 and might not be possible to play. Setting something very high such as 999 will just search for everything. If not added to the request then only maps made before beta will be searched for.

    `result` - Number of results to return on a page.

    `page` - Index of page of results to return, starting at page 0.

    `trendsystem` - 0 or 1, should always be set to 1 as that is the current version used ingame.

    `offset` - How many weeks / months / days from today to give results for, negative to go back in time, positive will give future and thus usually an empty list.

    Usage::

    >>> import intersection
    >>> maps = intersection.map.find_top_maps(gameMode=1, time="alltime", result=5)
    >>> for map in maps: print(map.name)
    """

    data = url.find_top_maps(**kwargs)
    maps = []
    for mapdata in data:
        maps.append(Map(
            mapdata['name'], 
            mapdata['desc'], 
            mapdata['gameModeGroup'], 
            mapdata['fileName'], 
            mapdata['fileExt'], 
            mapdata['author'], 
            mapdata['created'], 
            mapdata['updated'], 
            mapdata['gameVersion'], 
            mapdata['votesUp'], 
            mapdata['votesDown'],
            mapdata['highScore'],
            mapdata['highScoreUser'],
            mapdata['fullyUploaded'],
            mapdata['mapVersion'],
            mapdata['targetScore'],
            mapdata['favorites'],
            mapdata['deleted'],
            mapdata['objectId'],
            mapdata['authorName'],
        ))

    return maps

def list_new_maps(**kwargs):
    """A function used to used to create a list of `Map` objects in the new category.

    `gameMode` - 1 = Simulation, 2 = Traffic Controller, 3 = Miscellaneous

    `maxversion` - The requester's game version, so if you have version 130 of the app you will not get maps that were made using 140 and might not be possible to play. Setting something very high such as 999 will just search for everything. If not added to the request then only maps made before beta will be searched for.

    `result` - Number of results to return on a page.

    `page` - Index of page of results to return, starting at page 0.

    Usage::

    >>> import intersection
    >>> maps = intersection.map.list_new_maps(gameMode=1, result=5)
    >>> for map in maps: print(map.name)
    """

    data = url.list_new_maps(**kwargs)
    maps = []
    for mapdata in data:
        maps.append(Map(
            mapdata['name'], 
            mapdata['desc'], 
            mapdata['gameModeGroup'], 
            mapdata['fileName'], 
            mapdata['fileExt'], 
            mapdata['author'], 
            mapdata['created'], 
            mapdata['updated'], 
            mapdata['gameVersion'], 
            mapdata['votesUp'], 
            mapdata['votesDown'],
            mapdata['highScore'],
            mapdata['highScoreUser'],
            mapdata['fullyUploaded'],
            mapdata['mapVersion'],
            mapdata['targetScore'],
            mapdata['favorites'],
            mapdata['deleted'],
            mapdata['objectId'],
            mapdata['authorName'],
        ))

    return maps

def list_maps_by_user(**kwargs):
    """A function used to used to create a list of `Map` objects uploaded by a certain user.

    `userId` - ID of user.

    `maxversion` - The requester's game version, so if you have version 130 of the app you will not get maps that were made using 140 and might not be possible to play. Setting something very high such as 999 will just search for everything. If not added to the request then only maps made before beta will be searched for.

    `result` - Number of results to return on a page.

    `page` - Index of page of results to return, starting at page 0.

    Usage::

    >>> import intersection
    >>> maps = intersection.map.list_maps_by_user(userId=2452411)
    >>> for map in maps: print(map.name)
    """

    data = url.list_maps_by_user(**kwargs)
    maps = []
    for mapdata in data:
        maps.append(Map(
            mapdata['name'], 
            mapdata['desc'], 
            mapdata['gameModeGroup'], 
            mapdata['fileName'], 
            mapdata['fileExt'], 
            mapdata['author'], 
            mapdata['created'], 
            mapdata['updated'], 
            mapdata['gameVersion'], 
            mapdata['votesUp'], 
            mapdata['votesDown'],
            mapdata['highScore'],
            mapdata['highScoreUser'],
            mapdata['fullyUploaded'],
            mapdata['mapVersion'],
            mapdata['targetScore'],
            mapdata['favorites'],
            mapdata['deleted'],
            mapdata['objectId'],
            mapdata['authorName'],
        ))

    return maps

def get_map_details(**kwargs):
    """A function used to used to create a `Map` object from it's ID.

    `mapId` - ID of map to get info about.

    Usage::

    >>> import intersection
    >>> map = intersection.map.get_map_details(mapId=413915)
    >>> print(map.name)
    """
    data = url.get_map_details(**kwargs)
    map = Map(
        data['name'], 
        data['desc'], 
        data['gameModeGroup'], 
        data['fileName'], 
        data['fileExt'], 
        data['author'], 
        data['created'], 
        data['updated'], 
        data['gameVersion'], 
        data['votesUp'], 
        data['votesDown'],
        data['highScore'],
        data['highScoreUser'],
        data['fullyUploaded'],
        data['mapVersion'],
        data['targetScore'],
        data['favorites'],
        data['deleted'],
        data['objectId'],
        data['authorName'],
    )

    return map

def get_map_thumbnail_url(**kwargs):
    """A function used to return a link to a map's thumbnail.

    `mapId` - ID of the map to get an image for.

    Usage::

    >>> import intersection
    >>> link = intersection.map.get_map_thumbnail_url(mapId=413915)
    >>> print(link)
    """

    data = url.get_map_thumbnail_url(**kwargs)
    return data