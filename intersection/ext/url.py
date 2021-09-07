import requests
requests.packages.urllib3.disable_warnings()

def search_for_maps(**kwargs):
    """A function used to get JSON user data instead of the standard object-oriented format.

    `gameMode` - 1 = Simulation, 2 = Traffic Controller, 3 = Miscellaneous

    `maxversion` - The requester's game version, so if you have version 130 of the app you will not get maps that were made using 140 and might not be possible to play. Setting something very high such as 999 will just search for everything. If not added to the request then only maps made before beta will be searched for.

    `result` - Number of results to return on a page.

    `page` - Index of page of results to return, starting at page 0.

    `query` - Text to search for, will look at author name, map name and map description.

    Usage::
    >>> from intersection.ext import url
    >>> maps = url.search_for_maps(gameMode=1, result=5, query="Feeeeddmmmeee")
    >>> for map in maps: print(map["name"])
    """
    if not "maxversion" in kwargs.keys(): kwargs["maxversion"] = "999"
    if not "page" in kwargs.keys(): kwargs["page"] = "0"
    if not "trendsystem" in kwargs.keys(): kwargs["trendsystem"] = "1"
    if not "offset" in kwargs.keys(): kwargs["trendsystem"] = "0"

    return requests.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/map/public/top/{str(kwargs['gameMode'])}/search?maxversion={str(kwargs['maxversion'])}&result={str(kwargs['result'])}&page={str(kwargs['page'])}&query={str(kwargs['query'])}", verify=False).json()

def find_top_maps(**kwargs):
    """A function used to get JSON top map data instead of the standard object-oriented format.

    `gameMode` - 1 = Simulation, 2 = Traffic Controller, 3 = Miscellaneous

    `time` - alltime / month / week / day

    `maxversion` - The requester's game version, so if you have version 130 of the app you will not get maps that were made using 140 and might not be possible to play. Setting something very high such as 999 will just search for everything. If not added to the request then only maps made before beta will be searched for.

    `result` - Number of results to return on a page.

    `page` - Index of page of results to return, starting at page 0.

    `trendsystem` - 0 or 1, should always be set to 1 as that is the current version used ingame.

    `offset` - How many weeks / months / days from today to give results for, negative to go back in time, positive will give future and thus usually an empty list.

    Usage::

    >>> from intersection.ext import url
    >>> maps = url.find_top_maps(gameMode=1, time="alltime", result=5)
    >>> for map in maps: print(map["name"])
    """
    if not "maxversion" in kwargs.keys(): kwargs["maxversion"] = "999"
    if not "page" in kwargs.keys(): kwargs["page"] = "0"
    if not "trendsystem" in kwargs.keys(): kwargs["trendsystem"] = "1"
    if not "offset" in kwargs.keys(): kwargs["trendsystem"] = "0"

    return requests.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/map/public/top/{str(kwargs['gameMode'])}/{str(kwargs['time'])}?maxversion={str(kwargs['maxversion'])}&result={str(kwargs['result'])}&page={str(kwargs['page'])}&trendsystem={str(kwargs['trendsystem'])}&offset={str(kwargs['offset'])}", verify=False).json()

def list_new_maps(**kwargs):
    """A function used to get JSON new map data instead of the standard object-oriented format.

    `gameMode` - 1 = Simulation, 2 = Traffic Controller, 3 = Miscellaneous

    `maxversion` - The requester's game version, so if you have version 130 of the app you will not get maps that were made using 140 and might not be possible to play. Setting something very high such as 999 will just search for everything. If not added to the request then only maps made before beta will be searched for.

    `result` - Number of results to return on a page.

    `page` - Index of page of results to return, starting at page 0.

    Usage::

    >>> from intersection.ext import url
    >>> maps = url.list_new_maps(gameMode=1, result=5)
    >>> for map in maps: print(map["name"])
    """
    if not "maxversion" in kwargs.keys(): kwargs["maxversion"] = "999"
    if not "page" in kwargs.keys(): kwargs["page"] = "0"

    return requests.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/map/public/new/{str(kwargs['gameMode'])}?maxversion={str(kwargs['maxversion'])}&result={str(kwargs['result'])}&page={str(kwargs['page'])}", verify=False).json()

