# intersection.py

A not so easy to use API wrapper for IC's API with a few features.

## Key Features

- User and Map classes with all the features that IC maps or users have
- Several functions related to these classes
- It's not really optimized but should work just fine

## Installing

**Python is required**. Currently there's no "official" way to download the library so you can just download the newest version from github.
To do that you can use the following command:
```sh
$ git clone https://github/Feeeeddmmmeee/intersection.py
```

The requests library is also required.

# Code Examples

## User class
```py
# Importing the library
import intersection

# Creating a variable "example_user" that will store the User object created with the get_user() function
example_user = intersection.user.get_user(2452411)

# Printing the user's name
print(example_user.name)
```

## Map class
```py
# Importing the library
import intersection

# Creating a variable called "example_maps" with the get_maps() function. 
example_maps = intersection.map.get_maps(2452411, 1, 0) 

# Printing the author's name
print(example_maps[0].authorName)
```
