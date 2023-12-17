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

screen flashlightFound():
    imagemap:
        ground "bg next.png"
        hotspot(410, 844, 303, 153) action Jump("flashlight_found")

screen thirdScreen():
    imagemap:
        ground "bg next1.png"
        hotspot(146, 525, 120, 109) action Jump("first_completed")

screen firstCompleted():
    #add "bg one.png"
    imagemap:
        ground "bg one.png"
        hotspot(1811, 15, 93, 129) action Jump("second_completed")

screen secondCompleted():
    #add "bg two.png"
    imagemap:
        ground "bg two.png"
        hotspot(1196, 929, 113, 91) action Jump("third_completed")#, Jump("continue_to_play")

screen thirdCompleted():
    #add "bg three.png"
    imagemap:
        ground "bg three.png"
        hotspot(1380, 443, 291, 392) action Jump("fourth_screen")#, Jump("play_next")

screen findNote2():
    imagemap:
        ground "bg location2"
        hotspot(448, 199, 115, 124) action Jump("continue_search")

screen findCamera():
    imagemap:
        ground "bg location2"
        hotspot(697, 293, 148, 98) action Jump("find_camera")

screen firsParticle():
    imagemap:
        ground "bg location2"
        hotspot(1467, 998, 65, 32) action Jump("keep_searching")

screen secondParticle():
    imagemap:
        ground "bg location21"
        hotspot(1566, 975, 58, 29) action Jump("keep_looking")

screen lastParticle():
    imagemap:
        ground "bg location22"
        hotspot(1297, 962, 67, 32) action Jump("keep_going")
