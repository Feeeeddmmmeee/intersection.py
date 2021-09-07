# intersection.py

An easy to use API wrapper with some basic functionality you would expect an API wrapper to have.

## Key Features

- User, Map, Comment and Highscore classes with their corresponding features.
- Functions used to get said objects from different sources.
- It's not really optimized but should work just fine.

## Installing

You can either use pip or copy the github repository.

pip (replace "version" with the version you want to download or alternatively just don't specify it.):
```sh
pip install intersection.py==version
```

### Required packages
The only other package this API wrapper requires is `requests`. In order to download it run this command:
```sh
pip install requests
```

## Quick example
```py
import intersection

my_user = intersection.user.get_details_for_user(userId=2452411)
print(my_user.name)

my_maps = my_user.get_user_maps()

for map in my_maps:
    print(map.name)

    comment = map.get_comments(limit=1)
    if len(comment):
        print("Latest comment: " + comment[0].comment)

    if map.gameModeGroup == 2:
        highscore = map.get_highscores(count=1)
        print("Highscore: " + highscore[0].score)
```
### JSON example
```py
from intersection.ext import url

my_user = url.get_details_for_user(userId=2452411)
print(my_user["name"])

my_maps = url.list_maps_by_user(userId=my_user["objectId"])

for map in my_maps:
    print(map["name"])

    comment = url.list_comments_on_map(mapId=map["objectId"], limit=1)
    if len(comment):
        print("Latest comment: " + comment[0]["comment"])

    if map["gameModeGroup"] == 2:
        highscore = url.list_high_scores_on_map(mapId=map["objectId"], count=1)
        print("Highscore: " + highscore[0]["score"])
```

## External links

- [PYPI Page (pip installation)](https://pypi.org/project/intersection.py/)
- [JavaScript version](https://github.com/RanggaGultom/ic-api) made by [RanggaGultom](https://github.com/RanggaGultom)
- [Github Repository](https://github.com/Feeeeddmmmeee/intersection.py)
