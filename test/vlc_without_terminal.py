# Importing library
import vlc

print("Test VLC without terminal")
print("Choice your option: ", "1) Play Music","2) Play Video", sep="\n")
x = input("Enter your choice: ")

if x == "1":
    media = vlc.MediaPlayer("1.mp3")
    i = "notbreak"
    print("Controls:", "play", "pause", "stop", "exit", sep="\n")

    # y = input("Choose your option: ")

    while i == "notbreak":
        y = input()
        if y == "exit":
            i = "break"
        elif y == "play":
            media.play()
        elif y == "pause":
            media.pause()
        elif y == "stop":
            media.stop()
        else:
            print("Command no valid")

    # if y == "play":
    #     while i == "notbreak":
    #         media.play()
    #     else:
    #         print("finish")
    # if y == "exit":
    #     while i == "notbreak":
    #         i = "break"
    #     else:
    #         print("finish")

    # while i == "notbreak":
    #     media.play()
    #     if y == "break":
    #         i = "break"
    # else:
    #     print("Finish")

    #     if y == "play":
    #         media.play()
    #     elif y == "pause":
    #         media.pause()
    #     elif y == "stop":
    #         media.stop()
    # else:
    #     print("Finish")