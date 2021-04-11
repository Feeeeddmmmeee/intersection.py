import intersection
from intersection.ext import errors

def compare_user_followers(*args):
    """A function used to compare the amount of followers of User objects. Returns the user with the most followers. You can pass an unlimited amount of User objects

        Example code
        -----------
        ```py
        import intersection
        from intersection.ext import tools

        example_user_object0 = intersection.user.get_user(2452411)
        example_user_object1 = intersection.user.get_user(2)

        print(tools.compare_user_followers(example_user_object0, example_user_object1).name)
        ```

        Output
        -----------
        Feeeeddmmmeee

        Another example
        -----------

        You can also pass in a list by using the `*` operator, note that you can pass several lists too

        Example code
        -----------
        ```py
        import intersection
        from intersection.ext import tools

        example_user_list = [intersection.user.get_user(2452411), intersection.user.get_user(2)]

        print(tools.compare_user_followers(*example_user_list))
        ```

        Output
        -----------
        Feeeeddmmmeee
    """
    final = intersection.user.User(0, 0, 0, 0, "no name", 0)
    final_backup = final

    for user in args:
        if user.followers > final.followers:
            final = user

    if final == final_backup:
        raise errors.noArgumentsError
    else:
        return final

def compare_map_likes(*args):
    """A function used to compare the amount of likes of Map objects. Returns the map with the most likes. You can pass an unlimited amount of Map objects

        Example code
        -----------
        ```py
        import intersection
        from intersection.ext import tools

        example_map_list = intersection.map.get_maps(2452411, 50, 0)

        print(tools.compare_map_likes(example_map_list[0], example_map_list[1]).name)
        ```

        Output
        -----------
        The Oak Ridge Place in Houston
    """

    final = intersection.map.Map("no name", "no desc", 0, "no fileName", "no fileExt", 0, 0, 0, 0, 0, 0, 0, 0, False, 0, 0, 0, False, 0, "no authorName")
    final_backup = final

    for map in args:
        if map.votesUp > final.votesUp:
            final = map

    if final == final_backup:
        raise errors.noArgumentsError
    else:
        return final