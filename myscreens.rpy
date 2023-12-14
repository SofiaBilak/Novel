# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
screen firstScreen():
    # add "bg next.png"
    imagemap:
        ground "bg next.png"
        hotspot(1166, 257, 119, 173) action Jump("continue_game")
        #hotspot(78, 223, 150, 102) action Jump("continue_play")

screen secondScreen():
    imagemap:
        ground "bg next.png"
        #hotspot(1166, 257, 119, 173) action Jump("continue_game")
        hotspot(78, 223, 150, 102) action Jump("continue_play")

screen thirdScreen():
    imagemap:
        ground "bg next.png"
        hotspot(146, 525, 120, 109) action Show("firstCompleted")

screen firstCompleted():
    add "bg one.png"
    imagemap:
        ground "bg one.png"
        hotspot(1811, 15, 93, 129) action Show("secondCompleted")

screen secondCompleted():
    add "bg two.png"
    imagemap:
        ground "bg two.png"
        hotspot(1196, 929, 113, 91) action Show("thirdCompleted"), Jump("continue_to_play")

screen thirdCompleted():
    add "bg three.png"

screen fourthScreen():
    add "bg unlocked.png"
    
