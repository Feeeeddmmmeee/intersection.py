from intersection.ext import url
from intersection import user, map

class Comment:
    """A class representing an IC comment.
    """

    def __init__(self, user, map, comment, flag, datePosted, rtl, objectId, username):
        self.user = user
        self.map = map
        self.comment = comment
        self.flag = flag 
        self.datePosted = datePosted
        self.rtl = rtl
        self.objectId = objectId
        self.username = username

    def get_author(self):
        """A method used to used to create a `User` object of the comment author.

        Usage::

        >>> import intersection
        >>> comment = intersection.comment.list_comments_on_map(mapId=413915, limit=1)
        >>> author = comment[0].get_author()
        >>> print(author.name)
        """
        return user.get_details_for_user(userId=self.user)
    
    def get_map(self):
        """A method used to used to create a `Map` object of the map the comment was posted on.

        Usage::

        >>> import intersection
        >>> comment = intersection.comment.list_comments_on_map(mapId=413915, limit=1)
        >>> map = comment[0].get_map()
        >>> print(map.name)
        """
        return map.get_map_details(mapId=self.map)

def list_comments_on_map(**kwargs):
    """A function used to used to create a list of `Comment` objects under a certain map.

    `mapId` - ID of map to list comments for.

    `before` - ID of comment to fetch results after, in order to not get duplicates.

    `limit` - Number of comments to return.

    Usage::

    >>> import intersection
    >>> comments = intersection.map.list_comments_on_map(mapId=413915, limit=5)
    >>> for comment in comments: print(comment.comment)
    """

    data = url.list_comments_on_map(**kwargs)
    comments = []
    for commentdata in data:
        comments.append(Comment(
            commentdata['user'],
            commentdata['map'],
            commentdata['comment'],
            commentdata['flag'],
            commentdata['datePosted'],
            commentdata['rtl'],
            commentdata['objectId'],
            commentdata['username'],
        ))

    return comments