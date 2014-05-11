init:
    # Position the navigation on the right side of the screen.
    $ style.gallery_nav_frame.xpos = 800 - 10
    $ style.gallery_nav_frame.xanchor = 1.0
    $ style.gallery_nav_frame.ypos = 12

    # Add the gallery to the main menu.
    $ config.main_menu.insert(2, ('Gallery', "gallery", "True"))

# The entry point to the gallery code.
label gallery:
    python hide:

        # Construct a new gallery object.
        g = Gallery()

        # The image used for locked buttons.
        g.locked_button = "assets/buttons/lockedart.png"

        # The background of a locked image.
        g.locked_background = Solid("#808080")

        # Frames added over unlocked buttons, in hover and idle states.
        g.hover_border = "assets/buttons/gallerybuttontest.png"
        g.idle_border = "assets/buttons/gallerybuttontest.png"

        # An images used as the background of the various gallery pages.
        g.background = Solid((0, 0, 0, 255))

        # Lay out the gallery images on the screen.
        # These settings lay images out 3 across and 4 down.
        # The upper left corner of the gird is at xpos 10, ypos 20.
        # They expect button images to be 155x112 in size.
        g.grid_layout((3, 4), (10, 12), (160, 124))

        # Show the background page.
        g.page("Backgrounds")

        # Our first button is a picture of the beach.
        g.button("assets/buttons/backgrounds.png")
        #
        # These show images, if they have been unlocked. The image name must
        # have been defined using an image statement.
        g.unlock_image("outside")
        g.unlock_image("placeholder_lunch")
        #
        # This shows a displayable...
        g.display("dorm")
        # ... if all prior images have been show.
        g.allprior()

        # A second set of images.
        #g.button("thumb_lighthouse.jpg")
        #g.unlock_image("bg lighthouse day")
        #g.unlock_image("bg lighthouse night")
        #g.display("lighthouse_sketch.jpg")
        #g.allprior()



        # We can use g.page to introduce a second page.
        #g.page("Characters")

        #g.button("thumb_eileen.jpg")
        #
        # Note that we can give image and unlock image more than one image
        # at a time.
        #g.unlock_image("bg lighthouse day", "eileen day happy")
        #g.unlock_image("bg lighthouse day", "eileen day mad")



        # Another page, this one for concept art.
        g.page("Concept Art")

        g.button("assets/buttons/gallerybuttontest.png")
        #
        # We can apply conditions to buttons as well as to images.
        # The "condition" condition checks an arbitrary expression.
        #g.condition("persistent.beat_game")
        #
        g.display("assets/backgrounds/gallerytest1.png")
        g.display("assets/backgrounds/gallerytest2.png")
        g.display("assets/backgrounds/gallerytest3.png")
        g.display("assets/backgrounds/gallerytest4.png")


        # Now, show the gallery.
        g.show()

    jump main_menu_screen