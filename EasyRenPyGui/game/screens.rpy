screen hp_bars_1v1:

    vbox:
        spacing 20
        xalign 0.1
        yalign 0.0
        xmaximum 600
        text "Player 1"
        bar value player_hp range player_max_hp
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.0
        xmaximum 600
        text "Skeleton"
        bar value enemy_hp range enemy_max_hp
