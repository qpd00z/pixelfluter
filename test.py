from pixelflut import Pixelflut

# set 'True' to switch on local and/or remote connection
local = True
remote = False

# set local connection (127.0.0.1)
conn_local = Pixelflut()

# set remote connection to ip of your remote pixelflut server
conn_remote = Pixelflut("192.168.178.83")

######################################################################
#                           TEST OPTIONS                             #
######################################################################
clear_screen            = True      # clear screen
draw_image              = True      # draw image full screen
draw_image_parametric   = True      # draw image parametric
magic_logo_flood        = True      # magic logo flood
draw_circle             = True      # draw single circle
render_char             = True      # render single char
render_text             = True      # render text

# test client functions with some nice maker kids presets
def test(conn):

    # clear screen
    if clear_screen:
        conn.clear_screen()

    # draw image full screen
    if draw_image:
        conn.draw_image("mklogo.png")

        # clear screen
        if clear_screen:
            conn.clear_screen()

    # draw image parametric
    if draw_image_parametric:
        conn.draw_image("tastaturtstern.png", 350, 248, 100, 100)

        # clear screen
        if clear_screen:
            conn.clear_screen()

    # magic logo flood
    if magic_logo_flood:
        conn.magic_logo_flood("tastaturtstern.png", 100, 100, 200)

        # clear screen
        if clear_screen:
            conn.clear_screen()

    # draw single circle       (                           )
    if draw_circle:
        conn.draw_circle(50, 400, 300, 255, 255, 255)

        # clear screen
        if clear_screen:
            conn.clear_screen()

    # render single char
    if render_char:
        # parameters:    (c,  r,   g,   b,   a,   px_size, pos_x, pos_y)
        conn.render_char("A", 255, 255, 255, 255, 10,      40,    250)

    # render text
    if render_text:
        conn_local.render_text("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 255, 255, 255, 255, 2, 40, 40)
        conn_local.render_text("abcdefghijklmnopqrstuvwxyz", 255, 255, 255, 255, 2, 40, 80)
        conn_local.render_text("0123456789", 255, 255, 255, 255, 2, 40, 120)
        conn_local.render_text(".,;:$1#'!\"/?%&()@", 255, 255, 255, 255, 2, 40, 160)
        conn_local.render_text("Der komplett verwahrloste Franz jagt im fixen Taxi quer durch Bayern!", 255, 255, 255, 255,
                           1, 40, 200)

if local:
    test(conn_local)

if remote:
    test(conn_remote)

