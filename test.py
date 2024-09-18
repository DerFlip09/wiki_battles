from article import *
from player import *
import string


title = "Python (Programming Language)"
content = get_content_with_title(title)

player_1 = {"stats": COMMAND_DISPATCHER.copy()}
player_2 = {"stats": {1: "Count of Words", 2: "Count of images"}}

del player_1["stats"][1]

print(player_1["stats"])

del player_1["stats"][5]

print(player_1["stats"])