def list_maps_by_user(**kwargs):
    """A function used to get JSON user map data instead of the standard object-oriented format.

    `userId` - ID of user.

    `maxversion` - The requester's game version, so if you have version 130 of the app you will not get maps that were made using 140 and might not be possible to play. Setting something very high such as 999 will just search for everything. If not added to the request then only maps made before beta will be searched for.

    `result` - Number of results to return on a page.

    `page` - Index of page of results to return, starting at page 0.

    Usage::

    >>> from intersection.ext import url
    >>> maps = url.list_maps_by_user(userId=2452411)
    >>> for map in maps: print(map["name"])
    """
    if not "result" in kwargs.keys(): kwargs["result"] = 50
    if not "maxversion" in kwargs.keys(): kwargs["maxversion"] = "999"
    if not "page" in kwargs.keys(): kwargs["page"] = "0"

    return requests.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/map/public/user/{str(kwargs['userId'])}?maxversion={str(kwargs['maxversion'])}&result={str(kwargs['result'])}&page={str(kwargs['page'])}", verify=False).json()

def list_comments_on_map(**kwargs):
    """A function used to get JSON comment data instead of the standard object-oriented format.

    `mapId` - ID of map to list comments for.

    `before` - ID of comment to fetch results after, in order to not get duplicates.

    `limit` - Number of comments to return.

    Usage::

    >>> from intersection.ext import url
    >>> comments = url.list_comments_on_map(mapId=413915, limit=5)
    >>> for comment in comments: print(comment["comment"])
    """
    before = ""
    if "before" in kwargs.keys(): before = f"&before={str(kwargs['before'])}"
    
    return requests.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/comment/public/{str(kwargs['mapId'])}?limit={str(kwargs['limit'])}{before}", verify=False).json()

def get_map_details(**kwargs):
    """A function used to get JSON map data from it's ID instead of the standard object-oriented format.

    `mapId` - ID of map to get info about.

    Usage::

    >>> from intersection.ext import url
    >>> map = url.get_map_details(mapId=413915)
    >>> print(map["name"])
    """
    return requests.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/map/public/{str(kwargs['mapId'])}/meta", verify=False).json()

def get_map_thumbnail_url(**kwargs):
    """A function used to get thumbnail data instead of the standard object-oriented format.

    `mapId` - ID of the map to get an image for.

    Usage::

    >>> from intersection.ext import url
    >>> link = url.get_map_thumbnail_url(mapId=413915)
    >>> print(link)
    """
    return f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/map/public/{str(kwargs['mapId'])}/thumb"

def search_for_users(**kwargs):
    """A function used to get JSON user data instead of the standard object-oriented format.

    `result` - Number of results to return on a page.

    `page` - Index of page of results to return, starting at page 0.

    `query` - Text to search for, looks at the username.

    Usage::

    >>> from intersection.ext import url
    >>> maps = url.search_for_user(result=5, query="Feeeeddmmmeee")
    >>> for user in users: print(user["name"])
    """
    if not "page" in kwargs.keys(): kwargs["page"] = "0"

    return requests.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/user2/public/search?result={str(kwargs['result'])}&page={str(kwargs['page'])}&query={str(kwargs['query'])}", verify=False).json()

def get_details_for_user(**kwargs):
    """A function used to get JSON user data instead of the standard object-oriented format.

    `userId` - ID of user to get info about.

    Usage::

    >>> from intersection.ext import url
    >>> user = url.get_details_for_user(userId=2452411)
    >>> print(user["name"])
    """

    return requests.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/user2/public/info/{str(kwargs['userId'])}", verify=False).json()

def list_high_scores_on_map(**kwargs):
    """A function used to get JSON highscore data instead of the standard object-oriented format.

    `mapId` - ID of map to get high scores for.

    `count` - Number of high scores to get.

    Usage::

    >>> from intersection.ext import url
    >>> highscores = url.list_high_scores_on_map(mapId=413915, count=5)
    >>> for highscore in highscores: print(highscore["score"])
    """

    return requests.get(f"https://tl3.shadowtree-software.se/TL3BackEnd/rest/highscore/public/{str(kwargs['mapId'])}?count={str(kwargs['count'])}", verify=False).json()