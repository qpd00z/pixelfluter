from pixelflut import Pixelflut

# set 'True' to switch on local and/or remote connection
local = True
remote = False


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

# clear screen
def clr(conn):
    if clear_screen:
        conn.clear_screen()

# test client functions with some nice maker kids presets
def test(conn):

    # clear screen
    clr(conn)

    # draw image full screen
    if draw_image:
        conn.draw_image("mklogo.png")
        clr(conn)  # clear screen

    # draw image parametric
    if draw_image_parametric:
        conn.draw_image("tastaturtstern.png", 350, 248, 100, 100)
        clr(conn)  # clear screen

    # magic logo flood
    if magic_logo_flood:
        conn.magic_logo_flood("tastaturtstern.png", 100, 100, 200)
        clr(conn)  # clear screen

    # draw single circle       (                           )
    if draw_circle:
        conn.draw_circle(50, 400, 300, 255, 255, 255)
        clr(conn)  # clear screen

    # render single char
    if render_char:
        # parameters:    (c,  r,   g,   b,   a,   px_size, pos_x, pos_y)
        conn.render_char("A", 255, 255, 255, 255, 10,      40,    250)
        clr(conn)  # clear screenpix

    # render text
    if render_text:
        conn_local.render_text("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 255, 255, 255, 255, 2, 40, 40)
        conn_local.render_text("abcdefghijklmnopqrstuvwxyz", 255, 255, 255, 255, 2, 40, 80)
        conn_local.render_text("0123456789", 255, 255, 255, 255, 2, 40, 120)
        conn_local.render_text(".,;:$1#'!\"/?%&()@", 255, 255, 255, 255, 2, 40, 160)
        conn_local.render_text("Der komplett verwahrloste Franz jagt im fixen Taxi quer durch Bayern!", 255, 255, 255, 255,
                           1, 40, 200)

# set local connection (127.0.0.1)
if local == True:
    conn_local = Pixelflut()
    test(conn_local)

# set remote connection to ip of your remote pixelflut server
if remote == True:
    conn_remote = Pixelflut("192.168.178.83")
    test(conn_remote)