import intersection.url
import intersection.errors
from intersection import map

class User:
    """A class representing an IC user

    You can use the provided functions to get the user object from either their name or their ``ID``
    The required __init__ arguments are: ``objectId, gameVersion, lastLogin, maps, name, followers``

    lastLogin is represented in milliseconds

    Example code
    -----------
    ```py
    import user

    example_user_object = User(1, 1, 1, 1, "name", 1)

    print(example_user_object.name)
    ```

    Output
    -----------
    name
    """
    
    def __init__(self, objectId, gameVersion, lastLogin, maps, name, followers):
        self.objectId = objectId
        self.gameVersion = gameVersion
        self.lastLogin = lastLogin
        self.maps = maps
        self.name = name
        self.followers = followers

    def get_user_maps(self, resultsPerPage, page):
        """A function allowing you to create a ``Map`` object from an ``User`` object

        For creating a ``Map`` object from its author's ID look for: ``map.get_maps()``

        50 is currently the highest possible amount of maps so setting ``resultsPerPage`` to 50 will return all the maps that user has

        Example code
        -----------
        ```py
        import user

        example_user_object = user.get_user(2452411)

        example_map_list = example_user_object.get_user_maps(1, 0)

        print(example_map_list[0].authorName)
        ```

        Output
        -----------
        Feeeeddmmmeee
        """

        maps = []

        api = intersection.url.url.map_user(self.objectId, resultsPerPage, page)

        for i in range(len(api)):

            temp = map.Map(
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


def get_user(id):
    """A function allowing you to create an ``User`` object from an ``ID``

    For creating an ``User`` object from the ``Name`` look for: ``search_for_users(name)``

    Example code
    -----------
    ```py
    import user

    example_user_object = user.get_user(2452411)

    print(example_user_object.name)
    ```

    Output
    -----------
    Feeeeddmmmeee
    """

    api = intersection.url.url.user_info(id)

    user = User(
        int(api['objectId']),
        int(api['gameVersion']),
        int(api['lastLogin']),
        int(api['maps']),
        api['name'],
        int(api['followers'])
    )

    return user

def search_for_users(name):
    """A function allowing you to create a list of ``User`` objects from a ``name``

    For creating an ``User`` object from the ``ID`` look for: ``get_user(id)``

    Example code
    -----------
    ```py
    import user

    example_user_object_list = user.search_for_users("Feeeeddmmmeee")

    print(example_user_object_list[0].name)
    ```

    Output
    -----------
    .Feeeeddmmmeee

    Note
    -----------
    The output isn't the same as if we used the get_user() function. That's because it's using IC's search algorithm and it returns all the users with a matching name. User with the exact name as what we searched for may be among them.
    """

    user = []

    api = intersection.url.url.user_search(name)
    
    for i in range(len(api)):

        api2 = intersection.url.url.user_info(api[i]['objectId'])

        temp = User(
            int(api[i]['objectId']), 
            int(api2['gameVersion']),
            int(api2['lastLogin']),
            int(api2['maps']),
            api2['name'],
            int(api2['followers'])
        )

        user.append(temp)

    return user