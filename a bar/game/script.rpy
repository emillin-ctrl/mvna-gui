define e = Character("Eileen")


screen love_points():
    zorder 100
    vbar value AnimatedValue(love, max_love, delay=1.0):
        xalign 0.988 yalign 0.008
        xmaximum 47
        ymaximum 327
        left_bar Frame("images/bar/love_empty.png", 100, 10)
        right_bar Frame("images/bar/love_full.png", 100, 10)
        thumb "images/bar/love_thumb.png"
        thumb_offset 30
    imagebutton idle "images/bar/love_text.png" xalign 1.00 yalign 0.06 xmaximum 47 ymaximum 327 action NullAction()

default love = 1
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
