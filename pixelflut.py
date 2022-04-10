"""
################################################################################
#                                                                              #
#                 fl00dt00l P I X E L F L U T   C L I E N T                    #
#                                                                              #
################################################################################
"""

import socket
import math
import random
from PIL import Image
# from fonts import led8x6
from fonts import led9x7


class Pixelflut:
    
    def __init__(self, host="127.0.0.1", port=1337):
        
        # server data
        self.__HOST = host  # initially set to localhost (127.0.0.1)
        self.__PORT = port  # initially set to pixelflut's standard port 1337
                
        # connection
        self.so = socket.socket()
        self.so.connect((self.__HOST, self.__PORT))

        # pathes
        self.__PATH_IMG = "./img/"  # path to images directory (closing /)

        # handler
        self.im = ""

        # screen dimensions
        self.__XMAX = 800  # screen width
        self.__YMAX = 600  # screen height

        # color initially set to white
        self.color_r = 255  # red
        self.color_g = 255  # green
        self.color_b = 255  # blue
        self.color_a = 255  # alpha

        # init pixel pointer (0|0)
        self.pointer_x = 0
        self.pointer_y = 0

        # fonts
        self.__FONT = led9x7.led9x7  # font data

    def set_host(self, host):
        self.__HOST = host
        
    def get_host(self):
        return self.__HOST

    def set_port(self, port):
        self.__PORT = port

    def get_port(self):
        return self.__PORT

    def set_font(self, font):
        self.__FONT = font

    def get_font(self):
        return self.__FONT

    # set pixel pointer
    def set_pointer(self, x=0, y=0):
        self.pointer_x = x
        self.pointer_y = y

    ######################################################################
    #                          COLOR SETTING                             #
    ######################################################################

    # set drawing color and alpha
    def set_color(self, r=255, g=255, b=255, a=255):
        self.color_r = r
        self.color_g = g
        self.color_b = b
        self.color_a = a

    # set color channel red
    def set_color_r(self, r=255):
        self.color_r = r

    # set color channel green
    def set_color_g(self, g=255):
        self.color_g = g

    # set color channel blue
    def set_color_b(self, b=255):
        self.color_b = b

    # set color channel alpha
    def set_color_a(self, a=255):
        self.color_a = a

    ######################################################################
    #                          IMAGE SETTING                             #
    ######################################################################

    # set image path
    def set_image_path(self, img_path):
        self.__PATH_IMG = img_path

    # set image file handler
    def set_image_source(self, img_path, img_filename, img_mode='RGBA'):
        self.im = Image.open(img_path + img_filename).convert(img_mode)  # read image file

    ######################################################################
    #                           CLEAR SCREEN                             #
    ######################################################################

    # clear screen
    def clear_screen(self):
        for y in range(self.__YMAX):
            for x in range(self.__XMAX):
                self.pixel(x, y, 0, 0, 0, a=255)

    ######################################################################
    #                          DRAW SINGLE PIX                           #
    ######################################################################

    # draw single pixel
    def pixel(self, x, y, r, g, b, a=255):
        if a == 255:
            payload = bytes("PX %d %d %02x%02x%02x\n" % (x, y, r, g, b), "ascii")
        else:
            payload = bytes("PX %d %d %02x%02x%02x%02x\n" % (x, y, r, g, b, a), "ascii")
        
        self.so.sendall(payload)

    ######################################################################
    #                          DRAW IMAGE FILE                           #
    ######################################################################

    # draw image from file
    def draw_image(self, img_filename, pos_x=0, pos_y=0, size_x=0, size_y=0):
        # self.set_image_source(self.__PATH_IMG, img_filename) # read image
        self.im = Image.open(self.__PATH_IMG + img_filename).convert('RGBA')   # read image file

        # img_width  = self.im.size[0]
        # img_height = self.im.size[1]
        # print(img_width)
        # print(img_height)

        if size_x == 0:            # if horizontal size not set, set to max
            size_x = self.__XMAX
        if size_y == 0:            # if vertical size not set, set to max
            size_y = self.__YMAX

        self.im.thumbnail((size_x, size_y), Image.ANTIALIAS)  # create thumbnail
        _, _, width, height = self.im.getbbox()

        for x in range(width):
            for y in range(height):
                r, g, b, a = self.im.getpixel((x, y))
                self.pixel(pos_x + x, pos_y + y, r, g, b, a)

    ######################################################################
    #                         MAGIC LOGO FLOOD                           #
    ######################################################################

    # draw logo image in random color at random position
    def magic_logo_flood(self, img_filename, size_x=0, size_y=0, loops=100):
        self.im = Image.open(self.__PATH_IMG + img_filename).convert('RGBA')   # read image file
        self.im.thumbnail((size_x, size_y), Image.ANTIALIAS)  # create thumbnail
        _, _, width, height = self.im.getbbox()

        for i in range(loops):

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            pos_x = random.randint(0, self.__XMAX - size_x)
            pos_y = random.randint(0, self.__YMAX - size_y)

            for x in range(width):
                for y in range(height):
                    _, _, _, a = self.im.getpixel((x, y))
                    self.pixel(pos_x + x, pos_y + y, r, g, b, a)

    ######################################################################
    #                            DRAW CIRCLE                             #
    ######################################################################

    # draw circle
    def draw_circle(self, rad, x, y, r, g, b, a=255):
        for i in range(360):
            xc = int(rad * math.cos(i))
            ys = int(rad * math.sin(i))
            self.pixel(x+xc, y+ys, r, g, b, a)

    ######################################################################
    #                            RENDER CHAR                             #
    ######################################################################

    # render single char
    def render_char(self, c, r, g, b, a=255, px_size=1, start_x=0, start_y=0):

        pos_x = start_x
        pos_y = start_y

        if c in self.__FONT.keys():  # check if char is included in font

            # iterate rows
            for row in range(len(self.__FONT[c])):

                for k in range(px_size):
                    # iterate cols
                    for col in range(len(self.__FONT[c][row])):

                        if self.__FONT[c][row][col] == 1:
                            # set pixel
                            for m in range(px_size):
                                self.pixel(pos_x, pos_y, r, g, b, a)
                                pos_x = pos_x + 1
                        else:
                            # set blank
                            for n in range(px_size):
                                pos_x = pos_x + 1

                    pos_y = pos_y + 1  # new line
                    pos_x = start_x    # carriage return

            self.pointer_x = self.pointer_x + px_size * (len(self.__FONT[c][0]) + 2)

    ######################################################################
    #                            RENDER TEXT                             #
    ######################################################################

    # render text
    def render_text(self, txt, r, g, b, a=255, px_size=1, start_x=0, start_y=0):

        self.pointer_x = start_x
        self.pointer_y = start_y

        for c in txt:
            self.render_char(c, r, g, b, a, px_size, self.pointer_x, self.pointer_y)
