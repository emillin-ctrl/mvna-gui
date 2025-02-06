define e = Character("Eileen")


# screen love_points():
#     zorder 100
#     vbar value AnimatedValue(love, max_love, delay=1.0):
#         xalign 0.988 yalign 0.008
#         xmaximum 125
#         ymaximum 700
#         left_bar Frame("images/bar/love_empty.png", 100, 10)
#         right_bar Frame("images/bar/love_full.png", 100, 10)
#         thumb "images/bar/love_thumb.png"
#         thumb_offset 30
#     imagebutton idle "images/bar/love_text.png" xalign 1.00 yalign 0.06 xmaximum 47 ymaximum 327 action NullAction()

# default love = 1
# default max_love = 100

screen love_points():
    zorder 100
    fixed:
        xalign 0.988
        yalign 0.008
        xsize 125    # Bar width remains same
        ysize 571    # Updated total height

        # Visible bar area (using full height now)
        vbar value AnimatedValue(love, max_love, delay=1.0):
            area (0, 0, 125, 571)  # Use full image height
            left_bar "images/bar/love_empty.png"
            right_bar ConditionSwitch(
                "love < 40", "images/bar/love_low.png",
                "love < 70", "images/bar/love_mid.png",
                "True", "images/bar/love_full.png"
            )
            thumb "images/bar/love_thumb.png"
            thumb_offset 30

        # Counter image positioning
        imagebutton idle "images/bar/love_text.png":
            pos (125-47, 571-327)  # Bottom-aligned with bar
            xsize 47
            ysize 327
            action NullAction()

default love = 50
default max_love = 100


label start:

    show screen love_points
    pause
    $ love += 10
    pause
    $ love += 1
    pause
    #call code
    $ love += 1
    pause
    $ love += 1
    pause
    $ love += 1
    pause
    $ love += 1
    pause
    $ love += 1
    pause
    $ love += 1
    pause
    $ love += 1
    pause
    $ love += 1
    pause
    $ love += 1
    pause
    $ love += 10
    pause
    $ love += 10
    pause
    e "See how it grows (get your mind out of the gutter)"
    $ love += 10
    pause
    $ love += 10

    return
return
