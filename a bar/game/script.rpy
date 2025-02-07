define e = Character("Eileen")

screen love_points():
    zorder 100
    fixed:
        xalign 0.0
        yalign 0.5
        xsize 125
        ysize 716  # Increased by 30px to accommodate moved icon (686 + 30)

        # Meter Score Icon (moved down 30px)
        add "images/bar/meter_score.png":
            xpos 0
            ypos 35  #Important: so icon fits on bar
            xsize 125
            ysize 115
        # Percentage Text Display (NEW)
        text "{:.0f}%".format(love):
            xcenter 65  # Half of 125
            ypos 108    # 35 + (115/2) - centers on icon
            color "#ffffff"
            size 18

        # Love Bar (position adjusted relative to moved icon)
        vbar value AnimatedValue(love, max_love, delay=1.0):
            xpos 0
            ypos 145  # 30 (icon ypos) + 115 (icon height)
            xsize 125
            ysize 568 # so it stops at top of bar
            left_bar "images/bar/love_empty.png"
            right_bar ConditionSwitch(
                "love < 40", "images/bar/love_low.png",
                "love < 70", "images/bar/love_mid.png",
                "True", "images/bar/love_full.png"
            )
            thumb "images/bar/love_thumb.png"
            thumb_offset 25
default love = 50
default max_love = 100


label start:

    show screen love_points
    pause
    $ love += 50
    pause
    $ love -= 25
    pause
    #call code
    $ love += 10
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
