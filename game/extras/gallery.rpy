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
        g.hover_border = "assets/buttons/hoverborder.png"
        g.idle_border = "assets/buttons/idleborder.png"

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
        g.page("Characters")
        #
        # Note that we can give image and unlock image more than one image
        # at a time.
        
        #Burrito button and images
        g.button("assets/buttons/burrito.png")
        g.unlock_image("burrito")
        g.unlock_image("generic_character", "burrito normal")
        g.unlock_image("generic_character", "burrito happy")
        #KT button and images
        g.button("assets/buttons/katie.png")
        g.unlock_image("katie")
        g.unlock_image("generic_character", "katie")
        g.unlock_image("generic_character", "katie")



        # Another page, this one for concept art.
        g.page("Concept Art")
        #
        # We can apply conditions to buttons as well as to images.
        # The "condition" condition checks an arbitrary expression.
        #g.condition("persistent.beat_game")
        #
        # Various art
        g.button("assets/buttons/variousart.png")
        g.condition("persistent.beat_game") #Game not yet beaten, not unlocked button will show.
        g.display("assets/gallery/gallerytest1.png")
        g.display("assets/gallery/gallerytest2.png")
        g.display("assets/gallery/gallerytest3.png")
        g.display("assets/gallery/gallerytest4.png")
        
        # Placeholder art of characters
        g.button("assets/buttons/conceptartcharacters.png")
        g.display("burrito_placeholder")
        g.display("generic_character")
        g.display("katie_placeholder")
        g.display("atv_placeholder")
        g.display("abby_placeholder")
        g.display("digrat_placeholder")
        g.display("snake_placeholder")
        g.display("arc_placeholder")
        g.display("bj_placeholder")
        g.display("air_placeholder")
        g.display("brian_placeholder")
        g.display("flareon_placeholder")
        g.display("gator_placeholder")
        g.display("fontz_placeholder")
        g.display("gyra_placeholder")
        g.allprior()
        
        # Placeholder backgrounds
        g.button("assets/buttons/backgroundplaceholder.png")
        g.display("start_placeholder")
        g.display("lunch_placeholder")
        g.display("dorm_placeholder")
        g.display("outside_placeholder")
        g.allprior()
        

        # Now, show the gallery.
        g.show()

    jump main_menu_screen