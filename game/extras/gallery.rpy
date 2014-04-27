init python:
    g = Gallery()

    # A button that contains an image that automatically unlocks.
    g.button("gallery_test_1")
    g.image("gallery_test_1")
    g.unlock("gallery_test_1")

    # This button has multiple images assocated with it. We use unlock_image
    # so we don't have to call both .image and .unlock. We also apply a
    # transform to the first image.
    g.button("gallery_test_1")
    g.unlock_image("gallery_test_1")

    g.unlock_image("gallery_test_1")
    g.unlock_image("gallery_test_2")

    # The transition used when switching images.
    g.transition = dissolve

screen gallery:

    # Ensure this replaces the main menu.
    tag menu

    # The background.
    add "bg standard"

    # A grid of buttons.
    grid 2 1:

        xfill True
        yfill True

        # Call make_button to show a particular button.
        add g.make_button("gallery_test_1", "gallery_test_1", xalign=0.5, yalign=0.5)

        # The screen is responsible for returning to the main menu. It could also
        # navigate to other gallery screens.
        textbutton "Return" action Return() xalign 0.5 yalign 0.5