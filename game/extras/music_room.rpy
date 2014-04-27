init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Step 2. Add music files.
    mr.add("assets/music/intro_theme.mp3", always_unlocked=True)

screen music_room:

    tag menu

    frame:
        has vbox

        # The buttons that play each track.
        textbutton "Intro Theme" action mr.Play("assets/music/intro_theme.mp3")

        null height 20

        # Buttons that let us advance tracks.
        textbutton "Next" action mr.Next()
        textbutton "Previous" action mr.Previous()

        null height 20

        # The button that lets the user exit the music room.
        textbutton "Main Menu" action ShowMenu("main_menu")

    # Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", "assets/music/intro_theme.mp3")